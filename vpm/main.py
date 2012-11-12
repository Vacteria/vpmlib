#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2012 Miguel Angel Reynoso Reyes <miguel@vacteria.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import gettext
_ = gettext.gettext

def usage():
	print(_("Im help function"))

def install_packages(oconf, pkgv):
	print("Im install function")
	return(0)
		
def remove_packages(oconf, pkgv):
	print("Im remove function")
	return(0)

def config_packages(oconf, pkgv):
	print("Im config function")
	return(0)

def run_query(oconf, query):
	print("Im query function")
	return(0)

def init_db(oconf, argv):
	print("Im initdb function")
	from vpmlib.common import sql
	
	sql.create_database(oconf.vpmlocaldb)
	return(0)
