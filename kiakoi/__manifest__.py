# -*- coding: utf-8 -*-
{
    'name': "KiaKoi",

    'summary': """
        Garder la trace de qui nous a emprunté quoi""",

    'description': """
        ...
    """,

    'author': "Michel Grenson",
    'website': "https://www.michelgrenson.eu/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/kiakoi.xml',
        'views/borrowing.xml',
        'views/object.xml',
        'views/borrower.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/borrower.xml',
        'demo/object.xml',
    ],
}