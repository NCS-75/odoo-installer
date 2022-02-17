# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Partner Restrict",
    "summary": """
        Restrict security group "Internal Users" to CRUD on thei own res.partner records only.""",
    "description": """This module creates 2 new ir.rule defined like the rules used to restrict Salesmen on their own leads/orders.""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["sale"],
    "data": ["security/sale_partner_security.xml"],
    "demo": [],
}
