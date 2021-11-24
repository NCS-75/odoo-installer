# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = ["sale.order", "report.tools.mixin"]
    _name = "sale.order"

    has_product_photo = fields.Boolean(compute="_compute_has_product_photo")
    display_uom = fields.Boolean(compute="_compute_display_uom")

    def _compute_has_product_photo(self):
        for rec in self:
            rec.has_product_photo = any(rec.order_line.product_id.mapped("image_1920"))

    def _compute_display_uom(self):
        unit_id = self.env.ref("uom.product_uom_unit")
        for rec in self:
            rec.display_uom = bool(rec.order_line.product_uom - unit_id)
