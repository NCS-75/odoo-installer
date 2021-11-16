from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
# from odoo.addons.datamodel.fields import NestedModel


class PartnerInfo(Datamodel):
    _inherit = "ds.partner.create.param"
    _name = "ds.partner.info"

    id = fields.Integer(required=True)
    write_date = fields.Date()
    write_uid = fields.Integer()
