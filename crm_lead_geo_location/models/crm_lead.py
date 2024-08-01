from odoo import models, fields
# from odoo import http
# from odoo.http import request

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    latitude = fields.Char(string='Latitude', readonly=True)
    longitude = fields.Char(string='Longitude', readonly=True)

    def get_geo_location(self):
        return True

    # Way 1 get geo location from google api.
    # def get_geo_location(self):
    #     api_key = 'AIzaSyDpdWOwrMUJJlbsUpNYXNR5MaN5cZkBDgY'
    #     for record in self:
    #         coords = self._get_coords_from_ip(api_key)
    #         record.latitude = coords.get('lat')
    #         record.longitude = coords.get('lng')
    
    # def _get_coords_from_ip(self, api_key):
    #     url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
    #     response = requests.post(url, json={})
    #     if response.status_code == 200:
    #         result = response.json()
    #         return {'lat': result.get('location', {}).get('lat'), 'lng': result.get('location', {}).get('lng')}
    #     return {'lat': 0.0, 'lng': 0.0}