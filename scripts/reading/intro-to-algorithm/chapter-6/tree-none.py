#!/usr/bin/python

""" TODO
1. draw a tree graph
"""

import Image, ImageDraw

im = Image.new("RGB",(400,300))

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.ellipse((1,1,50,50))
del draw
im.show()
#im.save(sys.stdout, "PNG")
