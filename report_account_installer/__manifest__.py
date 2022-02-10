# Copyright 2022 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Report Account Installer",
    "description": """
        Pdf reports for account.move for installers""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": [
        "account",
        # https://github.com/OCA/bank-payment
        "account_payment_partner",
        # https://github.com/akretion/odoo-usability
        "account_usability",
    ],
    "data": ["report/invoice_report_templates.xml"],
    "demo": [],
}
