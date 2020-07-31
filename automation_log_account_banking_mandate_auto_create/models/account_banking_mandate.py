# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountBankingMandate(models.Model):
    _inherit = 'account.banking.mandate'            

    @api.model
    def create(self, values):
        res = super(AccountBankingMandate, self).create(values)
        # operations
        if self.auto_create:
            # save_log
            vals = {
                'model': 'account.banking.mandate',
                'res_id': self.id,
                'category': 'account_banking_mandate',
                'action': 'create',                                                                                                                                                                                           
            }
            self.env['automation.log'].sudo().create(vals)
        # return
        return res

    @api.model
    def validate(self):
        res = super(AccountBankingMandate, self).validate()
        # operations
        if return_create:
            if self.auto_create:
                # save_log
                vals = {
                    'model': 'account.banking.mandate',
                    'res_id': self.id,
                    'category': 'account_banking_mandate',
                    'action': 'validate',                                                                                                                                                                                           
                }
                self.env['automation.log'].sudo().create(vals)
        # return
        return res
