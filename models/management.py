from odoo import fields, models, api, _
from odoo.exceptions import UserError 

class HospitalManagement(models.Model):
    _name = 'hospital.management'
    _description = 'Management Information'
    _rec_name = 'hos_name'

    hos_name = fields.Char(string='Hospital Name')
    hos_id = fields.Integer(string='Hospital ID')
    hos_Type = fields.Char(string='Hospital Type')
    hos_desc = fields.Text(string='Description')
    hos_place = fields.Text(string='Address')
    hos_doc_id = fields.Char(string='Doctor List')

