import pygame as pg
import math
import sys
from random import *
import pygame.base


pg.init()


root = pg.display.set_mode((500, 500))
pg.display.set_caption("Aim Trainer")

true = True

radius = randrange(10, 40)
circle_x = randrange(40, 440)
circle_y = randrange(40, 440)

while true:

    pg.time.delay(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            true = False

    pg.draw.circle(root, (255, 0, 0), (circle_x, circle_y), radius)
    pg.display.update()

    mouse_xpos = pg.mouse.get_pos()[0]
    mouse_ypos = pg.mouse.get_pos()[1]

    sqx = (mouse_xpos - circle_x)**2
    sqy = (mouse_ypos - circle_y)**2

    if math.sqrt(sqx + sqy) < radius and pg.mouse.get_pressed()[0]:
        root.fill((0, 0, 0))
        pg.display.update()

        radius = randrange(10, 40)
        circle_x = randrange(50, 450)
        circle_y = randrange(50, 450)

pg.quit()
