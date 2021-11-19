# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _order = "relation_code desc, name"

    # Rename 'Individual' into 'Contact'
    company_type = fields.Selection(selection_add=[("person", "Contact")])

    stage_id = fields.Many2one(
        string="Installer Stage",
        comodel_name="res.partner.stage",
        ondelete="set null",
        group_expand="_read_group_stage_ids",
        store=True,
        index=True,
        tracking=True,
        readonly=False,
        copy=False,
        help="Installer Qualification Stage",
    )

    is_pv = fields.Boolean("PV")
    is_pvt = fields.Boolean("PVT")
    use_ids = fields.Many2many(
        string="Uses", comodel_name="crm.use", help="Uses covered by the installer"
    )
    heater_ids = fields.Many2many(
        string="Heaters",
        comodel_name="crm.heater",
        help="Auxiliary Heaters proposed by the installer",
    )
    range_ids = fields.Many2many(
        string="Installation Ranges",
        comodel_name="res.partner.range",
        help="The installation sizes accepted by the installer",
    )
    action_radius = fields.Integer("Action Radius")
    is_seller = fields.Boolean("Seller")
    is_fitter = fields.Boolean("Fitter")
    accept_fitting_for_x = fields.Boolean("Accept fitting PVT for X")

    distributor_ids = fields.Many2many(
        string="Distributors",
        comodel_name="res.partner",
        domain=[("is_distributor", "=", True), ("is_company", "=", True)],
        relation="res_partner_distributors",
        column1="res_partner_installer",
        column2="res_partner_distributor",
        help="Potential distributors for this installer.",
    )
