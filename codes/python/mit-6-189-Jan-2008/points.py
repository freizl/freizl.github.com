#!/usr/bin/python

### Demonstrate Class & Method features

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__rmul__(other)
        return self.x * other.x + self.y * other.y 

    def __rmul__(self, other): # scalar multiplication
        return Point(other * self.x,  other * self.y) 

#    def __radd__()  what is radd?


if __name__ == '__main__':
    p1 = Point(3,4)
    p2 = Point(5,6)
    print p1 + p2
    print p1 * p2
    print 2 * p1  # invoke func __rmul__
    print p1 * 2  # invoke func __mul__
