# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = "crm.lead"

    url_drive = fields.Char("Drive Folder")
    code = fields.Char("Code") # Numéro de dossier

    # --- Administration
    # - Worksite Request
    date_worksite_request = fields.Date(string="Worksite Request Sent")
    date_worksite_request_voucher = fields.Date(string="Worksite Request Voucher")
    date_worksite_request_ok = fields.Date(string="Worksite Request OK")

    additional_doc_ready = fields.Boolean(string="Additional Doc. Ready")
    date_additional_doc_sent = fields.Date(string="Additional Doc. Sent")
    date_additional_doc_voucher = fields.Date(string="Additional Doc. Voucher")
    # - Connection
    date_security_visit = fields.Date(string="Security Visit")
    date_security_ok = fields.Date(string="Security Certificate")

    date_powergrid_request = fields.Date(string="Powergrid Request")
    date_powergrid_commissioned = fields.Date(string="Powergrid Commissioned")
    # - Invoicing
    date_invoice_sent = fields.Date(string="Invoice sent")
    is_maintenance_contract = fields.Boolean(string="Maintenance Contract")
    is_advance_pay_received = fields.Boolean(string="Advance Payment Received")


    # --- Technical
    # - Technical Visit
    technical_visit_user_id = fields.Many2one(
        string="TV Technician", comodel_name="res.users"
    )
    date_technical_visit = fields.Date(string="Technical Visit")
    difficulty = fields.Selection(
        string="Difficulty",
        selection=[("easy", "Easy"), ("normal", "Normal"), ("hard", "Hard")],
    )
    mandays_estimated = fields.Float(string="Estimated man-days")
    # - Installation
    installation_user_id = fields.Many2one(
    string="Installation Manager", comodel_name="res.users"
    )
    equipment_ordered = fields.Boolean(string="Equipment Ordered")
    date_worksite_end = fields.Date(string="Worksite End date")
    mandays_spent = fields.Float(string="Spent man-days")
    # - Reception
    is_installation_file_complete = fields.Boolean(string="Complete Installation File")
    is_photo_received = fields.Boolean(string="Photo Received")
    is_monitoring_sent = fields.Boolean(string="Monitoring Sent")
    is_monitoring_confirmed = fields.Boolean(string="Monitoring Confirmed")

    # --- Commercial
    # is_paid_lead = fields.Boolean(string="Paid Lead")
    # is_free_lead = fields.Boolean(string="Free Lead")
    # is_personal_lead = fields.Boolean(string="Personal Lead")
    # is_sponsored_lead = fields.Boolean(string="Sponsored Lead")
    # TODO: ==> liste choix simple à la place des 4 booléens?

    # TODO:
    # Revente Totale	Booléen
    # Revente Surplus	Booléen
    # Auto Consommation	Booléen
    # Bâtiment de France	Booléen


    # TODO:
    # - toggle worksite_request_ok when filling date_worksite_request_ok
    # - add on views date_deal_signed
