# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CrmStage(models.Model):
    _inherit = "crm.stage"

    on_change = fields.Boolean(default=True)
    # Usefuly display active fields in order to hide MyDS stages if not used
    active = fields.Boolean("Active", default=True)

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

    def write(self, vals):
        """Avoid archive stages with leads"""
        if vals.get("active") is False:
            for rec in self:
                lead_ids = self.env["crm.lead"].search(
                    [("stage_id", "=", rec.id), ("active", "in", [True, False])]
                )
                if lead_ids:
                    list = "\n - ".join(lead_ids.mapped("name"))
                    raise ValidationError(
                        _(
                            "It is not possible to archive the stage '%s' as it still "
                            "contains the following leads :\n - %s"
                        )
                        % (rec.name, list)
                    )
        return super().write(vals)
