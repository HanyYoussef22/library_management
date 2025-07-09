from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    isbn = fields.Char(string="ISBN", required=True, size=13)
    publication_year = fields.Integer(string="Publication Year")
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    ], string="Status", default='available', required=True)

    _sql_constraints = [
        ('isbn_unique', 'unique(isbn)', 'ISBN must be unique!'),
    ]

    @api.constrains('isbn')
    def _check_isbn_length(self):
        for record in self:
            if record.isbn and len(record.isbn) != 13:
                raise ValidationError("ISBN must be exactly 13 digits.")
