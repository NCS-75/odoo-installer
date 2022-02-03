# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Readonly",
    "description": """
        Add security group displaying CRM leads in readonly mode""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm"],
    "data": ["security/crm_readonly_security.xml","security/ir.model.access.csv"],
    "demo": [],
}
