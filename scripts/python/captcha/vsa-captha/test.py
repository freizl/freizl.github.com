#!/usr/bin/env python
# coding: utf8 -*-

import cookielib, Image, StringIO, urllib, urllib2
from captchaidentifier import CaptchaIdentifier

CAPTHA = 'http://www.vsa.com.cn/user/center/code/image2.jsp'

identify = CaptchaIdentifier()

# Set the cookie
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

# Get the captha image
#img_file = opener.open(CAPTHA)
#tmp = StringIO.StringIO(img_file.read())
#image = Image.open(tmp)

image = Image.open('C:\Documents and Settings\simon.wu\Desktop\captha\\vsa_sample\\11.jpeg')
# Show the image
image.show()

# Parse the captha image
numbers = identify.parse(image)
print numbers
