# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Quotation Restrict",
    "summary": """
        Restrict security group "Sales/Own Documents Only" to edit Sale Orders only in 'draft' or 'sent' state.""",
    "description": """
        /!\\ WARNING : this module change the domain of native ir.rule "Personal Orders"
        and "Personal Order Lines".
        When uninstalling this module the domains must be set back manually to their native value :
        `['|',('user_id','=',user.id),('user_id','=',False)]`
        """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["sale"],
    "data": ["security/sale_quotation_security.xml"],
    "demo": [],
}
