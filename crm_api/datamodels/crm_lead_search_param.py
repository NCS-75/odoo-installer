from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class LeadSearchParam(Datamodel):
    _name = "ds.lead.search.param"

    write_date_from = fields.Date()
    manual_write_date_from = fields.Date()
