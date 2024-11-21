from odoo import *
from odoo import _

class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Custom Model'
    _rec_name = 'description'

    description = fields.Char(string='Description', default="a value", required=True)
    date = fields.Date(string="Date")
    customer = fields.Many2one('res.partner', 'Customer')
    customer_brithday = fields.Date(string="Customer birthday", related='customer.birthday')
    sale_order_id = fields.Many2one('sale.order', ondelete='cascade', string='Sale Order')
    date_allowed = fields.Selection([
        ('nein', 'Nein'),
        ('ja', 'Ja')],
        string='Date Allowed', default='nein', readonly=True,)
    goal_value = fields.Integer()
    value = fields.Integer()
    progress = fields.Float(compute='compute_progress', store=True)

    is_checked = fields.Boolean()

    def set_time(self):
        self.date = fields.Date.today()

    def search_customer(self):
        customer = self.env['res.partner'].search([('name', '=', self.description)], limit=1)
        if len(customer) > 0:  # if customer:
            self.customer = customer.id

    @api.depends('goal_value', 'value')
    def compute_progress(self):
        for record in self:
            if record.goal_value > 0:
                record.progress = record.value / record.goal_value * 100

    def print_etiquette(self):
        return {
            'name': _('Print Etiquette'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'my.model.wizard',
            'view_id': self.env.ref('ff_test_module.view_my_model_wizard').id,
            'target': 'new',
        }
