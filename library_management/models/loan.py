from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'

    book_id = fields.Many2one('library.book', string="Book", required=True)
    partner_id = fields.Many2one('res.partner', string="Member", required=True)
    borrow_date = fields.Date(string="Borrow Date", default=fields.Date.today)
    return_date = fields.Date(string="Return Date", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
        ('overdue', 'Overdue')
    ], string="Status", default='draft', required=True)

    # Actions
    def action_borrow(self):
        for rec in self:
            if rec.book_id.status == 'borrowed':
                raise UserError("This book is already borrowed!")
            rec.book_id.status = 'borrowed'
            rec.state = 'borrowed'

    def action_return(self):
        for rec in self:
            rec.book_id.status = 'available'
            rec.state = 'returned'

    def action_set_draft(self):
        for rec in self:
            rec.book_id.status = 'available'
            rec.state = 'draft'

    def action_mark_overdue(self):
        for rec in self:
            if rec.state == 'borrowed' and rec.return_date < date.today():
                rec.state = 'overdue'

    @api.model
    def cron_check_overdue_loans(self):
        today = date.today()
        overdue_loans = self.search([
            ('state', '=', 'borrowed'),
            ('return_date', '<', today),
        ])
        for loan in overdue_loans:
            loan.state = 'overdue'
            # إرسال إيميل (اختياري إذا فيه template):
            template = self.env.ref(
                'library_management.mail_template_overdue_notification',
                raise_if_not_found=False
            )
            if template:
                template.send_mail(loan.id, force_send=True)

    @api.model
    def cron_check_overdue_loans(self):
        today = date.today()
        overdue_loans = self.search([
            ('state', '=', 'borrowed'),
            ('return_date', '<', today),
        ])
        for loan in overdue_loans:
            loan.state = 'overdue'


    def action_check_overdue_loans(self):
        self.env['library.loan'].cron_check_overdue_loans()

