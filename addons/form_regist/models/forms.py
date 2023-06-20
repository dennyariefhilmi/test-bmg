from odoo import fields, models, api


class test_form(models.Model):
    _name = 'test.form'
    _description = 'Form Registration'
    
    firstname = fields.Char(string="First Name", required=True)
    lastname = fields.Char(string="Last Name", required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('Female', 'Female')],
        required=True, )
    address = fields.Text(string="Address",
                          required=True)

    others_id = fields.Many2one(
        comodel_name='test.others',
        string='Jobs',
        required=False)

class test_others(models.Model):
    _name = 'test.others'
    _description = 'Additional'
    _rec_name = 'job'

    job = fields.Char(
        string='Job', 
        required=False)

    level = fields.Selection(
        string='Level',
        selection=[('high_level', 'Executive or Senior Management'),
                   ('mid_level', 'Middle Management'),
                   ('entry_level', 'Entry Level')],
        required=False, default='entry_level' )

    
    joindate = fields.Date(
        string='Join Date',
        required=False, default=fields.Date.today)

        
    
