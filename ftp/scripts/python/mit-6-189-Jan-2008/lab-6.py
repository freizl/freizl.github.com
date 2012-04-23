#!/usr/bin/python

### Lab - 6

from math import *

## problem 1 Collision detection of balls
class Ball():
    # center position (x,y) with radius
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __sub__(self, other): # distance with another ball
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def collision(self, other):
        return (self - other) <= (self.radius + other.radius)

if __name__ == '__main__':
    ball1 = Ball(0,0,1)
    ball2 = Ball(3,3,1)
    print ball1.collision(ball2)
    ball1 = Ball(5,5,2)
    ball2 = Ball(2,8,3)
    print ball1.collision(ball2)
