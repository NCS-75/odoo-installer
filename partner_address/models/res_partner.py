# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Split child_ids in 2 without changing child_ids itself
    contact_ids = fields.One2many(
        "res.partner",
        "parent_id",
        "Contacts",
        domain=[("active", "=", True), ("type", "=", "contact")],
    )
    address_ids = fields.One2many(
        "res.partner",
        "parent_id",
        string="Addresses",
        domain=[("active", "=", True), ("type", "!=", "contact")],
    )
    # New address_type field related to original 'type' but without the 'contact' option
    address_type = fields.Selection(
        string="Address Type",
        selection=[
                ('delivery', 'Delivery Address'),
                ('invoice', 'Invoice Address'),
                ('private', 'Private Address'),
        ],
    )
    type = fields.Selection(
        string="Contact Type", # Rename 'type' to avoid confusion with new address_type
        compute="_compute_contact_type",
        inverse="_inverse_contact_type",
        readonly=False,
        store=True,
    )

    @api.depends("address_type")
    def _compute_contact_type(self):
        for rec in self:
            rec.type = rec.address_type or "contact"

    def _inverse_contact_type(self):
        addr_type_options = [s[0] for s in self._fields["address_type"].selection]
        for rec in self:
            rec.address_type = rec.type in addr_type_options and rec.type or False
