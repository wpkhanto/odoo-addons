from odoo import models, fields
from odoo.http import request
import qrcode
import base64
from io import BytesIO

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qr_code = fields.Binary("QR Code", compute='_generate_qr_code')

    def _generate_qr_code(self):
        if request:
            base_url = request.httprequest.url_root
        else:
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        
        for record in self:
            qr_data = f"{base_url}#id={record.id}&model=product.template"
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            record.qr_code = base64.b64encode(buffer.getvalue())
