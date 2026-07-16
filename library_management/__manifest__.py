{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Simple module to manage library books',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
        'views/author_views.xml',
        'views/category_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}