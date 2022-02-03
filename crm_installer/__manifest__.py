# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Installer",
    "summary": """
        Specific fields and stages for a perfect CRM for DualSun's installers""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm", "partner_role", "crm_aftersale", "crm_stage_probability"],
    "data": [
        # Security
        "security/ir.model.access.csv",
        "security/crm_stage_security.xml",
        # Views
        "views/crm_building_views.xml",
        "views/crm_heater_views.xml",
        "views/crm_lead_views.xml",
        "views/crm_stage_views.xml",
        "views/crm_roof_views.xml",
        "views/crm_use_views.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
}
