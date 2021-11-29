# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    customer_longitude = fields.Float(
        string='Customer Longitude', digits=(16, 5)
    )
    customer_latitude = fields.Float(
        string='Customer Latitude', digits=(16, 5)
    )

    @api.model
    def _geo_localize(self, street='', zip='', city='', state='', country=''):
        geo_obj = self.env['base.geocoder']
        search = geo_obj.geo_query_address(
            street=street, zip=zip, city=city, state=state, country=country
        )
        result = geo_obj.geo_find(search, force_country=country)
        if result is None:
            search = geo_obj.geo_query_address(
                city=city, state=state, country=country
            )
            result = geo_obj.geo_find(search, force_country=country)
        return result

    def geo_localize(self):
        for lead in self.with_context(lang='en_US'):
            result = self._geo_localize(
                street=lead.street,
                zip=lead.zip,
                city=lead.city,
                state=lead.state_id.name,
                country=lead.country_id.name,
            )

            if result:
                lead.write(
                    {
                        'customer_latitude': result[0],
                        'customer_longitude': result[1],
                    }
                )

        return True    
