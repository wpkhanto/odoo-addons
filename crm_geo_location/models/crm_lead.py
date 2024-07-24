from odoo import models, fields, api
import requests

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    latitude = fields.Float(string='Latitude', readonly=True, digits=(9, 7))
    longitude = fields.Float(string='Longitude', readonly=True, digits=(10, 7))

    def get_geo_location(self):
        api_key = 'AIzaSyDpdWOwrMUJJlbsUpNYXNR5MaN5cZkBDgY'  # Replace with your Google API Key
        for record in self:
            # address = f"{record.street}, {record.city}, {record.state_id.name}, {record.country_id.name}"
            coords = self._get_coords_from_wifi(api_key)
            if coords:
                record.latitude = coords.get('lat')
                record.longitude = coords.get('lng')
            else:
                record.latitude = 0
                record.longitude = 0
            # coords = self._get_coords_from_address(address, api_key)
            # if coords:
            #     record.latitude = coords.get('lat')
            #     record.longitude = coords.get('lng')
            # else:
            #     coords = self._get_coords_from_ip(api_key)
            #     record.latitude = coords.get('lat')
            #     record.longitude = coords.get('lng')

    def _get_coords_from_address(self, address, api_key):
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json().get('results')
            if result:
                return result[0]['geometry']['location']
        return None

    def _get_coords_from_ip(self, api_key):
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
        response = requests.post(url, json={})
        if response.status_code == 200:
            result = response.json()
            return {'lat': result.get('location', {}).get('lat'), 'lng': result.get('location', {}).get('lng')}
        return {'lat': 0.0, 'lng': 0.0}

    def _get_coords_from_wifi(self, api_key, **kwargs):
        # Example WiFi information
        wifi_access_points = [
            {
                "macAddress": "7c:57:3c:e9:9a:c5",
                "signalStrength": -67,  # ตัวอย่างการแปลงค่า
                "signalToNoiseRatio": 0  # ข้อมูลนี้ไม่ได้มีในผลลัพธ์
            }
        ]

        # wifi_access_points = kwargs.get('wifiAccessPoints', [])

        if not wifi_access_points:
            return {'error': 'No WiFi access points provided'}

        payload = {
            "wifiAccessPoints": wifi_access_points
        }
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return {'lat': result.get('location', {}).get('lat'), 'lng': result.get('location', {}).get('lng')}
        return {'lat': 0.0, 'lng': 0.0}