# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Avoin.Systems
#    Copyright 2017 Avoin.Systems
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
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import models, fields


class Report(models.Model):
    _inherit = 'report'

    def _build_wkhtmltopdf_args(self, paperformat,
                                specific_paperformat_args=None):
        # noinspection PyUnresolvedReferences,PyProtectedMember
        command_args = super(Report, self)._build_wkhtmltopdf_args(
            paperformat,
            specific_paperformat_args
        )

        if paperformat.disable_smart_shrinking:
            command_args.extend(['--disable-smart-shrinking'])

        for param in paperformat.custom_params:
            command_args.extend([param.name])
            if param.value:
                command_args.extend([param.value])

        return command_args


class Paper(models.Model):
    _inherit = 'report.paperformat'

    disable_smart_shrinking = fields.Boolean(
        'Disable Smart Shrinking',
        help='Disable the intelligent shrinking strategy '
             'used by WebKit that makes the pixel/dpi '
             'ratio none constant.'
    )

    custom_params = fields.One2many(
        'report.paperformat.parameter',
        'paperformat_id',
        'Custom Parameters',
        help='Custom Parameters passed forward as wkhtmltopdf '
             'command arguments'
    )


class PaperParameter(models.Model):
    _name = 'report.paperformat.parameter'
    _description = 'wkhtmltopdf parameters'

    paperformat_id = fields.Many2one(
        'report.paperformat',
        'Paper Format',
        required=True,
    )

    name = fields.Char(
        'Name',
        required=True,
        help='The command argument name. Remember to add prefix -- or -'
    )

    value = fields.Char(
        'Value',
    )
