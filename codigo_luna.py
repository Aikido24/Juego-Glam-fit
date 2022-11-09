import pygame as pg 
from sys import exit
pg.init()
#canciones 
canciones=["I’m-So-Sorry"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
Partitura=""
nota=""
play_song=False
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
#Funcion de eventos# 
time_Music=pg.USEREVENT +1
pg.time.set_timer(time_Music,100)
def events(): 
    global Partitura , nota , play_song 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.play()
                Partitura=open(f"data_{canciones[0]}.txt", "r")
                play_song=True 
        if play_song:
            if event.type==time_Music:
                nota=Partitura.readline()
                print(nota)


while True:
    events()

    screen.fill("White")
    #zona de dibujo
    print(nota.split(';'))
    print(len(nota.split(';')))
    dibujo_nota= nota.split(';')
    if len(dibujo_nota)==2:
        if dibujo_nota[1] =="0\n":
            pg.draw.circle(screen,'Red',(100,500),50)
        if dibujo_nota[1] =="1\n":
            pg.draw.circle(screen,'Red',(300,500),50)
        if dibujo_nota[1] =="2\n":
            pg.draw.circle(screen,'Red',(500,500),50)
        if dibujo_nota[1] =="3\n":
            pg.draw.circle(screen,'Red',(700,500),50)

    pg.display.update()
    clock.tick(60)
