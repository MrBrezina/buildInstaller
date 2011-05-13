__copyright__ = """
Copyright (c) David Brezina, 2008. All rights reserved.
Redistribution and use of the script is limited by the BSD licence (http://creativecommons.org/licenses/BSD/).
"""

colour = {"Red":1, "Green":80, "Blue":170}

def Mark(glyphs, colourCode):
	"""
	Mark glyphs with the defined colour.
	"""

	for gl in glyphs:
		gl.mark = colourCode
		#fl.UpdateGlyph(gl.index)