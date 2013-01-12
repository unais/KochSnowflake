import pygame
import math
pygame.init()
black = (0,0,0)
screen = pygame.display.set_mode((600,600))
screen.fill(black)
angle = 0


startx =180
starty = 350

def forward(f):
        global startx, starty
        x0 = startx
        y0 = starty
        x1 = startx + (math.cos((math.pi* angle)/180)*f)
        y1 = starty + (math.sin((math.pi* angle)/180)*f)
        pygame.draw.line(screen,(255,255,255),(x0,y0),(x1,y1),1)
        startx = x1
        starty = y1
#        clock.tick(2)
def right(a):
        global angle
        angle = angle + a

def koch(screen,order,a):
        if order == 0:
           for angles in [60,-120,60,0]:
               forward(1)
               right(angles)
        else:
           for angles  in [60,-120,60,0]:
               koch(screen, order - 1,a)   
               right(angles)

koch(screen,4,60)
right(-120)
koch(screen,4,60)
right(-120)
koch(screen,4,60)
pygame.display.update()
raw_input('Prees any key to quite')
