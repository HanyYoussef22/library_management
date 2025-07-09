# return_book_wizard.py

from odoo import models, fields, api

class ReturnBookWizard(models.TransientModel):
    _name = 'library.return.book.wizard'
    _description = 'Return Book Wizard'

    loan_id = fields.Many2one('library.loan', string='Loan', required=True)

    def action_confirm_return(self):
        self.ensure_one()
        if self.loan_id.state != 'borrowed':
            return  # or raise warning
        self.loan_id.action_return()
