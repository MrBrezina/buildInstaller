import os, binascii
from distutils.sysconfig import get_python_lib
from FL import *



#################### Functions & classes ####################

# Separator used for normalized paths
SEP = "/"

def denormalizePath(*paths):
	"""
	Convert path to correct OS-dependent form.
	"""
	
	return os.sep.join(map(lambda x: os.sep.join(x.split(SEP)), paths))

def installPythonPath(fileName, path):
	# Install folder to python modules.
	
	sitePackDir = get_python_lib()
	fileName = os.path.join(sitePackDir, fileName + ".pth")
	f = open(fileName, "w")
	f.write(path)
	f.close()
	return fileName

def installFiles(baseFolder, files):
	for path in files:
		targetPath = os.path.join(baseFolder, denormalizePath(path))
		if not os.path.exists(os.path.dirname(targetPath)):
			os.makedirs(os.path.dirname(targetPath))
		f = open(targetPath, "w")
		f.write(binascii.unhexlify(files[path]))
		f.close()

class BundlesDialog:

	fields = {}

 	def __init__(self, fields, title):

		self.fields = fields

		self.d = Dialog(self)
		self.d.size = Point(300, len(fields)*20+80)
		self.d.Center()
		self.d.title = title
		self.d.AddControl(CHECKBOXCONTROL, Rect(aIDENT2, 20, aIDENT2, aAUTO), "field%d" % 0, STYLE_CHECKBOX, ' ' + fields[0][0])
		exec "self.field%d = %s" % (0, fields[0][1])
		for i in range(len(fields)-1):
			self.d.AddControl(CHECKBOXCONTROL, Rect(aIDENT2, 40+i*20, aIDENT2, aAUTO), "field%d" % (i+1), STYLE_CHECKBOX, ' ' + fields[i+1][0])
			exec "self.field%d = %s" % ((i+1), fields[i+1][1])

	def on_cancel(self, code):
		self.results = None
		self.fields = None

	def on_ok(self, code):
		self.results = []
		for i in range(len(self.fields)):
			self.d.GetValue("field%d" % i)
			exec "self.results.append(int(self.field%d))" % i
			i += 1
		self.results = tuple(self.results)
		return 1

	def Run(self):
		return self.d.Run()

class LicenceDialog:
	def __init__(self, lines, title):
		self.d = Dialog(self)
		self.d.size = Point(400, len(lines)*20+100)
		self.d.Center()
		self.d.title = title
		self.d.AddControl(STATICCONTROL, Rect(aIDENT2, 20, aIDENT2, aAUTO), 'licence', STYLE_LABEL, lines[0])
		for l in range(len(lines)-1):
			self.d.AddControl(STATICCONTROL, Rect(aIDENT2, 40+l*20, aIDENT2, aAUTO), 'licence', STYLE_LABEL, lines[l+1])

		self.d.AddControl(CHECKBOXCONTROL, Rect(aIDENT2, 40+l*20+20, 360, 40+l*20+20+25), 'agree', STYLE_CHECKBOX, ' I agree with the terms of the licence')
		self.agree = 0

	def on_agree(self, code):
		self.d.GetValue('agree')

	def on_ok(self, code):
		return 1

	def Run(self):
		return self.d.Run()
					
#################### Main Program ####################

# 1. get installation folders
macrosFolder = os.path.join(fl.userpath, "Macros")
packagesFolder = get_python_lib()

# 2. install files & Python environment
# 2a. bundles dialog
installBundle = {}
for bundleName, fileType in files:
	installBundle[bundleName] = False
d = BundlesDialog(installBundle.items(), NAME + ": select bundles")
if d.Run() and d.results:
	for i in range(len(installBundle)):
		installBundle[installBundle.items()[i][0]] = d.results[i] == 1
	if not os.path.exists(macrosFolder):
		os.makedirs(os.path.dirname(macrosFolder))
	# 2b. licence dialog
	d = LicenceDialog(LICENCE.split("\n"), NAME + ": licence")
	ok = d.Run()
	while ok == 1 and d.agree == 0:
		fl.Message("You have to agree with the licence to proceed.")
		ok = d.Run()
	if ok == 1 and d.agree == 1:
		# 2c. copy files
		try:
			for bundleName, fileType in files:
				if installBundle[bundleName]:
					if fileType == "macros":
						installFiles(macrosFolder, files[bundleName, fileType])
					elif fileType == "site-packages":
						installFiles(packagesFolder, files[bundleName, fileType])
					# install paths to the environment
					for path, folderName in folders[bundleName, "modules-paths"].items():
						installPythonPath(folderName, os.path.join(macrosFolder, denormalizePath(path)))
					for path, folderName in folders[bundleName, "site-packages-paths"].items():
						installPythonPath(folderName, os.path.join(packagesFolder, denormalizePath(path)))
			# confirmation dialog
			fl.Message("Bundle(s) has been installed.\nClick Reset Macro button for changes to take effect.")
		except:
			fl.Message("Installation was not successful.")
