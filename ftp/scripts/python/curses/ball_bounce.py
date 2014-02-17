#!/usr/bin/env python
# Simple ball bounce demo
# 

import random, string, traceback
import curses
import math

class Ball(object):
    """
    x,y : init position at first quadrant
    Vx : init horizontal velocity
    Vy : init vertical velocity
    """
    def __init__(self, x_postion, y_postion, x_velocity, y_velocity):
        self.x = x_postion
        self.y = y_postion
        self.Vx = x_velocity
        self.Vy = y_velocity

class BallBoard:
    def __init__(self, scr, char=ord('*')):
        self.state = {}
        self.scr = scr
        Y, X = self.scr.getmaxyx()
        self.X, self.Y = X-2, Y-2-1
        self.char = char
        self.scr.clear()

        # Draw a border around the board
        border_line = '+'+(self.X*'-')+'+'
        self.scr.addstr(0, 0, border_line)
        self.scr.addstr(self.Y+1,0, border_line)
        for y in range(0, self.Y):
            self.scr.addstr(1+y, 0, '|')
            self.scr.addstr(1+y, self.X+1, '|')
        self.scr.refresh()

## TODO
#drag = .1 * .5 * 1.29 * 0.001 * math.pi
#accerlation = gravity  - drag * (velocity**2)
    def throw_ball(self):
        global accerlation
        global dt
        global ground_resis
        accerlation = -9.8
        ground_resis = 0.8
        dt = .01

        x = random.randint(1,self.X)
        y = random.randint(1,self.Y)
        x_velocity = random.randint(-50,50)
        y_velocity = random.randint(-50,50)
        self._throw_one_ball(Ball(x,y,x_velocity,y_velocity))
        
    def _throw_one_ball(self, ball):
        """
        a := accerlation, is gravity when without resistence
        V0 := init velocity
        Vt := velocity after time t
        
        S = V0*t + 0.5 * a * t**2
        2 * a * S = Vt**2 - V0**2
        """
        open('tst.log', 'wb').write('')
        seconds = 0

        while True:
            seconds += dt
            s = ball.Vy * seconds + .5 * accerlation * seconds**2
            h = ball.y + s
            vty = math.copysign(math.sqrt(2 * accerlation * s + ball.Vy**2), s)
            vtx = ball.Vx
            w = ball.x + vtx * seconds

            open('tst.log', 'a').write('debug11: ' + '==='.join([str(item) for item in [s,h,vty,vtx,w,'\n']]))

            if h < 1 and s < 0 and vty < 0 and vty > -0.2: break

            # Hit Top/Bottom Wall 
            if h < 1 and vty < 0 or h > self.Y and vty > 0:
                open('tst.log', 'a').write('debug22: ' + '==='.join([str(item) for item in [s,h,vty,'\n']]))
                ball.y = h > self.Y and self.Y or 1
                ball.x = w
                ball.Vy = -(vty * ground_resis)
                ball.Vx = vtx * ground_resis
                seconds = 0
                continue

            # Hit Left/Right Wall
            if w > self.X and vtx > 0 or w < 1 and vtx < 0:
                open('tst.log', 'a').write('debug44: ' + '==='.join([str(item) for item in [s,h,vty,vtx,w,'\n']]))
                ball.x = w > self.X and self.X or 1
                ball.y = h
                ball.Vy = ground_resis * vty
                ball.Vx = - ground_resis * vtx
                seconds = 0
                continue

            if vty < 0.2 and vty > 0:
                open('tst.log', 'a').write('debug33: ' + '==='.join([str(item) for item in [s,h,vty,'\n']]))
                ball.y = h
                ball.x = w
                ball.Vy = 0
                seconds = 0
                continue

            self._draw_ball(h, w)            
            curses.napms(2)

    def _draw_ball(self, height=0, width=0):
        int_h = int(round(self.Y - height)) + 1
        int_w = int(round(width))
        self.scr.addch(int_h, int_w, ord('o'))
        self.scr.refresh()
        self.scr.addch(int_h, int_w, ord(' '))

def display_menu(stdscr, menu_y):
    stdscr.addstr(menu_y+1, 4, 'S)tart throwing balls, Q)uit [Ctrl-C to force to quit]')

def keyloop(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr_y, stdscr_x = stdscr.getmaxyx()
    menu_y = (stdscr_y-2)-1
    display_menu(stdscr, menu_y)

    subwin = stdscr.subwin(stdscr_y-3, stdscr_x, 0, 0)
    board = BallBoard(subwin, char=ord('*'))

    # Main loop:
    while (1):
        c = stdscr.getch()                # Get a keystroke
        if 0<c<256:
            c = chr(c)
            if c in 'Ss':
                board.throw_ball()
            elif c in 'Qq':
                break
            else: pass                  # Ignore incorrect keys
        else:
            pass

def main(stdscr):
    keyloop(stdscr)                    # Enter the main loop

if __name__ == '__main__':
    curses.wrapper(main)
