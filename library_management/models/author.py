from odoo import models, fields

class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'
    _order = 'name'

    name = fields.Char(string='Author Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    biography = fields.Text(string='Biography')

    book_ids = fields.One2many(
        'library.book',
        'author_id',
        string='Books'
    )

    _sql_constraints = [
        (
            'unique_author_name',
            'unique(name)',
            'Author name must be unique!'
        )
    ]