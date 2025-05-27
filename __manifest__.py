# -*- coding: utf-8 -*-
{
    'name': "School Management System",
    'summary': "School Management System for Odoo",
    'description': """
        Complete School Management System
        ================================
        Manage students, teachers, classes, and academic records.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Education',  # More specific category
    'version': '17.0.1.0.0',  # Proper Odoo 17 versioning
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        # Only include files that actually exist
        # 'views/templates.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',  # Add license
}