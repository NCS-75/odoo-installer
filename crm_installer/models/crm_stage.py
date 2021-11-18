# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmStage(models.Model):
    _inherit = "crm.stage"

    worksite_completed = fields.Boolean("Worksite completed")
    guarantees_granted = fields.Boolean("Guarantees granted")
