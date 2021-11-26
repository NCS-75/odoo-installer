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
