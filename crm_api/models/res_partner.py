# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import requests

from odoo import api, fields, models

logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    myds_id = fields.Integer("MyDS ID", index=True, readonly=True)
    myds_url = fields.Char(
        "MyDS",
        readonly=True,
        help="Related object on MyDualSun.\nNot editable because it is made to be "
        "modified through the MyDS-Odoo API exclusively.",
    )
    is_myds_visible = fields.Boolean(
        string="Is MyDS visible?", compute="_compute_is_myds_visible"
    )

    @api.depends("email", "user_ids", "role_id")
    def _compute_is_myds_visible(self):
        for rec in self:
            rec.is_myds_visible = (rec.email or rec.is_company) and (
                rec.user_ids or rec.role_id
            )

    def notify_myds_update(self):
        myds_ws_url = (
            self.env["ir.config_parameter"].sudo().get_param("dualsun.myds.ws.url")
        )
        if myds_ws_url:
            odoo_server = (
                self.env["ir.config_parameter"].sudo().get_param("web.base.url")
            )
            for rec in self:
                r = requests.get(
                    "%s/odoo/update_entity/%s" % (myds_ws_url, rec.id),
                    params={"entity_type": rec._name, "odoo_server": odoo_server},
                )
                logger.info("MyDS notification %s. Response: %s" % (r.url, r))
