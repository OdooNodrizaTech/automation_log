# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def action_auto_create(self):
        self.ensure_one()
        return_item = super(AccountInvoice, self).action_auto_create()
        # save_log
        vals = {
            'model': 'account.invoice',
            'res_id': self.id,
            'category': 'account_invoice',
            'action': 'create'
        }
        self.env['automation.log'].sudo().create(vals)
        # return
        return return_item

    @api.multi
    def action_auto_open(self):
        self.ensure_one()
        return_item = super(AccountInvoice, self).action_auto_open()
        # save_log
        vals = {
            'model': 'account.invoice',
            'res_id': self.id,
            'category': 'account_invoice',
            'action': 'valid'
        }
        self.env['automation.log'].sudo().create(vals)
        # return
        return return_item
