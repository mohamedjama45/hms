from odoo import models,fields,api
from datetime import date


class Prescription(models.Model):
    _name = 'hospital.prescription'
    _inherit = ['mail.thread','mail.activity.mixin']


    prescription_date = fields.Date(string='Prescription Date',default=fields.Datetime.today,readonly=True)
    prescription_number = fields.Char(string='Prescription Number',required=True)
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True
    )
    dictor_id = fields.Many2one(
        'h.dictor',
        string='Doctor',
        required=True
    )











