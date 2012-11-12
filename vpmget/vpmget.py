#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#  vpmget.py
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

import sys
import getopt
import gettext

import messages
import common
import install
import remove
import update
import repos

global PROGNAME
PROGNAME="vpmget"

gettext.bindtextdomain(PROGNAME, "/usr/share/locale")
gettext.textdomain(PROGNAME)

global _
_ = gettext.gettext


#
# Main program function
#
def main(argv):
	short_opts = "iruR:"
	long_opts = ["install", "remove", "udate", "root="]
	
	try:
		opts, args = getopt.getopt(argv[1:], short_opts, long_opts)
	except getopt.error, err :
		print err
		return(1)

	s = common.Settings()
	
	for opt, arg in opts:
		if opt in ("-i", "--install"):
			s.selector = "install"
		elif opt in ("-r", "--remove"):
			s.selector = "remove"
		elif opt in ("-u", "--update"):
			s.selector = "update"
		elif opt in ("-R", "--root"):
			s.root = arg

	if (s.selector == "null"):
		print(_("No main action was selected"))
		exit(1)
		
	switch = {
		"install":install.install_packages,
		"remove":remove.remove_packages,
		"update":repos.update_repos
	}
	
	switch[s.selector](s,args)
	
if __name__ == '__main__':
	sys.exit(main(sys.argv))
