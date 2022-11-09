import pygame as pg 
from sys import exit
pg.init()
#canciones 
canciones=["I’m-So-Sorry"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
Partitura=""
nota=""
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#Funcion de eventos#
def events(): 
    global Partitura , nota 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.play()
                Partitura=open(f"data_{canciones[0]}.txt", "r")

            if event.key==pg.K_UP:
                nota=Partitura.readline()
                print(nota)

while True:
    events()

    screen.fill("White")

    pg.display.update()
    clock.tick(60)
