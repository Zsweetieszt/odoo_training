from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title')
    author = fields.Char(string='Author')
    published_year = fields.Integer(string='Published Year')
