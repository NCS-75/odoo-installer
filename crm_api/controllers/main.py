# Copyright 2021 Akretion
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main


class CrmApiController(main.RestController):
    _root_path = "/crm-api/"
    _collection_name = "crm.api.service"
    _default_auth = "api_key"
