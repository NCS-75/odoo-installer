# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging
from odoo import SUPERUSER_ID, _, api, tools

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    _logger.info(_("Loading custom A4 paper format and Company report parameters..."))

    env.ref("base.paperformat_euro").write({"margin_top": 5})
    env.ref("base.main_company").write(
        {"external_report_layout_id": env.ref("report_base_installer.external_layout_boxed").id}
    )
