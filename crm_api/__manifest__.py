# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Api",
    "description": """
        Exposes Partners and Opportunities as REST API""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "depends": [
        "crm",
        "base_rest",
        "base_rest_datamodel",
        "auth_api_key",
        # https://github.com/akretion/odoo-installer
        "crm_installer",
        "partner_role",
        "partner_relation",
        "partner_installer",
        # TODO: remove
        "incwo_url",
    ],
    "data": [],
    "demo": [
        "demo/auth_api_key_demo.xml",
    ],
}
