# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartnerRelation(models.Model):
    _name = "res.partner.relation"
    _description = "Relationship"
    _rec_name = "name"
    _order = "sequence, name"

    name = fields.Char("Name", translate=True)
    code = fields.Char("Code")
    sequence = fields.Integer()

    role_ids = fields.Many2many(
        string="Relation visibility",
        comodel_name="res.partner.role",
        help="Define if the Relation is visible on partners with specific Roles.\nIf "
        "empty, the relation is visible on all the partners, even those with no Role.",
    )

    def name_get(self):
        res = []
        for rel_id in self:
            res.append((rel_id.id, "%s - %s" % (rel_id.code, rel_id.name)))
        return res


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _default_relation_id(self):
        rel_id = self.env["res.partner.relation"].search([("code", "=", "0")], limit=1)
        return rel_id.id

    relation_id = fields.Many2one(
        string="Relationship",
        comodel_name="res.partner.relation",
        help="Relationship level with this partner.",
        default=_default_relation_id,
    )
