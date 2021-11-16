from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class PartnerSearchParam(Datamodel):
    _name = "ds.partner.search.param"

    write_date_from = fields.Date()
    manual_write_date_from = fields.Date()
