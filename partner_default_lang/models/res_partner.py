# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def default_get(self, default_fields):
        """Define current company's lang as fallback default lang"""
        vals = super().default_get(default_fields)
        parent = self.env["res.partner"]
        if "parent_id" in default_fields and vals.get("parent_id"):
            parent = self.browse(vals.get("parent_id"))
        if "lang" in default_fields:
            vals["lang"] = parent.lang or self.env.company.partner_id.lang
        return vals
