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

# noinspection PyStatementEffect
{
    "name": "Paper Parameters",
    "version": "1.0.0",
    "license": "AGPL-3",
    "description": """
        This module allows you to add new parameters for a paper format
        which are then forwarded to wkhtmltopdf command as arguments.
    """,
    "author": "Avoin.Systems",
    "website": "https://avoin.systems",
    "category": "Technical Settings",
    "depends": [
        "report",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/paperformat.xml",
    ],
    "installable": True,  # Can the module be installed or not
    "auto_install": False,  # Will be installed automatically as soon as all the dependencies are installed.
    "application": False,  # False = module, True = app. Explanation here: http://stackoverflow.com/a/32734931/403053
    "active": False,  # Will be automatically installed upon database creation
}
