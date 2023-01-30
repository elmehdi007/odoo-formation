# -*- coding: utf-8 -*-

from odoo import models, fields, api

class instanceRequest(models.Model):
     _name = 'instance_request.instance_request'
     _description = 'instance_request.instance_request'

     name = fields.Char(string="desgination")
     adress_ip = fields.Char(string="adress_ip")
     active = fields.Boolean(string="active", default=True)
     cpu = fields.Char(string="cpu")
     ram = fields.Char(string="ram")
     disk = fields.Char(string="disk")
     url = fields.Char(string="url")
     state = fields.Selection([ ('brouillon', 'Brouillon'),('soumise', 'Soumise'),('en_traitement', 'en_traitement'),('traitee', 'Traitée')],
                              'Type', default='brouillon')
     limit_date = fields.Date(string="Date limite de traitement")
     treat_date = fields.Date(string="Date de traitement")
     #treat_duration = fields.Char(string='Durée de traitement')
     treat_duration = fields.Float(string='Durée de traitement')

     def action_draft(self):
          for record in self:
               record.state = 'brouillon'

     def action_submit(self):
          for record in self:
               get_if_submit = self.env.context.get('get_if_submit', False)
               print("===============>", get_if_submit)
               record.state = 'soumise'

     def action_progress(self):
          for record in self:
               record.state = 'en_traitement'

     def action_done(self):
          for record in self:
               record.state = 'traitee'