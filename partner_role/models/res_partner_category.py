# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartnerCategory(models.Model):
    _inherit = "res.partner.category"

    name = fields.Char(translate=True)
    role_id = fields.Many2one(
        string="Partner Role",
        comodel_name="res.partner.role",
        readonly=True,
        help="Role (in MyDualSun) applied to the Partner if this Category is selected.",
    )

    def unlink(self):
        for categ in self:
            if categ.role_id:
                raise ValidationError(
                    _(
                        "Impossible to delete the category '%s' as it is linked to a "
                        "specific 'Role' used in the API with MyDualSun" % categ.name
                    )
                )


class ResPartnerRole(models.Model):
    _name = "res.partner.role"
    _description = "Installers Role in MyDualSun"
    _rec_name = "name"
    _order = "id"

    name = fields.Char(translate=True)
    is_installer = fields.Boolean()
    is_distributor = fields.Boolean()
    is_project_manager = fields.Boolean()

    # TODO: add constrains to secure each boolean is only True for one role only.
