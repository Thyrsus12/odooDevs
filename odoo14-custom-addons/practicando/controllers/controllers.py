# -*- coding: utf-8 -*-
# from odoo import http


# class Practicando(http.Controller):
#     @http.route('/practicando/practicando/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practicando/practicando/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practicando.listing', {
#             'root': '/practicando/practicando',
#             'objects': http.request.env['practicando.practicando'].search([]),
#         })

#     @http.route('/practicando/practicando/objects/<model("practicando.practicando"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practicando.object', {
#             'object': obj
#         })
