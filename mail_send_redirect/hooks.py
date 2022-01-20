# Copyright 2021 Akretion
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import logging
from odoo import SUPERUSER_ID, _, api, tools

_logger = logging.getLogger(__name__)

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env["ir.config_parameter"].set_param("mail.redirect", "mail.redirect@example.com")
