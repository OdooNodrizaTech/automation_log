# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ShippingExpedition(models.Model):
    _inherit = 'shipping.expedition'

    @api.one 
    def action_send_mail_info_real(self):                
        return_item = super(ShippingExpedition, self).action_send_mail_info_real()
        # save_log
        vals = {
            'model': 'shipping.expedition',
            'res_id': self.id,
            'category': 'shipping_expedition',
            'action': 'send_mail_info',                                                                                                                                                                                           
        }
        self.env['automation.log'].sudo().create(vals)
        # return
        return return_item