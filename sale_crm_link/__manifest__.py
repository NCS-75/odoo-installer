# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Crm Link",
    "description": """
        Smartbutton to go from Sale Order to related Lead""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["sale_crm"],
    "data": [
        "views/sale_order.xml",
        "views/crm_lead.xml",
    ],
    "demo": [],
}
