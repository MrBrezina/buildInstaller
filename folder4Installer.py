#!/usr/bin/python
"""
Save folder entries (recursively) in YAML format for the buildInstaller script.
It saves some time when adding lots of scripts. Very simple and quite experimental code.
"""

import os, sys


#################### Function ####################

# function borrowed from bvdet from theScripts(.com)
def dirEntries(dir_name, subdir, *args):
	"""
	Return a list of file names found in directory 'dir_name'
	If 'subdir' is True, recursively access subdirectories under 'dir_name'.
	Additional arguments, if any, are file extensions to match filenames. Matched file names are added to the list.
	If there are no additional arguments, all files found in the directory are added to the list.
	Example usage: fileList = dir_list(r'H:\TEMP', False, 'txt', 'py')
		Only files with 'txt' and 'py' extensions will be added to the list.
	Example usage: fileList = dir_list(r'H:\TEMP', True)
		All files and all the files in subdirectories under H:\TEMP will be added
		to the list.
	"""
	
	fileList = []
	for file in os.listdir(dir_name):
		dirfile = os.path.join(dir_name, file)
		if os.path.isfile(dirfile):
			if len(args) == 0:
				fileList.append(dirfile)
			else:
				if os.path.splitext(dirfile)[1][1:] in args:
					fileList.append(dirfile)
		# recursively access file names in subdirectories
		elif os.path.isdir(dirfile) and subdir:
			print "Accessing directory:", dirfile
			[fileList.append(f) for f in dirEntries(dirfile, subdir, *args)]
	return fileList

#################### Scanning directory ####################

# get the command-line parameters
if len(sys.argv)<2:
	print "Usage: [python] folder4installer.py <directory> <output YAML file>"
else:
	l = dirEntries(sys.argv[1], True)
	f = open(sys.argv[2], "w")
	for path in l:
		if os.path.basename(path) and os.path.basename(path) != ".DS_Store":
			f.write(path + ":" + "	"*(10-len(path)/4) + os.path.dirname(path) + "\n")
	f.close()