# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    worksite_completed = fields.Boolean(
        related="stage_id.worksite_completed", store=True
    )
    guarantees_granted = fields.Boolean(
        related="stage_id.guarantees_granted", store=True
    )
