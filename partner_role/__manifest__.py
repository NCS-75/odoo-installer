# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Partner Role",
    "description": """
        Add a "Role" field on Partners and Partners Categories, allowing to relate to
        the Partner one specific info from one specific Category.

        We separate this model's creation from `partner_role` because we need the model
        to exist before loading "partner_role/data/partner_extra_data.xml"
        in pre_init_hook.

        """,
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base"],
    "data": [
        "data/partner_role_data.xml",
        "security/ir.model.access.csv",
        "views/res_partner_category_views.xml",
    ],
    "demo": [],
}
