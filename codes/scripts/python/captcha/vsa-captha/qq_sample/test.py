#!/usr/bin/env python
# coding: utf8 -*-


""" TODO
1. firebug qq login process
2. firebug qzone secure login
"""

import cookielib, Image, StringIO, urllib, urllib2
from captchaidentifier import CaptchaIdentifier
import ImageFilter

identify = CaptchaIdentifier()

image = Image.open('C:\Documents and Settings\simon.wu\Desktop\captha\\qq_sample\\11.jpeg')

#image.show()
image.filter(ImageFilter.SHARPEN).show()


# Parse the captha image
#numbers = identify.parse(image)
#print numbers
