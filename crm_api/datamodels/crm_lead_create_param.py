from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
# from odoo.addons.datamodel.fields import NestedModel


class LeadCreateParam(Datamodel):
    _inherit = "ds.lead.update.param"
    _name = "ds.lead.create.param"

    name = fields.String(required=True)
