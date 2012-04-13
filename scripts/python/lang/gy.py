#!/usr/bin/python

# yieldex.py example of yield, return in generator functions
def gy():
  print "start gy fun"
  x = 2
  y = 3
  print " ... init x and y"
  yield x,y,x+y
  print "finish first yield"
  z = 12
  yield z/x
  print "finish second yield"
  print z/y
  print "end gy fun"
  return

def main():
  print "== start main"
  g = gy()
  print "== init gy and first next"
  print g.next() # prints x,y,x+y
  print "== second next"
  print g.next() # prints z/x
  print "== third next"
  print g.next()

if __name__ == '__main__':
  main()
