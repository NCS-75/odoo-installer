from odoo.addons.base_rest import restapi
from odoo.addons.base_rest_datamodel.restapi import Datamodel
from odoo.addons.component.core import Component

# 'user' or 'api_key'
AUTH = "api_key"

M2O_UPD_PARAM = [
    # [model, param_field, odoo_field, match="name"]
    ["res.country", "country_code", "country_id", "code"],
    ["crm.stage", "stage_name", "stage_id"],
    ["crm.lost.reason", "lost_reason_name", "lost_reason"],
    ["crm.building", "building_name", "building_id"],
    ["res.users", "kam_id", "user_id", "partner_id"],
    ["crm.roof", "roof_name", "roof_id"],
    ["crm.roof.covering", "roof_covering_name", "roof_covering_id"],
]

M2M_UPD_PARAM = [
    # [model, param_field, odoo_field, match, (domain)]
    ["crm.use", "use_names", "use_ids", "name"],
    ["crm.heater", "heater_names", "heater_ids", "name"],
]


class leadService(Component):
    """
    CRM Lead API
    """

    _inherit = "base.crm.api.service"
    _name = "base.crm.api.lead"
    _usage = "lead"
    _collection = "crm.api.service"
    _description = "CRM Lead API"

    @restapi.method(
        [(["/"], "GET")],
        input_param=Datamodel("ds.lead.search.param"),
        output_param=Datamodel("ds.lead.info", is_list=True),
        auth=AUTH,
    )
    def search(self, lead_search_param):
        """
        List leads
        """
        res = []
        if lead_search_param.write_date_from:
            domain = [("write_date", ">", lead_search_param.write_date_from)]
        elif lead_search_param.manual_write_date_from:
            domain = [
                ("write_date", ">", lead_search_param.manual_write_date_from),
                ("write_uid", "!=", 1),
            ]
        else:
            domain = []
        for p in self.env["crm.lead"].search(domain, order="write_date DESC"):
            res.append(self._to_lead_info(p))
        return res

    @restapi.method(
        [(["/<int:id>"], "GET")],
        output_param=Datamodel("ds.lead.info"),
        auth=AUTH,
    )
    def get(self, _id):
        """
        Get lead information
        """
        lead = self.env["crm.lead"].browse(_id)
        return self._to_lead_info(lead)

    @restapi.method(
        [(["/"], "POST")],
        input_param=Datamodel("ds.lead.create.param"),
        output_param=Datamodel("ds.lead.info"),
        auth=AUTH,
    )
    def create(self, lead_create_param):
        """
        Create a new lead
        """
        lead = self.env["crm.lead"].with_context(connector_no_export=True).create(
            self._prepare_lead_write(lead_create_param)
        )
        return self._to_lead_info(lead)

    @restapi.method(
        [(["/<int:id>"], "POST")],
        input_param=Datamodel("ds.lead.update.param"),
        output_param=Datamodel("ds.lead.info"),
        auth=AUTH,
    )
    def update(self, _id, lead_update_param):
        """
        Update lead informations
        """
        lead = self.env["crm.lead"].with_context(connector_no_export=True).browse(_id)
        write_dict = self._prepare_lead_write(lead_update_param)
        if write_dict.get("lost_reason"):
            lead.action_archive()
        else:
            lead.action_unarchive()

        lead.write(write_dict)
        return self._to_lead_info(lead)

    @restapi.method(
        [(["/<int:id>/archive"], "POST")],
        auth=AUTH,
    )
    def archive(self, _id):
        """
        Archive the given lead.
        :param _id:
        :return:
        """
        self.env["crm.lead"].browse(_id).unlink()
        return True

    def _prepare_lead_write(self, lead_update_param):
        param = lead_update_param
        write_dict = {}
        for key in [
            "name",
            "partner_id",
            "street",
            "street2",
            "city",
            # Custom DualSun
            "myds_id",
            "myds_url",
            "white_label",
            "phase",
            "pvt_nb",
            "pv_nb",
            "project_manager_id",
            "distributor_id",
            "installer_seller_id",
            "installer_fitter_id",
            "referrent_id",
        ]:
            if getattr(param, key) is not None:
                write_dict[key] = getattr(param, key)
        if param.zip_code:
            write_dict["zip"] = param.zip_code

        if param.lost_reason_name is not None:
            write_dict["active"] = not bool(param.lost_reason_name)

        for m2o_args in M2O_UPD_PARAM:
            self._match_m2o(write_dict, param, *m2o_args)

        for m2m_args in M2M_UPD_PARAM:
            self._match_m2m(write_dict, param, *m2m_args)

        return write_dict

    def _to_lead_info(self, lead):
        if not lead:
            return None
        lead = lead.with_context(lang="en_US")
        LeadInfo = self.env.datamodels["ds.lead.info"]
        lead_info = LeadInfo(partial=True)
        lead_info.id = lead.id
        lead_info.write_date = lead.write_date
        lead_info.write_uid = lead.write_uid
        lead_info.name = lead.name
        lead_info.active = lead.active

        lead_info.lost_reason_name = lead.lost_reason.name
        lead_info.stage_name = lead.stage_id.name
        lead_info.partner_id = lead.partner_id.id
        lead_info.street = lead.street or ""
        lead_info.street2 = lead.street2 or ""
        lead_info.zip_code = lead.zip or ""
        lead_info.city = lead.city or ""
        lead_info.country_code = lead.country_id.code
        lead_info.kam_id = lead.user_id.partner_id.id

        # Custom DualSun
        lead_info.myds_id = lead.myds_id
        lead_info.white_label = lead.white_label
        lead_info.phase = lead.phase
        lead_info.pvt_nb = lead.pvt_nb
        lead_info.pv_nb = lead.pv_nb
        lead_info.use_names = lead.use_ids.mapped("name")
        lead_info.heater_names = lead.heater_ids.mapped("name")
        lead_info.building_name = lead.building_id.name
        lead_info.project_manager_id = lead.project_manager_id.id
        lead_info.distributor_id = lead.distributor_id.id
        lead_info.installer_seller_id = lead.installer_seller_id.id
        lead_info.installer_fitter_id = lead.installer_fitter_id.id
        lead_info.referrent_id = lead.referrent_id.id
        lead_info.kam_id = lead.user_id.partner_id.id
        lead_info.roof_name = lead.roof_id.name
        lead_info.roof_covering_name = lead.roof_covering_id.name

        return lead_info
