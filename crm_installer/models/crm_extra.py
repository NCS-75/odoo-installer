# Copyright 2021 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from random import randint

from odoo import api, fields, models, _


class CrmUse(models.Model):
    _name = "crm.use"
    _description = "CRM Use"
    _order = "sequence, name"

    name = fields.Char(string="Name", translate=True)
    color = fields.Integer(string='Color')
    sequence = fields.Integer()

class CrmHeater(models.Model):
    _name = "crm.heater"
    _description = "CRM Heater"
    _order = "sequence, name"

    name = fields.Char(string="Name", translate=True)
    color = fields.Integer(string='Color')
    sequence = fields.Integer()

    is_hp_required = fields.Boolean("HP qualification")

class CrmBuilding(models.Model):
    _name = "crm.building"
    _description = "CRM Building"
    _order = "name"

    name = fields.Char(string="Name", translate=True)
    is_with_pm = fields.Boolean("Require a Project Manager")

class CrmRoof(models.Model):
    _name = "crm.roof"
    _description = "CRM Roof"
    _order = "name"

    name = fields.Char(string="Name", translate=True)

class CrmRoofCovering(models.Model):
    _name = "crm.roof.covering"
    _description = "CRM Roof Covering"
    _order = "name"

    name = fields.Char(string="Name", translate=True)
