from PIL import Image
from pytesser import *
from BeautifulSoup import BeautifulSoup
import sys

w_index  = 0
h_index = 1 
img = Image.open(sys.argv[1])
img = img.convert("RGB")
pixdata = img.load()

for y in xrange(img.size[h_index]):
        for x in xrange(img.size[w_index]):
            if pixdata[x, y] != (255, 255, 255):
                print pixdata[x, y]

html_text = image_to_string(img)
