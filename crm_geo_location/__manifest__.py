{
    'name': 'CRM Geo Location',
    'version': '1.0',
    'depends': ['base', 'crm'],
    'author': 'Your Name',
    'category': 'CRM',
    'description': """
    Adds a button to fetch latitude and longitude in CRM module.
    """,
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
}
