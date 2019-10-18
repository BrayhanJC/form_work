# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    Autor: Brayhan Andres Jaramillo Castaño
#    Correo: brayhanjaramillo@hotmail.com
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

from odoo import api, fields, models, _
import time
from datetime import datetime, timedelta, date
import logging
_logger = logging.getLogger(__name__)
from odoo import modules
from odoo.addons import decimal_precision as dp
import base64


class FormOne(models.Model):
	
	_name = 'form.one'

	def get_default_img():
		with open(modules.get_module_resource('form_work', 'static/src/img', 'icon.png'),'rb') as f:
		
			return base64.b64encode(f.read())

	field_binary_logo = fields.Binary(default=get_default_img(), readonly=True)
	name = fields.Char(string="Acta")
	date_act = fields.Date(string="Fecha")
	space = fields.Char(string="Lugar")
	name_meet = fields.Char(string=u"Nombre Reunión")
	theme_main = fields.Char(string="OBJETIVO/TEMA PRINCIPAL")
	hour_begin = fields.Float(string="HORA INICIO")
	hour_end = fields.Float(string="HORA INICIO")
	attendeens_ids = fields.One2many('form.attendees', 'form_one_id', string="ASISTENTES (A) / INVITADOS (I)")
	commitment_ids = fields.One2many('form.commitment', 'form_one_id', string="TAREAS Y COMPROMISOS")
	date_meet = fields.Date(string=u"FECHA DE REUNÓN")
	duration = fields.Float(string="DURACIÓN")
	relevant_themes = fields.Text(string="TEMAS RELEVANTES")
	job_id = fields.Many2one('hr.job', string=U"CARGO DE LA PERSONA QUE CONVOCA LA REUNIÓN")
	digital_signature = fields.Binary(string='FIRMA')

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('form.one')
		
		res = super(FormOne, self).create(vals)
		return res




FormOne()