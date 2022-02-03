# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Aftersale Restrict",
    "summary": """
        Restrict security group "Sales/Own Documents Only" to edit Leads only if not in After-Sale stage.""",
    "description": """
        /!\\ WARNING : this module change the domain of native ir.rule "Personal Leads"
        When uninstalling this module the domain must be set back manually to native value :
        `['|',('user_id','=',user.id),('user_id','=',False)]`
        """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm_aftersale"],
    "data": ["security/crm_aftersale_security.xml"],
    "demo": [],
}
