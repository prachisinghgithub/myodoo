# -*- coding: utf-8 -*-
# from odoo import http


# class CustomeModule(http.Controller):
#     @http.route('/custome_module/custome_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_module/custome_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_module.listing', {
#             'root': '/custome_module/custome_module',
#             'objects': http.request.env['custome_module.custome_module'].search([]),
#         })

#     @http.route('/custome_module/custome_module/objects/<model("custome_module.custome_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_module.object', {
#             'object': obj
#         })
