---
title: Python Tips
author: Haisheng, Wu
tags: python
---

# re

~~~~~~{.python}
>>> re.split("[^0-9]", "12 34 + 2 *")
['12', '34', '', '', '2', '', '']
~~~~~~

Cant understand how '' being produced.

# list

~~~~~~{.python}
str("abcdef")[::-1] ==> "fedcba"
reduce(lambda x,y:y+x,"abcdef") ==> "fedcba"
sorted([1,5,3,2]) ==> [1,2,3,5]
a = [1,5,3,2]; a.sort() ==> a := [1,2,3,5]
~~~~~~

# dict

~~~~~~{.python}
### demostrate loop a dict and list/dict parameter
def tst_dict(*args, **kargs):
    for k, v in dict(*args, **kargs).iteritems():
        print k, v

def tst_dict2():
    for key in a_dict:
        print key, a_dict[key]

tst_dict(name='aa', place='bb')
tst_dict('aaa', 'bbb') # throw error
~~~~~~

# Mise

~~~~~~{.python}
range(4) ==> [0,1,2,3] #range start from 0 by default
'%s: %r' % (something, other)
'%(name)s is %(value)d' % {
    'name': 'The answer',
    'value': 42,
}
~~~~~~

# Reference
  - [re reference](http://docs.python.org/library/re.html)
