# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    date_order = fields.Datetime(
        states={
            "draft": [("readonly", False)],
            "sent": [("readonly", False)],
            "sale": [("readonly", False)],
        }
    )
