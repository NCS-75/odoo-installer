# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Api",
    "summary": """
        Exposes Partners and Opportunities as REST API""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "depends": [
        "crm",
        # https://github.com/OCA/rest-framework
        "datamodel",
        "base_rest",
        "base_rest_datamodel",
        # https://github.com/OCA/server-auth
        "auth_api_key",
        # https://github.com/OCA/queue
        "queue_job",
        # https://github.com/OCA/connector
        "component_event",
        # https://github.com/OCA/partner-contact
        "partner_firstname",
        # https://github.com/akretion/odoo-installer
        "crm_installer",
        "partner_installer",
        "partner_relation",
        "partner_role",
        "partner_stage",
    ],
    "data": ["data/rest_menu.xml"],
    "demo": ["demo/auth_api_key_demo.xml"],
}
