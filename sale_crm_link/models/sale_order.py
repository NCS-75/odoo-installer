# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_view_lead(self):
        self.ensure_one()
        if self.opportunity_id:
            action_xmlid = "crm.crm_lead_action_pipeline"
            action = self.env["ir.actions.actions"]._for_xml_id(action_xmlid)
            form = self.env.ref("crm.crm_lead_view_form")
            action.update(
                {"views": [(form.id, "form")], "res_id": self.opportunity_id.id}
            )
            return action
        else:
            return True
