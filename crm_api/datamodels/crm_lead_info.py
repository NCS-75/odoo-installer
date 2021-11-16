from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
# from odoo.addons.datamodel.fields import NestedModel


class LeadInfo(Datamodel):
    _inherit = "ds.lead.create.param"
    _name = "ds.lead.info"

    id = fields.Integer(required=True)
    active = fields.Boolean()
    write_date = fields.Date()
    write_uid = fields.Integer()
