import csv
import os
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

    # def generate_csv(self):
    #     folder_path = os.path.dirname(os.path.realpath(__file__))
    #     filename = os.path.join(folder_path, 'output.csv')
    #
    #     data = self.env['test.form'].search([])
    #
    #     fieldnames = ['firstname', 'lastname', 'gender', 'address']
    #
    #     with open(filename, 'w', newline='') as csvfile:
    #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #
    #         writer.writeheader()
    #
    #         for record in data:
    #             writer.writerow({
    #                 'firstname': record.firstname,
    #                 'lastname': record.lastname,
    #                 'gender': record.gender,
    #                 'address': record.address,
    #             })
    #
    #     return True

    _sql_constraints = [
        ('unique_name', 'unique(firstname, lastname)', 'The name must be unique.')
    ]
        
    
