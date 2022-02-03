# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmStage(models.Model):
    _inherit = "crm.stage"

    on_change = fields.Boolean(default=True)

    worksite_completed = fields.Boolean("Worksite completed")
    guarantees_granted = fields.Boolean("Guarantees granted")

    is_myds = fields.Boolean(
        string="Is a MyDS stage?",
        default=False,
        readonly=True,
        help="Technical field only True for hard-coded SQL stages related to MyDS API",
    )
    myds_stage_id = fields.Many2one(
        string="Related MyDS Stage",
        comodel_name="crm.stage",
        domain="[('is_myds', '=', True)]",
        help="Required to connect leads with MyDS API",
    )
