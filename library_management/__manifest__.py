{
    'name': 'Library Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Simple module to manage library books',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'installable': True,
    'application': True,
}
