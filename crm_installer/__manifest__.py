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
    "depends": ["crm", "partner_role", "crm_aftersale"],
    "data": [
        # Data
        "data/crm_building_data.xml",
        "data/crm_heater_data.xml",
        "data/crm_lost_reason_data.xml",
        "data/crm_roof_covering_data.xml",
        "data/crm_roof_data.xml",
        "data/crm_stage_data.xml",
        "data/crm_use_data.xml",
        "data/partner_category_data.xml",
        # Security
        "security/ir.model.access.csv",
        # Views
        "views/crm_building_views.xml",
        "views/crm_heater_views.xml",
        "views/crm_lead_views.xml",
        "views/crm_stage_views.xml",
        "views/crm_roof_views.xml",
        "views/crm_use_views.xml",
    ],
    "demo": [],
    "pre_init_hook": "pre_init_hook",
    "post_init_hook": "post_init_hook",
}
