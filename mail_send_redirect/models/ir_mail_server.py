# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class IrMailServer(models.Model):
    _inherit = "ir.mail_server"

    @api.model
    def send_email(
        self,
        message,
        mail_server_id=None,
        smtp_server=None,
        smtp_port=None,
        smtp_user=None,
        smtp_password=None,
        smtp_encryption=None,
        smtp_debug=False,
        smtp_session=None,
    ):

        del message["To"]
        del message["Cc"]
        del message["Bcc"]

        redirect_email = (
            self.env["ir.config_parameter"].sudo().get_param("mail.redirect")
        )
        if redirect_email:
            message["To"] = "Adresse de détournement <" + redirect_email + ">"

        return super().send_email(
            message,
            mail_server_id=mail_server_id,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            smtp_user=smtp_user,
            smtp_password=smtp_password,
            smtp_encryption=smtp_encryption,
            smtp_debug=smtp_debug,
            smtp_session=smtp_session,
        )
