# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
     _name = 'academy.teachers'
     _description = u'老师信息'

     name = fields.Char()
     biography = fields.Html()

     course_ids = fields.One2many('academy.courses', 'teacher_id', string="Courses")
#     course_ids = fields.One2many('product.template', 'teacher_id', string="Courses")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Courses(models.Model):
     _name = 'academy.courses'
     _description = u'课程信息'

     name = fields.Char()
     _inherit = 'mail.thread'
#     _inherit = 'product.template'

     teacher_id = fields.Many2one('academy.teachers', string="Tearcher")
