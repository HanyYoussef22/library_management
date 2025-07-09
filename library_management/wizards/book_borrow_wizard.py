from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class BookBorrowWizard(models.TransientModel):
    _name = 'library.book.borrow.wizard'
    _description = 'Borrow Book Wizard'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one(
        'res.partner', string='Member', required=True,
        domain=[('is_library_member', '=', True)]
    )
    borrow_date = fields.Date(string='Borrow Date', default=fields.Date.today, required=True)
    return_date = fields.Date(string='Return Date', required=True)

    def action_confirm_borrow(self):
        self.ensure_one()
        if self.return_date > self.borrow_date + timedelta(days=14):
            raise ValidationError("Return date cannot exceed 14 days.")

        self.env['library.loan'].create({
            'book_id': self.book_id.id,
            'partner_id': self.partner_id.id,
            'borrow_date': self.borrow_date,
            'return_date': self.return_date,
            'state': 'borrowed',
        })
