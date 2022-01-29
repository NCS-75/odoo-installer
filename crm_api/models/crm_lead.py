# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from os import environ
import requests

from odoo import _, api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    myds_id = fields.Integer("MyDS ID", index=True, readonly=True)
    myds_url = fields.Char(
        "MyDS",
        readonly=True,
        help="Related object on MyDualSun.\nNot editable because it is made to be "
        "modified through the MyDS-Odoo API exclusively.",
    )

    def _notify_lead_update(self):
        for rec in self:
            r = requests.get("%s/odoo/update_entity/%s?entity_type=%s" % (
                environ.get("MYDS_API"), rec.id, rec._name
            ))
            print(r)