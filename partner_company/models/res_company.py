# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    share_capital = fields.Monetary(
        "Share Capital",
        related="partner_id.share_capital",
        store=True,
        readonly=False,
        currency_field="currency_id",
    )
