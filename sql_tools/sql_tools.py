# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import pyexcel
import logging
from odoo import _, modules
from pprint import pprint

_logger = logging.getLogger(__name__)


def _get_vals_from_data(data):
    columns = []
    vals = []
    for column, val in data.items():
        columns.append(column)
        if val == "True":
            val = True
        elif val in ["False", ""]:
            val = False
        vals.append(str(val) if type(val) != str else "'" + val + "'")

    return columns, vals


def insert_sql_vals_from_data_list(cr, model, data_list):
    """Create new lines directly in SQL model's table in order to control lines IDs
    (and other columns values) in database.

    data_list is a list of dictionaries defining the data to insert in the database
    """
    sql = ""
    table_name = model.replace(".", "_")
    if not all(d.get("id") for d in data_list):
        m = f"{model}'s hard data do not provide an ID for all the datas'"
        _logger.critical(m)
        raise IOError(m)
    if not all(d.get("xmlid") for d in data_list):
        m = f"{model}'s hard data do not provide an XML ID for all the datas'"
        _logger.critical(m)
        raise IOError(m)

    for data in data_list:
        xmlid = data.pop("xmlid")
        columns, vals = _get_vals_from_data(data)

        sql += f"""
        INSERT INTO {table_name} ({", ".join(columns)})
            VALUES ({", ".join(vals)});

        INSERT INTO ir_model_data (name, module, model, noupdate, res_id)
            VALUES ('{xmlid}', '__installer__', '{model}', True, {data["id"]});

        SELECT
            SETVAL('{table_name}_id_seq', (SELECT MAX(id) FROM {table_name}));
        """

    _logger.info(_("Creating SQL data for %s...") % model)
    cr.execute(sql)


def _get_data_file(module, data_file):
    file = modules.get_resource_path(module, "data", data_file)
    if not file:
        m = f"File not found: '{data_file}' not in 'data' folder (module '{module}')."
        _logger.critical(m)
        raise IOError(m)
    return file


def insert_sql_datas(cr, module, model, data_file):
    file = _get_data_file(module, data_file)
    data_list = pyexcel.get_records(file_name=str(file))
    insert_sql_vals_from_data_list(cr, model, data_list)


def update_sql_datas(cr, module, model, data_file):
    """Update existing data given in data_file"""
    file = _get_data_file(module, data_file)
    data_list = pyexcel.get_records(file_name=str(file))
    table_name = model.replace(".", "_")
    sql = ""

    for data in data_list:
        data.pop("xmlid")
        id = data.pop("id")
        sql += f"\nUPDATE {table_name} SET "
        columns, vals = _get_vals_from_data(data)
        sql += ", ".join([f"{col} = {val}" for col, val in zip(columns, vals)])
        sql += f" WHERE id = {id};"

    _logger.info(_("Updating SQL datas for %s...") % model)
    cr.execute(sql)


# TODO: add method to create ID if not existing else update SQL line
