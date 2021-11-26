# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pyexcel
import logging
from odoo import _, modules
from pprint import pprint

_logger = logging.getLogger(__name__)


def insert_sql_datas_from_vals_list(cr, module, model, vals_list):
    """Create new lines directly in SQL model's table in order to control lines IDs
    (and other columns values) in database.

    vals_list is a list of dictionaries defining the datas to insert in the database
    """
    sql = ""
    table_name = model.replace(".", "_")
    if not all(v.get("id") for v in vals_list):
        m = f"{module}'s hard datas do not provide an ID for all the datas'"
        _logger.critical(m)
        raise IOError(m)
    if not all(v.get("xmlid") for v in vals_list):
        m = f"{module}'s hard datas do not provide an XML ID for all the datas'"
        _logger.critical(m)
        raise IOError(m)

    for vals in vals_list:
        xmlid = vals.pop("xmlid")
        columns = []
        datas = []
        for column, data in vals.items():
            columns.append(column)
            if data == "True":
                data = True
            elif data in ["False", ""]:
                data = False
            datas.append(str(data) if type(data) != str else  "'" + data + "'")

        sql += f"""
        INSERT INTO {table_name} ({", ".join(columns)})
            VALUES ({", ".join(datas)});

        INSERT INTO ir_model_data (name, module, model, noupdate, res_id)
            VALUES ('{xmlid}', '{module}', '{model}', True, {vals["id"]});

        SELECT
            SETVAL('{table_name}_id_seq', 1);
        """

    _logger.info(_("Creating SQL datas for %s...") % module)
    cr.execute(sql)


def insert_sql_datas(cr, module, model, data_file):
    file = modules.get_resource_path(module, "data", data_file)
    if not file:
        m = f"File not found: '{data_file}' in data folder (module '{module}')."
        _logger.critical(m)
        raise IOError(m)

    vals_list = pyexcel.get_records(file_name=str(file))
    insert_sql_datas_from_vals_list(cr, module, model, vals_list)
