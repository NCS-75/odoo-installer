# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import requests

from odoo import api, fields, models

logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = "crm.lead"

    myds_id = fields.Integer("MyDS ID", index=True, readonly=True)
    myds_url = fields.Char(
        "MyDS",
        compute="_compute_myds_url",
        help="Related object on MyDualSun.\nNot editable because it is made to be "
        "modified through the MyDS-Odoo API exclusively.",
    )
    is_myds_visible = fields.Boolean(
        string="Is MyDS visible?", compute="_compute_is_myds_visible"
    )

    @api.depends("myds_id")
    def _compute_myds_url(self):
        myds_server = (
            self.env["ir.config_parameter"].sudo().get_param("dualsun.myds.url")
        )
        for rec in self:
            if not myds_server or not rec.myds_id:
                rec.myds_url = False
            else:
                rec.myds_url = myds_server + "/projects/" + str(rec.myds_id)

    @api.depends(
        "street",
        "city",
        "partner_id",
        "installer_seller_id",
        "installer_fitter_id",
        "pvt_nb",
        "pv_nb",
        "building_id",
    )
    def _compute_is_myds_visible(self):
        for rec in self:
            rec.is_myds_visible = (
                (rec.street or rec.city)
                and rec.partner_id
                and (rec.installer_fitter_id or rec.installer_seller_id)
                and (rec.pv_nb or rec.pvt_nb)
                and rec.building_id
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
