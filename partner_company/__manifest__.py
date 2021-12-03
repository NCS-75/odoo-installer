# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Share Capital",
    "summary": """
        - Add 'Share Capital' field in res.partner and res.company
        - New page for company specific res.partner's fields
        - New page for Coworkers if any
    """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base", "account"],
    "data": ["views/res_company.xml", "views/res_partner.xml"],
    "demo": [],
}
