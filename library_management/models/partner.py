from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Library Member")
    loan_ids = fields.One2many('library.loan', 'partner_id', string="Loans")
    loan_count = fields.Integer(string="Active Loan Count", compute='_compute_loan_count')

    @api.depends('loan_ids.state')
    def _compute_loan_count(self):
        for partner in self:
            partner.loan_count = len(partner.loan_ids.filtered(lambda loan: loan.state in ['borrowed', 'overdue']))

    def action_view_loans(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Loans',
            'res_model': 'library.loan',
            'view_mode': 'tree,form',
            'domain': [('partner_id', 'in', self.ids)],
            'context': {'default_partner_id': self.id},
        }
