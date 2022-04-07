# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import requests

from odoo import fields, models

logger = logging.getLogger(__name__)


class CrmLead(models.Model):
    _inherit = "crm.lead"

    myds_id = fields.Integer("MyDS ID", index=True, readonly=True)
    myds_url = fields.Char(
        "MyDS",
        readonly=True,
        help="Related object on MyDualSun.\nNot editable because it is made to be "
        "modified through the MyDS-Odoo API exclusively.",
    )

    def notify_myds_update(self):
        myds_server = self.env['ir.config_parameter'].sudo().get_param('dualsun.myds.url')
        if myds_server:
            odoo_server = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            for rec in self:
                r = requests.get(
                    "%s/odoo/update_entity/%s" % (myds_server, rec.id,),
                    params={'entity_type': rec._name, 'odoo_server': odoo_server}
                )
                logger.info("MyDS notification %s. Response: %s" % (
                    r.url,
                    r,
                ))
