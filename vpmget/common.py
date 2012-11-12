#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#  common.py
#  
#  Copyright 2012 
#  * Miguel Angel Reynoso <miguel@vacteria.org>
#  * Daniel Angel gebaudo <dag@debian-ar.org>
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

class Settings():
	def __init__(self):
		self.root      = "/"
		self.repos     = self.root+"/etc/vpm/mirrors"
		self.selector  = "null"
		self.verbose   = 0
		self.silent    = 0
		self.rundeps   = 1
		self.conflicts = 1
		self.script    = 1
		self.triggers  = 1

