# -*- coding: utf-8 -*-
# from odoo import http


# class FormRegist(http.Controller):
#     @http.route('/form_regist/form_regist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/form_regist/form_regist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('form_regist.listing', {
#             'root': '/form_regist/form_regist',
#             'objects': http.request.env['form_regist.form_regist'].search([]),
#         })

#     @http.route('/form_regist/form_regist/objects/<model("form_regist.form_regist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('form_regist.object', {
#             'object': obj
#         })
