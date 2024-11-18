from odoo import *


class MyModelWizard(models.TransientModel):
    _name = 'my.model.wizard'

    labels_count = fields.Integer(string='Labels Count')
    height = fields.Integer(string='Height in cm')
    width = fields.Integer(string='Width in cm')

    def confirm(self):
        pass

