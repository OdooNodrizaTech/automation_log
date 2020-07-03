# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
_logger = logging.getLogger(__name__)

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from datetime import datetime
import decimal

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def action_send_sms_automatic(self, sms_template_id=False, need_check_date_order_send_sms=True):                
        return_item = super(SaleOrder, self).action_send_sms_automatic(sms_template_id, need_check_date_order_send_sms)        
        #save_log
        if self.date_order_send_sms!=False:
            automation_log_vals = {                    
                'model': 'sale.order',
                'res_id': self.id,
                'category': 'sale_order',
                'action': 'send_sms',                                                                                                                                                                                           
            }
            automation_log_obj = self.env['automation.log'].sudo().create(automation_log_vals)
        #return
        return return_item