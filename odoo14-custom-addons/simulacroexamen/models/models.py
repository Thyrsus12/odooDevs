# -*- coding: utf-8 -*-

from attr import field
from odoo import models, fields, api


class simulacroexamen(models.Model):
     _name = 'simulacroexamen.simulacroexamen' #nombre de la tabla de la BD
     _description = 'simulacroexamen.simulacroexamen'

     name = fields.Char()
     value = fields.Integer()
     value2 = fields.Float(compute="_value_pc", store=True) #campo computado, value2 depende del valor de value
     description = fields.Text()
     prioridad = fields.Integer()
     urgente = fields.Boolean(compute = "_value_urgente", store = True)
     fecha = fields.Date()
     avatar = fields.Image('image tarea', max_width=50, max_height=50)

     @api.depends('prioridad')
     def _value_urgente(self):
         for record in self:
             if record.prioridad >= 8:
                 record.urgente = True
             else:
                 record.urgente = False
