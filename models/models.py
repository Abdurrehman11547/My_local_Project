-*- coding: utf-8 -*-

from odoo import models, fields, api


class my_local__project(models.Model):
    _name = 'my_local'
    _description = 'my_local__project.my_local__project'

    name = fields.Char()
    value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

