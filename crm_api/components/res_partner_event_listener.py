from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if
from odoo.addons.queue_job.job import identity_exact


class ResPartnerEventListener(Component):
    _name = "res.partner.event.listener"
    _inherit = "base.event.listener"

    _apply_on = ["res.partner"]

    def _get_skip_if_condition(self, record, **kwargs):
        return False  # TODO FIXME !!

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

    # # fmt: off
    # @skip_if(
    #     lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    # )
    # # fmt: on
    # def on_record_unlink(self, record, fields=None):
    #     self._export_partner_delete(record, fields=fields)

    def _export_partner_info(self, record, fields=None):
        print("_export_partner_info", record.id)
        record.with_delay(
            description="update partner %s" % (record.id,),
            identity_key=identity_exact, # ensure will call WS only once
        )._notify_partner_update()
        