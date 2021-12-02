# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import pathlib

import logging
from odoo import SUPERUSER_ID, _, api, tools
from odoo.tools import convert_file, load_language
from odoo.addons.sql_tools.sql_tools import insert_sql_datas

_logger = logging.getLogger(__name__)

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
MODULE = CURRENT_DIR.stem
STAGE_CONVERT = {
    "New": MODULE + ".relation_established",
    "Qualified": MODULE + ".qualified_project",
    "Proposition": MODULE + ".proposition_made",
    "Won": MODULE + ".installation_started",
}

SQL_DATAS = [
    ("crm.building", "crm_building_data.csv"),
    ("crm.heater", "crm_heater_data.csv"),
    ("crm.lost.reason", "crm_lost_reason_data.csv"),
    ("crm.roof.covering", "crm_roof_covering_data.csv"),
    ("crm.roof", "crm_roof_data.csv"),
    ("crm.stage", "crm_stage_data.csv"),
    ("crm.use", "crm_use_data.csv"),
]


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    _logger.info(_("Loading %s SQL datas...") % MODULE)
    for model, file in SQL_DATAS:
        insert_sql_datas(cr, MODULE, model, file)
