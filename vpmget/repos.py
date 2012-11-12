#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sin título.py
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

class Repos(object):
	def __init__(self,objs):
		
		self.mirrorlist = objs.repos
		self.mylist = ["null"]
				
		myFile = open(self.mirrorlist,"r")
		rawList = myFile.readlines()
		myFile.close()

		for i in rawList:
			if ( i[0] != '#' ) or ( i[0] != '' ):
				self.mylist.append(i)

def parse_repos():
	pass
	
def update_repos():
	pass
