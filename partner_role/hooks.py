# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import pathlib
from odoo.addons.sql_tools.sql_tools import insert_sql_datas

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
MODULE = CURRENT_DIR.stem


def post_init_hook(cr, registry):
    insert_sql_datas(cr, MODULE, "res.partner.role", "res_partner_role_data.csv")
    insert_sql_datas(
        cr, MODULE, "res.partner.category", "res_partner_category_data.csv"
    )
