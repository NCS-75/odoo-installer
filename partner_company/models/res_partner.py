# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    headcount = fields.Integer("Headcount")
    annual_revenue = fields.Monetary("Annual Revenue", currency_field="currency_id")
    share_capital = fields.Monetary("Share Capital", currency_field="currency_id")
