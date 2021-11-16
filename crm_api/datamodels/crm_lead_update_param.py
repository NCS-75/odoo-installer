from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel
# from odoo.addons.datamodel.fields import NestedModel


class LeadUpdateParam(Datamodel):
    _name = "ds.lead.update.param"

    name = fields.String()
    stage_name = fields.String()
    lost_reason_name = fields.String()
    partner_id = fields.Integer()
    street = fields.String()
    street2 = fields.String()
    zip_code = fields.String()
    city = fields.String()
    country_code = fields.String()

    # Custom DualSun
    incwo_id = fields.Integer()
    myds_id = fields.Integer()
    myds_url = fields.String()
    white_label = fields.String()
    phase = fields.String()
    pvt_nb = fields.Integer()
    pv_nb = fields.Integer()
    use_names = fields.List(fields.String())
    heater_names = fields.List(fields.String())
    building_name = fields.String()
    project_manager_id = fields.Integer()
    distributor_id = fields.Integer()
    installer_seller_id = fields.Integer()
    installer_fitter_id = fields.Integer()
    referrent_id = fields.Integer()
    kam_id = fields.Integer()
    roof_name = fields.String()
    roof_covering_name = fields.String()
