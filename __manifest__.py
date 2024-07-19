{
    'name': 'Lot/Serial QR Code',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Display QR codes on Lots/Serial Numbers',
    'author': 'gcn-cman-jobb',
    'description': 'This module adds a QR code to the product lot/serial number view.',
    'depends': ['stock'],
    'data': [
        'views/stock_production_lot_views.xml',
    ],
    'installable': True,
    'application': False,
}
