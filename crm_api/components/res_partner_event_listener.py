from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if
from odoo.addons.queue_job.job import identity_exact


class ResPartnerEventListener(Component):
    _name = "res.partner.event.listener"
    _inherit = "base.event.listener"
    _apply_on = ["res.partner"]

    def _get_skip_if_condition(self, record, **kwargs):
        if not record.myds_id or self.env.context.get('connector_no_export'):
            return True
        else:
            return False

    # fmt: off
    @skip_if(
        lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    )
    # fmt: on
    def on_record_create(self, record, fields=None):
        self._export_partner_info(record, fields=fields)

    # fmt: off
    @skip_if(
        lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    )
    # fmt: on
    def on_record_write(self, record, fields=None):
        self._export_partner_info(record, fields=fields)

    def _export_partner_info(self, record, fields=None):
        record.with_delay(
            description="update partner %s" % (record.id,),
            identity_key=identity_exact, # ensure will call WS only once
            max_retries=5,
        ).notify_myds_update()
