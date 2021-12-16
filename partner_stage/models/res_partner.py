# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    stage_id = fields.Many2one(
        string="Installer Stage",
        comodel_name="res.partner.stage",
        ondelete="set null",
        group_expand="_read_group_stage_ids",
        store=True,
        index=True,
        readonly=False,
        copy=False,
        help="Installer Qualification Stage",
    )

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """Display all the stages"""
        search_domain = [("id", "!=", False)]
        stage_ids = stages._search(
            search_domain, order=order, access_rights_uid=SUPERUSER_ID
        )
        return stages.browse(stage_ids)

class ResPartnerStage(models.Model):
    _name = "res.partner.stage"
    _description = "Installers Qualification Stages"
    _rec_name = "name"
    _order = "sequence, name, id"

    name = fields.Char(string="Name", translate=True, index=True)
    code = fields.Char("Code")
    sequence = fields.Integer(
        "Sequence", default=1, help="Used to order stages. Lower is better."
    )
    fold = fields.Boolean("Folded in kanban view")

    def name_get(self):
        res = []
        for stg_id in self:
            res.append((stg_id.id, "%s - %s" % (stg_id.code, stg_id.name)))
        return res
