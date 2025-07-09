from odoo import models, fields, api

class MemberLoanHistoryWizard(models.TransientModel):
    _name = 'library.member.loan.history.wizard'
    _description = 'Member Loan History Wizard'

    partner_id = fields.Many2one('res.partner', string='Member', required=True)
    loan_ids = fields.One2many('library.loan', 'partner_id', string='Loans', compute='_compute_loans')

    @api.depends('partner_id')
    def _compute_loans(self):
        for wizard in self:
            wizard.loan_ids = self.env['library.loan'].search([
                ('partner_id', '=', wizard.partner_id.id)
            ])
