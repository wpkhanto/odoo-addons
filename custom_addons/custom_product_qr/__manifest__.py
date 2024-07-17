{
    'name': 'Product QR Code',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Add QR code to product template',
    'description': 'This module adds a QR code to the product template view.',
    'depends': ['base', 'product'],
    'data': [
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
}
