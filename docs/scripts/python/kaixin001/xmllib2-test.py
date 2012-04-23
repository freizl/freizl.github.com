#!/usr/bin/python
# -*- coding:utf-8 -*-

import libxml2
import re

#encoded = repr(open('res.xml','wb').read())
#open('res-new.xml', 'wb').write(encoded)
#rm \n

doc = libxml2.parseFile("res.xml")
ctxt = doc.xpathNewContext()
res = ctxt.xpathEval("//item")

print ">>", res[5]
print ">>", re.findall(r"\d\d%",res[5].content)
print ">>", len(re.findall(r"\d\d%",res[0].content))
print ">>", res[5].content.find('已偷过')

#print str(res[0].xpathEval2("//wapcrops/text()")[0])[:9]
#if str(res[0].xpathEval2("//wapcrops/text()")[0])[:9] == '已偷过':
 #   print 'aaaa'

for item in res[0:15]:
#    wapcrops = res[i].xpathEval2("//crops/text()")[0]
    if item.content.find('已偷过') < 0 and len(re.findall(r"\d\d%", item.content)) == 0:
        print item.content[1:3]



#    wapcrops = str(item.xpathEval2("//wapcrops/text()")[0])[:9]

    
doc.freeDoc()
ctxt.xpathFreeContext()
