# -*- coding: utf-8 -*-
# from odoo import http


# class MyLocalProject(http.Controller):
#     @http.route('/my_local__project/my_local__project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_local__project/my_local__project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_local__project.listing', {
#             'root': '/my_local__project/my_local__project',
#             'objects': http.request.env['my_local__project.my_local__project'].search([]),
#         })

#     @http.route('/my_local__project/my_local__project/objects/<model("my_local__project.my_local__project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_local__project.object', {
#             'object': obj
#         })

