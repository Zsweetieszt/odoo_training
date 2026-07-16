from odoo import models, fields

class LibraryCategory(models.Model):
    _name = 'library.category'
    _description = 'Library Category'
    _order = 'name'

    name = fields.Char(string='Category', required=True)
    description = fields.Text(string='Description')

    book_ids = fields.Many2many(
        'library.book',
        string='Books'
    )

    _sql_constraints = [
        (
            'unique_category_name',
            'unique(name)',
            'Category name must be unique!'
        )
    ]