# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Address",
    "description": """
        - Split partner's child_ids between contact and addresses
        - Add coworkers to individuals
        - New field 'Address type'
    """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "demo": [],
}
