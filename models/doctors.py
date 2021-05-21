from odoo import fields, models, api, _
from odoo.exceptions import UserError 

class HospitalDoctors(models.Model):
    _name = 'hospital.doctors'
    _description = 'Doctors Information'
    _rec_name = 'doc_name'

    doc_name = fields.Char(string='Name')
    doc_id = fields.Integer(string='ID')
    doc_add = fields.Text(string='Address')
    doc_mobile = fields.Char(string='Mobile')
    doc_email = fields.Char(string='Email')

