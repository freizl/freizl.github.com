#!/usr/bin/python

# Static Method
class AClass(object):
  def astatic(): print 'AClass static method'
  astatic = staticmethod(astatic)

aInstance = AClass()
AClass.astatic()


# Class method with Decorator
class BClass(object):
  @classmethod
  def aclassmethod(cls): print 'a class method for', cls.__name__

class BDev(BClass): pass

bInstance = BClass()
dInstance = BDev()
BClass.aclassmethod()
BDev.aclassmethod()
bInstance.aclassmethod()

# Customized Decorator
def showdoc(f):
  if f.__doc__:
    print '%s: %s' %(f.__name__, f.__doc__)
  else:
    print '%s: no docstring' % f.__name__
  return f

@showdoc 
def f1(): 
  "a doc string"
  def __init__(self):
    print 'init of f1 function';

@showdoc 
def f2(): pass

f1()
f2()
