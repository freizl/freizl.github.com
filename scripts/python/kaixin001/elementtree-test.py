#!/usr/bin/python
# coding:utf-8 -*-

from xml.etree.ElementTree import ElementTree,fromstring
import re

doc = ElementTree(file='res.xml')
result = []

for e in doc.findall('//item/')[0:15]:
    print ">>>", e.getiterator("crops")[0].text
    tmp = re.search('font.*font', e.getiterator("crops")[0].text)
    if tmp is None:
        print e.getiterator("farmnum")[0].text
        result.append(e.getiterator("farmnum")[0].text)
    else:
        print tmp.group(0)


#    print e.getiterator("crops")[0].text

#    print e.getiterator("wapcrops")

#print dir(doc.find("//item/farmnum"))
#print doc.find("//item/crops").text #.encode('utf-8')

#print result

print fromstring('<aaa><bb><cc>33</cc></bb><cc>22</cc></aaa>').findall('bb/cc')

