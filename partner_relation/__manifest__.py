# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Relation",
    "description": """
        We separate this model's creation from `dualsun_base` because we need the model
        to exist before loading "dualsun_base/data/partner_extra_data.xml"
        in pre_init_hook.

        """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base", "partner_role"],
    "data": ["data/res_partner_relation_data.xml", "security/ir.model.access.csv"],
    "demo": [],
}
