# -*- coding: utf-8 -*-
from odoo import http

# class Kiakoi(http.Controller):
#     @http.route('/kiakoi/kiakoi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kiakoi/kiakoi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kiakoi.listing', {
#             'root': '/kiakoi/kiakoi',
#             'objects': http.request.env['kiakoi.kiakoi'].search([]),
#         })

#     @http.route('/kiakoi/kiakoi/objects/<model("kiakoi.kiakoi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kiakoi.object', {
#             'object': obj
#         })