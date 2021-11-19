# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    is_with_pm = fields.Boolean(compute="_compute_is_with_pm")
    pvt_nb = fields.Integer("PVT number")
    pv_nb = fields.Integer("PV number")
    use_ids = fields.Many2many(
        string="Uses", comodel_name="crm.use", help="Uses selected for this lead"
    )
    heater_ids = fields.Many2many(
        string="Heaters",
        comodel_name="crm.heater",
        help="Auxiliary Heaters selected for this lead.",
    )
    building_id = fields.Many2one("crm.building", "Building")
    roof_id = fields.Many2one("crm.roof", "Roof")
    roof_covering_id = fields.Many2one("crm.roof.covering", "Roof covering")

    phase = fields.Selection(
        string="Phase",
        selection=[("aps", "APS"), ("apd", "APD"), ("pro", "PRO"), ("dce", "DCE")],
    )
    worksite_completed = fields.Boolean(
        related="stage_id.worksite_completed", store=True
    )
    guarantees_granted = fields.Boolean(
        related="stage_id.guarantees_granted", store=True
    )

    project_manager_id = fields.Many2one(
        string="Project Manager",
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
    )
    installer_seller_id = fields.Many2one(
        string="Installer (Seller)",
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
    )
    installer_fitter_id = fields.Many2one(
        string="Installer (Fitter)",
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
    )
    distributor_id = fields.Many2one(
        string="Distributor",
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
    )
    partner_ids = fields.Many2many(
        string="Partners",
        comodel_name="res.partner",
        relation="lead_related_partner",
        column1="lead",
        column2="related_partners",
        help="All the contacts related to the lead",
        compute="_compute_partner_ids",
        inverse="_inverse_partner_ids",
        store=True,
        readonly=False,
    )
    referrent_id = fields.Many2one(string="Referred by", comodel_name="res.partner")

    regulatory_calcul_ok = fields.Boolean("Regularoty Calcultation")
    worksite_request_ok = fields.Boolean("Worksite Request")
    purchase_obligation_ok = fields.Boolean("Purchase Obligation")
    security_ok = fields.Boolean("Security")
    powergrid_ok = fields.Boolean("Power Grid")

    date_prestudy = fields.Date("Pre-study date")
    date_qualified_project = fields.Date("Qualfied Project date")
    date_proposition_made = fields.Date("Proposition Made date")
    date_deal_signed = fields.Date("Date deal signed")
    date_distributor_order = fields.Date("Distributor Order date")
    date_commission = fields.Date("Commission date")
    date_guarantees_granted = fields.Date("Date Guarantees granted")
    # Overwrite native date_deadline's string and help in order to match with
    # the "worksite workflow" related to Installer's leads
    date_deadline = fields.Date(
        string="Worksite date",
        help="'Expected' Worksite date if the worksite is not completed yet",
    )

    url_study = fields.Char("Study MyDS")
    dropbox_folder = fields.Char("Dropbox folder")
    url_monitoring_th = fields.Char("Thermal Monitoring graph")
    url_monitoring_th_2 = fields.Char("Thermal Monitoring scheme")
    url_monitoring_pv = fields.Char("PV Monitoring")
    url_specifications = fields.Char("Specifications")

    commission_file = fields.Binary("Commission")
    guarantees_file = fields.Binary("Guarantees")
    is_photogenic = fields.Boolean("Photogenic Installation")

    solar_power = fields.Float("Solar Power", compute="_compute_solar_power")
    generator_power = fields.Float("Generator Power")
    tank_volume = fields.Float("Tank volume")
    pool_area = fields.Float("Pool Size")

    studies_results = fields.Text(
        "Studies Results",
        readonly="True",
        help="Filled by the MyDS API when a new study is made around this lead",
    )

    @api.constrains(
        "project_manager_id",
        "installer_seller_id",
        "installer_fitter_id",
        "distributor_id",
    )
    def _check_main_partners(self):
        msg = _("The choosen %s '%s' is not recorded as a %s")
        for rec in self:
            pm_id = rec.project_manager_id
            seller_id = rec.installer_seller_id
            fitter_id = rec.installer_fitter_id
            distrib_id = rec.distributor_id
            if pm_id and not pm_id.is_project_manager:
                field = self._fields["project_manager_id"]
                label = field._description_string(self.env)
                raise ValidationError(msg % (label, pm_id.name, label))

            if seller_id and (not seller_id.is_installer or not seller_id.is_seller):
                field = self._fields["installer_seller_id"]
                label = field._description_string(self.env)
                raise ValidationError(msg % (label, seller_id.name, label))

            if fitter_id and (not fitter_id.is_installer or not fitter_id.is_fitter):
                field = self._fields["installer_fitter_id"]
                label = field._description_string(self.env)
                raise ValidationError(msg % (label, fitter_id.name, label))

            if distrib_id and not distrib_id.is_distributor:
                field = self._fields["distributor_id"]
                label = field._description_string(self.env)
                raise ValidationError(msg % (label, distrib_id.name, label))

    @api.depends("project_manager_id", "building_id", "building_id.is_with_pm")
    def _compute_is_with_pm(self):
        for lead_id in self:
            if lead_id.project_manager_id:
                lead_id.is_with_pm = True
            elif lead_id.building_id.is_with_pm:
                lead_id.is_with_pm = True
            else:
                lead_id.is_with_pm = False

    @api.depends(
        "partner_id",
        "project_manager_id",
        "installer_seller_id",
        "installer_fitter_id",
        "distributor_id",
        "referrent_id",
    )
    def _compute_partner_ids(self):
        for l in self:
            l.partner_ids |= (
                l.partner_id
                | l.project_manager_id
                | l.installer_seller_id
                | l.installer_fitter_id
                | l.distributor_id
                | l.referrent_id
            )

    def _inverse_partner_ids(self):
        ResPartner = self.env["res.partner"]
        cust_categ_id = self.env.ref("crm_installer.end_customer")
        po_categ_id = self.env.ref("crm_installer.project_owner")

        for lead in self:
            lead.partner_ids |= lead.partner_ids.commercial_partner_id
            part_ids = lead.partner_ids
            if not lead.partner_id and not lead.is_with_pm:
                part_id = part_ids.filtered(
                    lambda p: p.is_company and cust_categ_id in p.category_id
                )
                lead.partner_id = part_id[0] if part_id else ResPartner
            if not lead.partner_id and lead.is_with_pm:
                part_id = part_ids.filtered(
                    lambda p: p.is_company and po_categ_id in p.category_id
                )
                lead.partner_id = part_id[0] if part_id else ResPartner
            if not lead.project_manager_id:
                pm_id = part_ids.filtered(
                    lambda p: p.is_company and p.is_project_manager
                )
                lead.project_manager_id = pm_id[0] if pm_id else ResPartner
            if not lead.installer_seller_id:
                inst_id = part_ids.filtered(
                    lambda p: p.is_company and p.is_installer and p.is_seller
                )
                lead.installer_seller_id = inst_id[0] if inst_id else ResPartner
            if not lead.installer_fitter_id:
                inst_id = part_ids.filtered(
                    lambda p: p.is_company and p.is_installer and p.is_fitter
                )
                lead.installer_fitter_id = inst_id[0] if inst_id else ResPartner
            if not lead.distributor_id:
                dist_id = part_ids.filtered(lambda p: p.is_company and p.is_distributor)
                lead.distributor_id = dist_id[0] if dist_id else ResPartner
