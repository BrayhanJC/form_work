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

{
    'name': 'Form Work',
    'version': '12.0',
    'category': '',
    'sequence': 14,
    'summary': '',
    'author': 'Brayhan Jaramillo',
    'license': 'AGPL-3',
    'images': [
    ],
    'depends': [
        'product_pack', 'sale', 'set_sequence_number', 'surcharge_value', 'web_digital_sign'
    ],
    'data': [
    
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'data/res_cities_data.xml',
        'views/form_attendees_view.xml',
        'views/form_commitment_view.xml',
        'views/form_one_view.xml',
        'views/form_subsystem_view.xml',
        'views/form_final_work_view.xml',
        
        'views/menu.xml',


    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
