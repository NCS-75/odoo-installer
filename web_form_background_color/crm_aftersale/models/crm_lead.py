# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    worksite_completed = fields.Boolean(
        related="stage_id.worksite_completed", store=True
    )
    guarantees_granted = fields.Boolean(
        related="stage_id.guarantees_granted", store=True
    )

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """Override native '_read_group_stage_ids' to display and fold columns depending
        on context"""
        stage_ids = super()._read_group_stage_ids(stages, domain, order)
        res_stage_ids = stage_ids

        if self._context.get("aftersale"):
            res_stage_ids.filtered(lambda s: not s.fold_aftersales).sudo().write(
                {"fold": False}
            )
            res_stage_ids.filtered(lambda s: s.fold_aftersales).sudo().write(
                {"fold": True}
            )
        else:
            res_stage_ids.filtered(lambda s: not s.fold_pipeline).sudo().write(
                {"fold": False}
            )
            res_stage_ids.filtered(lambda s: s.fold_pipeline).sudo().write(
                {"fold": True}
            )

        return res_stage_ids


class CrmStage(models.Model):
    _inherit = "crm.stage"

    fold_pipeline = fields.Boolean("Folded in main Pipeline")
    fold_aftersales = fields.Boolean("Folded in After-Sales")
    worksite_completed = fields.Boolean("Worksite completed")
    guarantees_granted = fields.Boolean("Guarantees granted")
