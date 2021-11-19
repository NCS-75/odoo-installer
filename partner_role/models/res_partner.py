# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


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


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_installer = fields.Boolean(related="role_id.is_installer", store=True)
    is_distributor = fields.Boolean(related="role_id.is_distributor", store=True)
    is_project_manager = fields.Boolean(
        related="role_id.is_project_manager", store=True
    )

    role_id = fields.Many2one(
        string="Role",
        comodel_name="res.partner.role",
        compute="_compute_role",
        store=True,
        readonly=False,  # Useful only for importation. Field not displayed in UI
        help="Partner's Role related to MyDualSun Role field",
    )

    @api.depends("category_id")
    def _compute_role(self):
        for partner_id in self:
            partner_id.role_id  = partner_id.category_id.role_id[-1:]

    def write(self, vals):
        """Change category_id depending on role_id"""
        # 'role_id' can be modified only by MyDS API (=through method write)
        if vals.get("role_id") is not None:
            if vals.get("category_id") and "tracking_disable" not in self.env.context:
                # Hack `"tracking_disable" not in self.env.context` used to
                # avoid raise when loading from anthem song
                raise ValidationError(
                    _(
                        "It is not possible to modify both partner's Categories and "
                        "Role.\nThe field 'Role' is designed to be edited only by API "
                        "while not touching to 'Categories'."
                    )
                )
            categ_vals = []
            new_role_id = self.env["res.partner.role"].browse([vals["role_id"]])
            # If vals.get("role_id") is False, we want to remove the
            # actual_categ_role_id but we don't want to add a categ_role_id.
            if new_role_id.id:
                categ_role_id = self.env["res.partner.category"].search(
                    [("role_id", "=", new_role_id.id)]
                )
                categ_vals += [(4, categ_role_id.id)]

            # We remove the actual category related to a role and add the category
            # related to the new role
            actual_categ_role_id = self.category_id.filtered(lambda c: c.role_id)
            if actual_categ_role_id and actual_categ_role_id.role_id != new_role_id:
                categ_vals += [(3, actual_categ_role_id.id)]

            vals["category_id"] = categ_vals
        return super().write(vals)
