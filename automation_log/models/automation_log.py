# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AutomationLog(models.Model):
    _name = 'automation.log'
    _description = 'Automation Log'

    model = fields.Char(
        string='Model'
    )
    res_id = fields.Integer(
        string='Related document'
    )
    category = fields.Selection(
        selection=[
            ('account_invoice', 'Account Invoice'),
            ('arelux_sale_report', 'Arelux Sale Report'),
            ('account_banking_mandate', 'Account Banking Mandate'),
            ('crm_lead', 'Crm Lead'),
            ('sale_order', 'Sale Order'),
            ('shipping_expedition', 'Shipping Expediotion'),
            ('survey_user_input', 'Survey User Input'),
            ('stock_picking', 'Stock Picking'),
        ],
        string='Categoria'
    )
    action = fields.Char(
        string='Accion'
    )
