# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custome_module(models.Model):
#     _name = 'custome_module.custome_module'
#     _description = 'custome_module.custome_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
