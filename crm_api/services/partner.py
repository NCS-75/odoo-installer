from odoo.addons.base_rest import restapi
from odoo.addons.base_rest_datamodel.restapi import Datamodel
from odoo.addons.component.core import Component

# 'api_key' or 'user'
AUTH = "api_key"

M2O_UPD_PARAM = [
    # [model, param_field, odoo_field, match]
    ["res.country", "country_code", "country_id", "code"],
    ["res.users", "kam_id", "user_id", "partner_id"],
    ["res.partner.role", "role_name", "role_id", "name"],
    ["res.partner.relation", "relation_code", "relation_id", "code"],
    ["res.partner.stage", "stage_name", "stage_id", "name"],
]

DISTRIB_DOMAIN = [("is_distributor", "=", True), ("is_company", "=", True)]
M2M_UPD_PARAM = [
    # [model, param_field, odoo_field, match, (domain)]
    ["res.partner", "distributor_ids", "distributor_ids", "id", DISTRIB_DOMAIN],
    ["res.partner.range", "range_names", "range_ids", "name"],
    ["crm.use", "use_names", "use_ids", "name"],
    ["crm.heater", "heater_names", "heater_ids", "name"],
]


class PartnerService(Component):
    """
    Partner API
    """

    _inherit = "base.crm.api.service"
    _name = "base.crm.api.partner"
    _usage = "partner"
    _collection = "crm.api.service"
    _description = "Partner API"

    @restapi.method(
        [(["/"], "GET")],
        input_param=Datamodel("ds.partner.search.param"),
        output_param=Datamodel("ds.partner.info", is_list=True),
        auth=AUTH,
    )
    def search(self, partner_search_param):
        """
        List partners
        """
        res = []
        if partner_search_param.write_date_from:
            domain = [("write_date", ">", partner_search_param.write_date_from)]
        elif partner_search_param.manual_write_date_from:
            domain = [
                ("write_date", ">", partner_search_param.manual_write_date_from),
                ("write_uid", "!=", 1),
            ]
        else:
            domain = []
        for p in self.env["res.partner"].search(domain, order="write_date DESC"):
            res.append(self._to_partner_info(p))
        return res

    @restapi.method(
        [(["/<int:id>"], "GET")],
        output_param=Datamodel("ds.partner.info"),
        auth=AUTH,
    )
    def get(self, _id):
        """
        Get partner information
        """
        partner = self.env["res.partner"].browse(_id)
        return self._to_partner_info(partner)

    @restapi.method(
        [(["/"], "POST")],
        input_param=Datamodel("ds.partner.create.param"),
        output_param=Datamodel("ds.partner.info"),
        auth=AUTH,
    )
    def create(self, partner_create_param):
        """
        Create a new partner
        """
        partner = self.env["res.partner"].with_context(connector_no_export=True).create(
            self._prepare_partner_write(partner_create_param)
        )
        return self._to_partner_info(partner)

    @restapi.method(
        [(["/<int:id>"], "POST")],
        input_param=Datamodel("ds.partner.update.param"),
        output_param=Datamodel("ds.partner.info"),
        auth=AUTH,
    )
    def update(self, _id, partner_update_param):
        """
        Update partner information
        """
        partner = self.env["res.partner"].with_context(connector_no_export=True).browse(_id)
        partner.write(self._prepare_partner_write(partner_update_param))
        return self._to_partner_info(partner)

    @restapi.method(
        [(["/<int:id>/archive"], "POST")],
        auth=AUTH,
    )
    def archive(self, _id):
        """
        Archive the given partner.
        :param _id:
        :return:
        """
        self.env["res.partner"].browse(_id).unlink()
        return True

    def _prepare_partner_write(self, partner_update_param):
        param = partner_update_param
        write_dict = {}
        for key in [
            "firstname",
            "lastname",
            "email",
            "street",
            "street2",
            "city",
            "phone",
            "mobile",
            "is_company",
            "comment",
            "siren",
            "nic",
            "lang",
            "website",
            # DS custom fields
            "myds_id",
            "myds_url",
            "is_seller",
            "is_fitter",
            "accept_fitting_for_x",
            "action_radius",
            "annual_volume",
        ]:
            if getattr(param, key) is not None:
                write_dict[key] = getattr(param, key)
        if param.zip_code is not None:
            write_dict["zip"] = param.zip_code
        if param.parent_id is not None:
            # Interpret "zero" as False (in order to erase 'parent_id')
            write_dict["parent_id"] = param.parent_id or False

        for m2o_args in M2O_UPD_PARAM:
            self._match_m2o(write_dict, param, *m2o_args)

        for m2m_args in M2M_UPD_PARAM:
            self._match_m2m(write_dict, param, *m2m_args)

        # {'is_company': True} not enough on company creation (but enough for update)
        if write_dict.get("is_company"):
            write_dict["company_type"] = "company"

        return write_dict

    def _to_partner_info(self, partner):
        if not partner:
            return None
        partner = partner.with_context(lang="en_US")
        PartnerInfo = self.env.datamodels["ds.partner.info"]
        partner_info = PartnerInfo(partial=True)
        partner_info.id = partner.id
        partner_info.write_date = partner.write_date
        partner_info.write_uid = partner.write_uid
        partner_info.firstname = partner.firstname or ""
        partner_info.lastname = partner.lastname or ""
        partner_info.email = partner.email or ""
        partner_info.street = partner.street or ""
        partner_info.street2 = partner.street2 or ""
        partner_info.zip_code = partner.zip or ""
        partner_info.city = partner.city or ""
        partner_info.phone = partner.phone or ""
        partner_info.mobile = partner.mobile or ""
        partner_info.country_code = partner.country_id.code or ""
        partner_info.parent_id = partner.parent_id.id
        partner_info.is_company = partner.is_company
        partner_info.comment = partner.comment or ""
        partner_info.siren = partner.siren or ""
        partner_info.nic = partner.nic or ""
        partner_info.lang = partner.lang
        partner_info.kam_id = partner.user_id.partner_id.id

        # custom DualSun:
        partner_info.myds_id = partner.myds_id
        partner_info.myds_url = partner.myds_url
        partner_info.role_name = partner.role_id.name
        partner_info.relation_code = partner.relation_id.code
        partner_info.stage_name = partner.stage_id.name
        partner_info.is_seller = partner.is_seller
        partner_info.is_fitter = partner.is_fitter
        partner_info.is_pv = partner.is_pv
        partner_info.is_pvt = partner.is_pvt
        partner_info.accept_fitting_for_x = partner.accept_fitting_for_x
        partner_info.action_radius = partner.action_radius or 0
        partner_info.annual_volume = partner.annual_volume or 0
        partner_info.distributor_ids = partner.distributor_ids.ids
        partner_info.range_names = partner.range_ids.mapped("name")
        partner_info.use_names = partner.use_ids.mapped("name")
        partner_info.heater_names = partner.heater_ids.mapped("name")

        return partner_info
