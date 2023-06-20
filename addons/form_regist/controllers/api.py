from odoo import http
from odoo.http import request
import json

class FormApi(http.Controller):
    @http.route(['/form/get_api/'], auth='public', method=['GET'], type='http', csrf=False)
    def FormApi(self, **kw):
        form = request.env['test.form'].search([])
        result = []
        for record in form:
            result.append({
                'firstname': record.firstname,
                'lastname': record.lastname,
                'gender': record.gender,
                'address': record.address,
            })
        return json.dumps(result)