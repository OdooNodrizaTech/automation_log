# -*- coding: utf-8 -*-
from openerp import _, api, exceptions, fields, models

import logging
_logger = logging.getLogger(__name__)

class SurveyMailComposeMessage(models.TransientModel):
    _inherit = 'survey.mail.compose.message'    
    
    @api.one
    def arelux_create_survey_user_input_log(self, survey_user_input):
        automation_log_vals = {                    
            'model': 'survey.user_input',
            'res_id': survey_user_input.id,
            'category': 'survey_user_input',
            'action': 'send_mail',                                                                                                                                                                                           
        }
        automation_log_obj = self.env['automation.log'].sudo().create(automation_log_vals)                          