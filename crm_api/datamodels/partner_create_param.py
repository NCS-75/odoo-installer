from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
# from odoo.addons.datamodel.fields import NestedModel


class PartnerCreateParam(Datamodel):
    _inherit = "ds.partner.update.param"
    _name = "ds.partner.create.param"

    lastname = fields.String(required=True)
