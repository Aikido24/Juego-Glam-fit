import pygame as pg 
from sys import exit
pg.init()
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#Funcion de eventos#
def events():
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
while True:
    events()

    screen.fill("White")

    pg.display.update()
    clock.tick(60)
