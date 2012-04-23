#!/usr/bin/python

def attributesFromDict(d):
    self = d.pop('self')
    for n, v in d.iteritems( ):
        setattr(self, n, v)

class AutoInit(object):
    def __init__(self, foo, bar, baz, boom=1, bang=2):
        print locals()
        attributesFromDict(locals( ))

if __name__ == '__main__':
    ai = AutoInit(111,222,333)
    print ai.foo
