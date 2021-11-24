# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = "base.document.layout"

    logo = fields.Binary("Logo", related="report_logo", readonly=True)
    report_logo = fields.Binary(
        "Report Logo", related="company_id.report_logo", readonly=False
    )
    siret = fields.Char(related="company_id.siret", readonly=True)
    ape = fields.Char(related="company_id.ape", readonly=True)
