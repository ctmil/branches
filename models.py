from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta, date
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)

class res_branch(models.Model):
	_name = 'res.branch'
	_description = 'Sucursal'

	name = fields.Char('Nombre')
	user_ids = fields.One2many(comodel_name='res.users',inverse_name='branch_id',string='Usuarios')

class res_users(models.Model):
	_inherit = 'res.users'

	branch_id = fields.Many2one('res.branch',string='Sucursal')

class account_invoice(models.Model):
	_inherit = 'account.invoice'
	
	branch_id = fields.Many2one('res.branch',string='Sucursal')

        @api.model
        def create(self, vals):
		context = self.env.context
		uid = context.get('uid',False)
		if uid:
			user = self.env['res.users'].browse(uid)
			if user.branch_id:
				vals['branch_id'] = user.branch_id.id
                return super(account_invoice,self).create(vals)

class account_voucher(models.Model):
	_inherit = 'account.voucher'
	
	branch_id = fields.Many2one('res.branch',string='Sucursal')

        @api.model
        def create(self, vals):
		context = self.env.context
		uid = context.get('uid',False)
		if uid:
			user = self.env['res.users'].browse(uid)
			if user.branch_id:
				vals['branch_id'] = user.branch_id.id
                return super(account_voucher,self).create(vals)

class account_move(models.Model):
	_inherit = 'account.move'
	
	branch_id = fields.Many2one('res.branch',string='Sucursal')

        @api.model
        def create(self, vals):
		context = self.env.context
		uid = context.get('uid',False)
		if uid:
			user = self.env['res.users'].browse(uid)
			if user.branch_id:
				vals['branch_id'] = user.branch_id.id
                return super(account_move,self).create(vals)
