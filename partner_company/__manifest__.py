# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Share Capital",
    "description": """
        Add 'Share Capital' field in res.partner and res.company and
        gather all res.partner's company fields in a new page
    """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base"],
    "data": ["views/res_company.xml", "views/res_partner.xml"],
    "demo": [],
}
