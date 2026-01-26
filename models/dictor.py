from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta


class Dictor(models.Model):
    _name = 'h.dictor'
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Char(string='Doctor Name',required=True)
    phone = fields.Char(string='Phone Number',required=True)
    sector_id = fields.Many2one(
        'h.sector',
        string='Speciality',
        required=True
    )
    date_of_birth = fields.Date(string='Date of Birth',compute='_compute_date_of_birth',store=True)
    age = fields.Integer(string='Age',required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender',required=True)



    @api.depends('age')
    def _compute_date_of_birth(self):
        for rec in self:
          today = date.today()
          if rec.age:
              rec.date_of_birth = today - relativedelta(years=rec.age)
          else:
              rec.date_of_birth = False

















