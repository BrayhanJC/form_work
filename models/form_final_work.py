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


class FormFinalWork(models.Model):
	
	_name = 'form.final_work'


	MONTHS = [('january', 'Enero'),
	('february', 'Febrero'),
	('march', 'Marzo'),
	('april', 'Abril'),
	('may', 'Mayo'),
	('june', 'Junio'),
	('july', 'Julio'),
	('august', 'Agosto'),
	('september', 'Septiembre'),
	('october', 'Octubre'),
	('novemeber', 'Noviembre'),
	('december', 'Diciembre'),]

	def get_years():
		year_list = []

		now = datetime.now()
		year = now.year
		for i in range(2000, int(year)):
			year_list.append((i, str(i)))
		return year_list

	name = fields.Char(string="Acta")
	date_current = fields.Date(string="Fecha")
	project_id = fields.Many2one('project.project', string="PROYECTO")
	coordinator_id = fields.Many2one('res.users', string="Coordinador")
	adviser_id = fields.Many2one('res.users', string="Coordinador")
	partner_id = fields.Many2one('res.partner', string="Cliente")
	sede_partner = fields.Char(related='partner_id.street', store=True, string="SEDE")
	resident_id = fields.Many2one('res.users', string="RESIDENT")





	subsystem_ids = fields.One2many('form.subsystem', 'form_final_work_id', string="ENTREGABLES")
	comments = fields.Text(string="Observaciones y comentarios")

	attendeens_ids = fields.One2many('form.attendees', 'form_final_work_id', string="ASISTENTES (A) / INVITADOS (I)")
	res_city_id = fields.Many2one('res.country.state.city', string="Ciudad")
	days = fields.Integer(string="Dias")
	month = fields.Selection(MONTHS, string="Meses")
	year = fields.Selection(get_years(), string='Year',)
	




	digital_signature = fields.Binary(string='FIRMA')

	@api.model
	def create(self, vals):
		vals['name'] = self.env['ir.sequence'].next_by_code('form.final_work')
		
		res = super(FormFinalWork, self).create(vals)
		return res
		
FormFinalWork()