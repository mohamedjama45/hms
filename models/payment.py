from odoo import models,fields,api


class PaymentInherit(models.Model):
    _inherit = 'account.payment'


    fixed_discount = fields.Float(string='Fixed Discount')
    fixed_percentage = fields.Char(string='Percentage Discount')
    discount_type = fields.Selection([
        ('fixed','Fixed'),
        ('percentage','Percentage')
    ], string='Discount Type')


    def create(self, vals):
        vals['amount'] = vals['amount'] - vals['fixed_discount']
        return super().create(vals)


















