# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    headcount = fields.Integer("Headcount")
    annual_revenue = fields.Monetary("Annual Revenue", currency_field="currency_id")
    share_capital = fields.Monetary("Share Capital", currency_field="currency_id")
    coworker_ids = fields.Many2many(
        string="Coworkers",
        comodel_name="res.partner",
        relation="res_partner_coworker",
        column1="res_partner",
        column2="coworker",
        compute="_compute_coworker_ids",
        help="Employees from the same company as current partner",
    )

    @api.depends(
        "parent_id", "parent_id.is_company", "child_ids.is_company", "child_ids.type"
    )
    def _compute_coworker_ids(self):
        for rec in self:
            company_id = rec.parent_id.filtered("is_company")
            employee_ids = company_id.child_ids.filtered(
                lambda p: p.type == "contact" and p.is_company == False
            )
            rec.coworker_ids = employee_ids - rec
