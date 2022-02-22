# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    report_bottom_image = fields.Binary(
        string="Report Bottom Image", help="Image displayed at the end of Qweb Reports"
    )
