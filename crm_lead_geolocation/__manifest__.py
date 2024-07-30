{
    'name': 'CRM Lead Geolocation',
    'version': '1.0',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'crm_lead_geolocation/static/src/js/crm_lead_geolocation.js',
        ],
    },
}
