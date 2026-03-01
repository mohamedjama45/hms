from odoo import models,fields,api
from datetime import date
from dateutil.relativedelta import relativedelta

class Patients(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Char(string='Patient',required=True)
    phone = fields.Char(string='Phone Number',required=True)
    dictor_id = fields.Many2one(
        'h.dictor',
        string='Doctors',
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        readonly=True
    )
    date_of_birth = fields.Date(string='Date of Birth',compute='_compute_date_of_birth',store=True)
    age = fields.Integer(string='Age',required=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ], string='Gender',required=True)
    card_number = fields.Char(string='Ticket',readonly=True)






    @api.model
    def create(self, vals):
        vals['card_number'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'new'
        record = super(Patients, self).create(vals)
        partner =self.env['res.partner'].create({
            'name':record.name
        })
        record.partner_id = partner.id
        return record

    def create_appoint(self):
        for rec in self:
            if 'hospital.appointment' in self.env.registry:
             self.env['hospital.appointment'].create({
                'patient_id': rec.id,
                'card_number':rec.card_number,
                'doctor_id':rec.dictor_id.id,
                'age':rec.age,
                'state': 'in_progress',
             })





    @api.depends('age')
    def _compute_date_of_birth(self):
        for rec in self:
            today = date.today()
            if rec.age:
                 rec.date_of_birth = today - relativedelta(years=rec.age)
            else:
                rec.date_of_birth = False

    def action_view_booking(self):
        return




