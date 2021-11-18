# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Installer",
    "description": """
        Specific fields and stages for a perfect CRM for DualSun's installers""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm"],
    "data": [
        "data/crm_stage_data.xml",
        "views/crm_lead_views.xml",
        "views/crm_stage_views.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
}
