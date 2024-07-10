# -*- coding: utf-8 -*-
{
    "name": "School Management",

    "summary": """School Management Software""",

    "description": """
        Treating Schools
    """,

    "author": "My Company",
    "website": "https://mycompany.com",

    "category": "Tools",
    "version": "17.0",

    "depends": ['base', 'contacts', 'hr', 'account'],

    "data": [
        'security/ir.model.access.csv',
        'views/school.xml',
    ],

    "demo": [

    ],
    "images": ['static/description/icon.png'],
    "installable": True,
    "application": True,
    "auto_install": False,
}