# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase

PRICE_TEST = [
    (12345, "12 345,00"),
    (12.3, "12,30"),
    (12.300, "12,30"),
    (12.3456, "12,3456"),
    (12.34564, "12,3456"),
    (-12.3, "-12,30"),
    (0, "0,00"),
]


class TestReportTools(TransactionCase):
    def setUp(cls):
        super(TestReportTools, cls).setUp()
        cls.partner = cls.env["res.partner"].search([], limit=1)
        # TODO:
        # - create model res.partner inheriting report.tools.mixin
        #   using https://github.com/akretion/odoo-test-helper
        # - create a decimal precision with 4 digits

    def test_price_str(self):
        # TODO!
        def _print_price(self, f, expected):
            result = cls.partner.price_to_str(f)
            success = "YES" if result == expected else "NO"
            print(f, ">", expected, " - result :", result, " - ", success)

        for f, expected in PRICE_TEST:
            _print_price(self, f, expected)
