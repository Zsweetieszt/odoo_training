from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'name'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    published_year = fields.Integer(string='Published Year', required=True)
    description = fields.Text(string='Description', required=True)
    price = fields.Float(string='Price', digits=(16,2), required=True, default=0.0)
    pages = fields.Integer(string='Pages', required=True)
    available = fields.Boolean(string='Available', required=True, default=True)
    published_date = fields.Date(string='Published Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')
    ], string='Status', default='draft', required=True)

    author_id = fields.Many2one(
        'library.author',
        string='Author Master',
        ondelete='restrict'
    )

    category_ids = fields.Many2many(
        'library.category',
        string='Categories'
    )

    _sql_constraints = [
        (
            'unique_book_name',
            'unique(name)',
            'Book title must be unique!'
        )
    ]

    @api.constrains('pages')
    def _check_pages(self):
        for record in self:
            if record.pages <= 0:
                raise ValidationError('Pages must be greater than 0.')

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError('Price cannot be negative.')

    @api.constrains('published_year')
    def _check_published_year(self):
        current_year = fields.Date.today().year
        for record in self:
            if record.published_year < 1000 or record.published_year > current_year:
                raise ValidationError('Published year is invalid.')