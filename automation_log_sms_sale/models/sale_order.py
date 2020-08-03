# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_send_sms_automatic(self,
                                  sms_template_id=False,
                                  need_check_date_order_send_sms=True
                                  ):
        self.ensure_one()
        res = super(SaleOrder, self).action_send_sms_automatic(
            sms_template_id,
            need_check_date_order_send_sms
        )
        # save_log
        if self.date_order_send_sms:
            vals = {
                'model': 'sale.order',
                'res_id': self.id,
                'category': 'sale_order',
                'action': 'send_sms'
            }
            self.env['automation.log'].sudo().create(vals)
        # return
        return res
