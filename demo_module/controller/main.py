from odoo import *
from odoo.http import request


class WebsiteHelloWorld(http.Controller):

    # Route to list of all models
    @http.route(['/my/models'], type='http', auth="public", website=True)
    def my_models_list(self, **post):
        testab = 23
        my_model_ids = request.env['my.model'].sudo().search([])

        return request.render("demo_module.my_model_list", {'test': testab, 'my_model_ids': my_model_ids})

    # Route to edit existing model form
    @http.route(['/my/model/<int:model_id>'], methods=['POST', 'GET'], type='http', auth="public", website=True)
    def my_models_detail(self, model_id, **kw):
        my_model_id = request.env['my.model'].sudo().browse(model_id)
        return request.render("demo_module.my_model_detail", {'my_model_id': my_model_id})

    # Route to save changes on existing model form
    @http.route(['/my/model/write/<int:model_id>'], methods=['GET'], type='http', auth="public", website=True, csrf=False)
    def edit_model(self, model_id, **post):
        my_model_id = request.env['my.model'].sudo().browse(model_id)
        my_model_id.write({
            'description': post.get('description'),
            'goal_value': post.get('goal_value'),
            'value': post.get('value'),
            'date': post.get('date'),
        })
        return request.redirect(f'/my/model/{model_id}')

    # Route to delete existing model
    @http.route(['/my/model/delete/<int:model_id>'], methods=['GET'], type='http', auth="public", csrf=False)
    def delete_model(self, model_id, **post):
        my_model_id = request.env['my.model'].sudo().browse(model_id)
        my_model_id.unlink()
        return request.redirect(f'/my/models')

    # Route to open new model form
    @http.route(['/my/model/create'], methods=['POST', 'GET'], type='http', auth="public", website=True, csrf=False)
    def create_model(self, **post):
        return request.render("demo_module.my_model_create")

    # Route to save new model Form
    @http.route(['/my/model/create/save'], methods=['POST', 'GET'], type='http', auth="public", csrf=False)
    def create_model_save(self, **post):
        post['date_allowed'] = 'ja'
        request.env['my.model'].sudo().create(post)
        return request.redirect(f'/my/models')
