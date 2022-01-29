from odoo.addons.component.core import Component
from odoo.addons.component_event import skip_if
from odoo.addons.queue_job.job import identity_exact


class CrmLeadEventListener(Component):
    _name = "crm.lead.event.listener"
    _inherit = "base.event.listener"

    _apply_on = ["crm.lead"]

    def _get_skip_if_condition(self, record, **kwargs):
        return False  # TODO FIXME !!

    # fmt: off
    @skip_if(
        lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    )
    # fmt: on
    def on_record_create(self, record, fields=None):
        self._export_lead_info(record, fields=fields)

    # fmt: off
    @skip_if(
        lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    )
    # fmt: on
    def on_record_write(self, record, fields=None):
        self._export_lead_info(record, fields=fields)

    # # fmt: off
    # @skip_if(
    #     lambda self, record, **kwargs: self._get_skip_if_condition(record, **kwargs)
    # )
    # # fmt: on
    # def on_record_unlink(self, record, fields=None):
    #     self._export_partner_delete(record, fields=fields)

    def _export_lead_info(self, record, fields=None):
        record.with_delay(
            description="update lead %s" % (record.id,),
            identity_key=identity_exact, # ensure will call WS only once
        )._notify_lead_update()
        