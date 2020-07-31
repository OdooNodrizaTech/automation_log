# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ShippingExpedition(models.Model):
    _inherit = 'shipping.expedition'

    @api.multi
    def action_send_sms_info_real(self):
        self.ensure_one()
        res = super(ShippingExpedition, self).action_send_sms_info_real()
        # save_log
        vals = {
            'model': 'shipping.expedition',
            'res_id': self.id,
            'category': 'shipping_expedition',
            'action': 'send_sms_info',                                                                                                                                                                                           
        }
        self.env['automation.log'].sudo().create(vals)
        # return
        return res
