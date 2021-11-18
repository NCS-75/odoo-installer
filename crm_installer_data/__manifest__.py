# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Crm Installer Data",
    "description": """
        Master datas for DualSun installers CRM""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["crm_installer", "partner_role"],
    "data": [
        "data/partner_category_data.xml",
        "data/crm_building_data.xml",
        "data/crm_heater_data.xml",
        "data/crm_lost_reason_data.xml",
        "data/crm_roof_covering_data.xml",
        "data/crm_roof_data.xml",
        "data/crm_stage_data.xml",
        "data/crm_use_data.xml",
    ],
    "demo": [],
}
