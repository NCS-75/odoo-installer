# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Base Report for Installer",
    "summary": """
        Custom base header and footer for Installers reports""",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://akretion.com",
    "depends": ["base", "account", "web", "l10n_fr_siret", "partner_company"],
    "data": [
        "report/report_templates.xml",
        "views/base_document_layout_views.xml",
        "views/report_base_installer.xml",
        "views/res_company_views.xml",
    ],
    "demo": [],
    "post_init_hook": "post_init_hook",
}
