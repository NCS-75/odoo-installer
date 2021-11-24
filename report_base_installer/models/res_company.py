# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    report_logo = fields.Binary(
        string="Report Logo", help="Logo used on report's header"
    )
