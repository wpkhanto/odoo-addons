{
    'name': 'CRM Geo Location',
    'version': '1.0',
    'depends': ['base', 'crm'],
    'author': 'Jobbexec',
    'category': 'CRM',
    'description': """
    Adds a button to fetch latitude and longitude in CRM module.
    """,
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'crm_lead_geo_location/static/src/components/*'
        ]
    },
}
