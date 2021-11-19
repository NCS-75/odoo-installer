# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.tools.misc import get_lang


class ReportToolsMixin(models.AbstractModel):
    _name = "report.tools.mixin"
    _description = "Report Tools Mixin"

    def price_to_str(self, value, precision="Product Price", min_digits=2):
        """
        :param value: float to convert to string.
        :param precision: Decimal precision's name.
        :param min_digits: minimum cents length to be displayed in result.

        :return: A string with maximum 'precision' values after zero and minimum
        'min_digits' after zero.
        """
        units = cents = ""

        res_digits = self.env["ir.qweb.field.float"].value_to_html(
            value, {"decimal_precision": precision}
        )
        decimal_point = get_lang(self.env).decimal_point
        res_tuplet = res_digits.split(decimal_point)
        units = res_tuplet[0]

        # Force cents to have min 2 significatives zero and max prec digits
        if len(res_tuplet) > 1:
            cents = res_tuplet[1].strip("0")
        while len(cents) < 2:
            cents += "0"

        return units + decimal_point + cents

    def qty_to_str(self, value, precision="Product Unit of Measure", separator=","):
        """
        :param value: float to convert to string.
        :param precision: Decimal precision's name.
        :param separator: result separator between units and cents.

        :return: A string with maximum 'precision' values after zero but without
        unnecessary zero if any.
        """
        units = cents = ""

        res_digits = self.env["ir.qweb.field.float"].value_to_html(
            value, {"decimal_precision": precision}
        )
        decimal_point = get_lang(self.env).decimal_point
        res_tuplet = res_digits.split(decimal_point)
        units = res_tuplet[0]

        if len(res_tuplet) > 1:
            cents = res_tuplet[1].strip("0")

        return units + decimal_point + cents if cents else units
