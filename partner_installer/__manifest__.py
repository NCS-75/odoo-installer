# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Installer",
    "description": """
        Minimum installer's fields on res.partner for connection with MyDS,
        with datas but no views.""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm_installer"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
}
