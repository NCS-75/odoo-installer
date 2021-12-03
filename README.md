# odoo-installer

These modules contain hard datas with hard coded SQL IDs for the following models :

- crm.building
- crm.heater
- crm.lost.reason
- crm.roof.covering
- crm.roof
- crm.stage
- crm.use
- res.partner.category
- res.partner.range
- res.partner.relation
- res.partner.role
- res.partner.stage

To update any of these datas, you need to :

1. Inform the **MyDualSun admin** about the future update
2. Update the datas (by SQL command or python script) on **all the databases** using these datas
3. Update the API points for these datas in **module crm_api** (if some fields names changed)
4. Update the SQL IDs used in DualSun **website's forms** (if the SQL IDs changed)
5. Update the basic **CSV files** used to load these datas (on new databases) in their respective modules (here in this repository)



<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | summary
--- | --- | ---
[crm_aftersale](crm_aftersale/) | 14.0.1.0.0 | Add CRM After-Sales menu
[crm_api](crm_api/) | 14.0.1.0.0 | Exposes Partners and Opportunities as REST API
[crm_installer](crm_installer/) | 14.0.1.0.0 | Specific fields and stages for a perfect CRM for DualSun's installers
[crm_installer_maps](crm_installer_maps/) | 14.0.1.0.0 | Google maps tools for Isntaller's CRM
[partner_address](partner_address/) | 14.0.1.0.0 | - Split partner's child_ids between contact and addresses - Add coworkers to individuals - New field 'Address type'
[partner_address_account](partner_address_account/) | 14.0.1.0.0 | Improvements on partner_address used with account module
[partner_address_firstname](partner_address_firstname/) | 14.0.1.0.0 | Improvements on partner_address used with partner_firstname
[partner_address_open_tab](partner_address_open_tab/) | 14.0.1.0.0 | Improvements on partner_address used with web_widget_open_tab
[partner_company](partner_company/) | 14.0.1.0.0 | - Add 'Share Capital' field in res.partner and res.company - New page for company specific res.partner's fields - New page for Coworkers if any
[partner_company_l10n_fr](partner_company_l10n_fr/) | 14.0.1.0.0 | Move SIRET fields in new res.partner's Company page from module partner_company
[partner_default_lang](partner_default_lang/) | 14.0.1.0.0 | Define res.partner's lang as user's company's.
[partner_installer](partner_installer/) | 14.0.1.0.0 | Minimum installer's fields on res.partner for connection with MyDS, with datas but no views.
[partner_relation](partner_relation/) | 14.0.1.0.0 | We separate this model's creation from `dualsun_base` because we need the model to exist before loading "dualsun_base/data/partner_extra_data.xml" in pre_init_hook.
[partner_role](partner_role/) | 14.0.1.0.0 | Add a "Role" field on Partners and Partners Categories, allowing to relate to the Partner one specific info from one specific Category. We separate this model's creation from `partner_role` because we need the model to exist before loading "partner_role/data/partner_extra_data.xml" in pre_init_hook.
[partner_stage](partner_stage/) | 14.0.1.0.0 | res.partner stage model and fields for MyDS connection. No views.
[report_base_installer](report_base_installer/) | 14.0.1.0.0 | Custom base header and footer for Installers reports
[report_sale_installer](report_sale_installer/) | 14.0.1.0.0 | Report for Sale Orders
[report_tools](report_tools/) | 14.0.1.0.0 | Useful mixin model providing methods to display custom numbers formats on reports
[sql_tools](sql_tools/) | 14.0.1.0.0 | Tools for SQL IDs settings
[web_form_background_color](web_form_background_color/) | 12.0.1.0.0 | Enable to change some models form's background color

[//]: # (end addons)

<!-- prettier-ignore-end -->
