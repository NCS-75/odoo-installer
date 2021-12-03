# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "L10n Fr Partner Company",
    "summary": """
        Move SIRET fields in new res.partner's Company page from module partner_company
    """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["l10n_fr_siret", "partner_company"],
    "data": ["views/res_partner.xml"],
    "demo": [],
}
