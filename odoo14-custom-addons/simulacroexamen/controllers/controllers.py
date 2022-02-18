# -*- coding: utf-8 -*-
# from odoo import http


# class Simulacroexamen(http.Controller):
#     @http.route('/simulacroexamen/simulacroexamen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/simulacroexamen/simulacroexamen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('simulacroexamen.listing', {
#             'root': '/simulacroexamen/simulacroexamen',
#             'objects': http.request.env['simulacroexamen.simulacroexamen'].search([]),
#         })

#     @http.route('/simulacroexamen/simulacroexamen/objects/<model("simulacroexamen.simulacroexamen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('simulacroexamen.object', {
#             'object': obj
#         })
