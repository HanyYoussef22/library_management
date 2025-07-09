{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Manage books, members, and loans in a library',
    'category': 'Library',
    'author': 'Zad',
    'depends': ['base'],
    'data': [
        # Security
        'security/library_groups.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',

        # Actions أولًا عشان الزرار يشتغل
        'views/actions.xml',

        # Main Views
        'views/book_views.xml',
        'views/loan_views.xml',
        'views/res_partner_view_inherit.xml',
        'views/dashboard_views.xml',

        # Wizards Views (المسارات المصححة هنا)
        'wizard/book_borrow_wizard_view.xml',
        'wizard/return_book_wizard_view.xml',

        # Menu
        'views/menu.xml',

        # Reports
        'reports/report_library_loan_template.xml',
        'reports/library_loan_report.xml',

        # Scheduled Actions
        'data/scheduled_actions.xml',
    ],

    'installable': True,
    'application': True,
}
