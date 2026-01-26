from odoo import models,fields,api
from datetime import date


class Sector(models.Model):
    _name = 'h.sector'



    name = fields.Char(string='Speciality',required=True)















