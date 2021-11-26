# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo.addons.sql_tools.sql_tools import insert_sql_datas

def post_init_hook(cr, registry):
    insert_sql_datas(
        cr, "partner_stage", "res.partner.stage", "res_partner_stage_data.csv"
    )
