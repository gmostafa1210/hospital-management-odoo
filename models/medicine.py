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
    mdcn_price = fields.Integer(string='Price')
    mdcn_discount = fields.Integer(string='Discount')
    mdcn_fprice = fields.Integer(string='Final Price', compute='_get_final_price')

    def final_price(self):
        price = 0
        discount = 0
        if self.mdcn_price > 0:
            price = self.mdcn_price
        if self.mdcn_discount > 0:
            discount = self.mdcn_discount

        return price - discount
        
    def _get_final_price(self):
        for item in self:
            item.mdcn_fprice = item.final_price()

