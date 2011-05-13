#FLM: Mark Green
__copyright__ = """
Copyright (c) David Brezina, 2008. All rights reserved.
Redistribution and use of the script is limited by the BSD licence (http://creativecommons.org/licenses/BSD/).
"""

__doc__ = """
Mark: Green
"""

from Mark import Mark, colour


#################### Local Dialog, Functions & Constants ####################

def processGlyph(font, gl, index):
	"""
	Adds glyph to lists of selected glyphs and composites.
	"""

	selected.append(gl) # selected is global
	return True



#################### Program ####################

# get selection
selected = [] # list of selected glyphs
fl.ForSelected(processGlyph)

Mark(selected, colour["Green"])
