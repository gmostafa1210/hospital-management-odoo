from odoo import fields, models, api, _
from odoo.exceptions import UserError 

class HospitalMedicine(models.Model):
    _name = 'hospital.medicine'
    _description = 'Medicine Information'
    _rec_name = 'mdcn_name'

    mdcn_name = fields.Char(string='Name')
    mdcn_id = fields.Integer(string='ID')
    mdcn_Type = fields.Char(string='Type')
    mdcn_desc = fields.Text(string='Description')

