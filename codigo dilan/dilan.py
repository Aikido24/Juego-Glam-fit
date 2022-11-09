import pygame as pg 
from sys import exit
pg.init()
# canciones
canciones=["ACDC-Thunderstruck"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
Partitura=""
nota=""
play_song=""
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
#tiempo
clock=pg.time.Clock()
current_time=0

def my_time():
    global current_time
    current_time= int(pg.time.get_ticks()/100)
#music
button1 =False
button2 =False
button3 =False
button4 =False
#Funcion de eventos#
time_music=pg.USEREVENT+1
pg.time.set_timer(time_music,100)
def events():
    global button1 , button2 , button3 , button4 , Partitura , nota , play_song
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.play()
                Partitura=open(f"data_{canciones[0]}.txt" , "r")
                play_song=True

        if play_song:            
            if event.type==time_music:
                nota=Partitura.readline()
                print(nota)
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                button1 =True
            if event.key == pg.K_w:
                button2 =True
            if event.key == pg.K_e:
                button3 =True
            if event.key == pg.K_r:
                button4 =True
        if event.type == pg.KEYUP:
            if event.key == pg.K_q:
                button1 =False
            if event.key == pg.K_w:
                button2 =False
            if event.key == pg.K_e:
                button3 =False
            if event.key == pg.K_r:
                button4 =False
while True:
    events()

    screen.fill("White")
# zona de dibujo
    pg.draw.circle(screen,'Red',(100,500),50)
    pg.draw.circle(screen,'Red',(300,500),50)
    pg.draw.circle(screen,'Red',(500,500),50)
    pg.draw.circle(screen,'Red',(700,500),50)
    if button1:
        pg.draw.circle(screen,'#C71EE8',(100,500),50)
    if button2:
        pg.draw.circle(screen,'#F28C1F',(300,500),50)
    if button3:
        pg.draw.circle(screen,'#561FF2',(500,500),50)
    if button4:
        pg.draw.circle(screen,'#561FF2',(700,500),50)
    pg.display.update()

    my_time()
        
    clock.tick(60)