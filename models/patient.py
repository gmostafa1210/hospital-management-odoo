from odoo import fields, models, api, _
from odoo.exceptions import UserError 

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'
    _rec_name = 'pat_name'

    pat_name = fields.Char(string='Name')
    pat_id = fields.Integer(string='ID')
    pat_add = fields.Text(string='Address')
    pat_mobile = fields.Char(string='Mobile')
    pat_email = fields.Char(string='Email')

