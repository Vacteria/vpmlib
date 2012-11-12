#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vpm.py
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

import sys
import getopt
import gettext

sys.path.append("/home/miguel/proyectos/github")

from vpmlib.common.main import *
from vpmlib.vpm.main import *

def main(argv):
	gettext.bindtextdomain("vpm","/usr/share/locale")
	gettext.textdomain("vpm")
	_ = gettext.gettext

	short_options = "ircqIhvsR:"
	long_options = [
		"install", "remove", "config", "query", "initdb", "help", "root=", 
		"verbose", "silent"
	]
	
	try:
		opts, args = getopt.getopt(argv[1:], short_options, long_options)
	except getopt.error, err:
		print(err)
		exit(1)
	
	s = Settings()

	for opt, arg in opts:
		if opt in ("-i", "--install"):
			s.selector = 1
		elif opt in ("-r", "--remove"):
			s.selector = 2
		elif opt in ("-c", "--config"):
			s.selector = 3
		elif opt in ("-q", "--query"):
			s.selector = 4
		elif opt in ("-I", "--initdb"):
			s.selector = 5
		elif opt in ("-h", "--help"):
			s.selector = 6
		elif opt in ("-R", "--root"):
			s.root = arg
		elif opt in ("-v", "--verbose"):
			s.verbose = True
			s.silent = False
		elif opt in ("-s", "--silent"):
			s.silent = True
			s.verbose = False
	
	if (s.selector == None):
		print(_("No main action was selected"))
		exit(1)
	
	switch = {
		1:install_packages,
		2:remove_packages,
		3:config_packages,
		4:run_query,
		5:init_db,
		6:usage
	}
	
	return(switch[s.selector](s,args))


if __name__ == '__main__':
	sys.exit(main(sys.argv))
