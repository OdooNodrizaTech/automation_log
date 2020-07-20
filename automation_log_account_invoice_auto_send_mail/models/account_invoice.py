# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.one 
    def account_invoice_auto_send_mail_item_real(self, mail_template_id, author_id):                
        return_item = super(AccountInvoice, self).account_invoice_auto_send_mail_item_real(mail_template_id, author_id)
        # save_log
        vals = {
            'model': 'account.invoice',
            'res_id': self.id,
            'category': 'account_invoice',
            'action': 'send_mail',                                                                                                                                                                                           
        }
        self.env['automation.log'].sudo().create(vals)
        # return
        return return_item