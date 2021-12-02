# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPartnerRole(TransactionCase):
    def setUp(self):
        super(TestPartnerRole, self).setUp()
        self.partner = self.env["res.partner"].create({"name": "Partner"})
        self.role_1 = self.env.ref("partner_role.role_installer")
        self.categ_1 = self.env.ref("partner_role.installer")
        self.role_2 = self.env.ref("partner_role.role_distributor")
        self.categ_2 = self.env.ref("partner_role.distributor")

    def test_categ_to_role(self):
        self.partner.write({"category_id": [(4, self.categ_1.id)]})
        self.assertEqual(self.partner.role_id, self.role_1)
        self.partner.write(
            {"category_id": [(4, self.categ_2.id), (3, self.categ_1.id)]}
        )
        self.assertEqual(self.partner.role_id, self.role_2)
        self.assertEqual(self.partner.category_id, self.categ_2)

    def test_role_to_categ(self):
        self.partner.write({"role_id": self.role_1.id})
        self.assertEqual(self.partner.category_id, self.categ_1)
        self.partner.write({"role_id": False})
        self.assertFalse(self.partner.category_id)

    def test_create_partner_with_role(self):
        partner_2 = self.env["res.partner"].create(
            {"name": "Partner 2", "role_id": self.role_1.id}
        )
        self.assertEqual(partner_2.category_id, self.categ_1)

    def test_create_partner_with_categ(self):
        partner_2 = self.env["res.partner"].create(
            {"name": "Partner 2", "category_id":  [(4, self.categ_2.id)]}
        )
        self.assertEqual(partner_2.role_id, self.role_2)
