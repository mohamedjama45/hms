from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _rec_name = 'patient_id'


    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
    )
    doctor_id = fields.Many2one(
        'h.dictor',
        string='Doctors',
    )
    age = fields.Integer(string='Age',required=True)
    card_number = fields.Char(string='Ticket',readonly=True)
    state = fields.Selection([
        ('new','New'),
         ('in_progress','In_progress'),
         ('entered','Entered'),
         ('done','Done'),
        ('cancel','Cancel')
    ])



    def action_cancel(self):
        if self.state == 'in_progress':
            raise ValidationError(_("You cant cancel it"))
        else:
            self.state = 'cancel'


    def action_money(self):
        return{
            'name':'pop up Form',
            'type':'ir.actions.act_window',
            'res_model':'account.payment',
            'view_mode':'form',
            'view_id':self.env.ref('hms.accountka_form').id,
            'target':'new',
            'context':{
            'default_partner_id':self.patient_id.id
        }
        }


    def action_free(self):
        for rec in self:
            return

    def action_credit(self):
        for rec in self:
            return









