from odoo import *


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    my_description = fields.Char(string='My Description', default="a value")
    my_model_ids = fields.One2many('my.model', 'sale_order_id', 'My Models')

    def change_name(self):
        self.my_description = "Hallo"

    def get_my_description(self):
        return self.my_description

    def delete(self):
        self.write({'my_model_ids': [(5)]})


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    extra_price = fields.Monetary(currency_field='currency_id', string="My Extra Price")
