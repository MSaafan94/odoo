from odoo import fields,api,models
from odoo.exceptions import ValidationError


class CrmLead(models.Model):
	_inherit = 'crm.lead'

	# open_whatsapp = fields.One2many("crm.lead","crm_id", string="Contact Person")
	
	whatsapp=fields.Char("whatsapp")
	# @api.depends('phone')
	def open_whatsapp(self):
		# for record in self:

		if len(self.phone)<13:
			return {
				"type": 'ir.actions.act_url',
				"url": 'https://web.whatsapp.com/send/?phone=20%s' % (self.phone),
				"target": 'new'
			}
		elif len(self.phone)==13:
			return {
				"type": 'ir.actions.act_url',
				"url": 'https://web.whatsapp.com/send/?phone=%s' % (self.phone),
				"target": 'new'
			}
		else:
			raise ValidationError("Please Provide Contact number for %s" % self.name)	
class CrmLeadContact(models.Model):
	_name = 'crm.lead.contact'

	name = fields.Char("name")
	country_id = fields.Many2one("res.country", "Select Country")
	phone = fields.Char("Contact Number")
	crm_id = fields.Many2one("crm.lead","Crm Lead ID")

