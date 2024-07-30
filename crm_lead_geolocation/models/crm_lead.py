# models/crm_lead.py
from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
