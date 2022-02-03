# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    is_quoted = fields.Boolean(
        string="Quotation made", compute="_compute_quotation", store=True
    )
    is_ordered = fields.Boolean(
        string="Quotation signed", compute="_compute_quotation", store=True
    )

    @api.depends("quotation_count", "sale_order_count")
    def _compute_quotation(self):
        for rec in self:
            rec.is_quoted = bool(rec.quotation_count) or bool(rec.sale_order_count)
            rec.is_ordered = bool(rec.sale_order_count)
