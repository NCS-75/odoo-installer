from odoo.addons.component.core import AbstractComponent
from odoo.exceptions import ValidationError
from odoo.osv import expression


class CrmApiService(AbstractComponent):
    """Base class for REST services"""

    _inherit = "base.rest.service"
    _name = "base.crm.api.service"
    _collection = "crm.api.service"
    _expose_model = None

    def _match_m2o(self, vals, param, model, param_field, odoo_field, match="name"):
        value = getattr(param, param_field)
        if value is not None:
            rec = (
                self.env[model]
                .with_context(lang="en_US")
                .search([(match, "=", value)], limit=1)
            )
            # TODO: special translation for crm.stage (test this code)
            # if model == "crm.stage":
            #     rec = (
            #         self.env[model]
            #         .with_context(lang="en_US")
            #         .search(
            #             ["|", (match, "=", value), ("myds_id.name", "=", value)],
            #             limit=1,
            #         )
            #     )

            # We write False is value is False
            if rec or not value:
                vals[odoo_field] = rec.id
            # If value is not False but we didn't find anything, we raise an error
            else:
                raise ValidationError(
                    "Error on paramater '%s':\n"
                    "No %s record for %s %s" % (param_field, model, match, value)
                )

    def _match_m2m(self, vals, param, model, param_field, odoo_field, match, domain=[]):
        val_list = getattr(param, param_field)
        if val_list is not None:
            search_domain = []
            for val in val_list:
                search_domain = expression.OR([search_domain, [(match, "=", val)]])
            if domain:
                search_domain = expression.AND([search_domain, domain])

            recs = self.env[model].with_context(lang="en_US").search(search_domain)

            if not val_list or (recs and len(recs) == len(val_list)):
                # Erase m2m values if val_list is empty
                ids = [] if not val_list else recs.ids
                vals[odoo_field] = [(6, 0, ids)]
            # If val_list is not empty but we didn't find the expected records
            else:
                msg = (
                    "Error on parameter '%s':\n"
                    "The list %s did not match the expected %s %s records.\n"
                    % (param_field, val_list, len(val_list), model)
                )
                if domain:
                    msg += (
                        "Search result is including the following filter domain: %s"
                        % (domain)
                    )
                raise ValidationError(msg)
