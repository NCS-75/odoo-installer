# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
from os import environ
import requests

from odoo import _, api, fields, models

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

    def _notify_myds_update(self):
        if environ.get("MYDS_API"):
            instance_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            for rec in self:
                r = requests.get(
                    "%s/odoo/update_entity/%s?entity_type=%s&instance_url=%s" % (
                    environ.get("MYDS_API"), rec.id, rec._name, instance_url,
                ))
                logger.info("notified %s about %s id %s update. Response code: %s" % (
                    environ.get("MYDS_API"),
                    rec._name,
                    rec.id,
                    r,
                ))
