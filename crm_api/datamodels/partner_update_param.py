from marshmallow import fields

from odoo.addons.datamodel.core import Datamodel


class PartnerUpdateParam(Datamodel):
    _name = "ds.partner.update.param"

    firstname = fields.String()
    lastname = fields.String()
    email = fields.String()
    street = fields.String()
    street2 = fields.String()
    zip_code = fields.String()
    city = fields.String()
    phone = fields.String()
    mobile = fields.String()
    country_code = fields.String()
    comment = fields.String()
    siren = fields.String()
    nic = fields.String()
    lang = fields.String()
    website = fields.String()

    is_company = fields.Boolean()
    parent_id = fields.Integer()
    # To be filled by user's partner_id and then translated to real user_id
    kam_id = fields.Integer()

    # custom DualSun:
    myds_id = fields.Integer()
    myds_url = fields.String()
    role_name = fields.String()
    relation_code = fields.String()
    stage_name = fields.String()
    is_seller = fields.Boolean()
    is_fitter = fields.Boolean()
    is_pv = fields.Boolean()
    is_pvt = fields.Boolean()
    accept_fitting_for_x = fields.Boolean()
    action_radius = fields.Integer()
    annual_volume = fields.Float()

    distributor_ids = fields.List(fields.Integer())
    range_names = fields.List(fields.String())
    use_names = fields.List(fields.String())
    heater_names = fields.List(fields.String())
