import pygame as pg 
from sys import exit
pg.init()
# canciones
canciones=["ACDC-Thunderstruck"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
Partitura=""
nota=""
play_song=False
lista_notas=[]
tiempo=pg.time.get_ticks
#variables#
size=(800,600)
screen=pg.display.set_mode(size)

def music_time():
    tiempo=pg.time.get_ticks()/100
    print (tiempo)
#tiempo
clock=pg.time.Clock()
current_time=0


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
    screen.fill("Black")
# zona de dibujo
    print (nota.split(';'))
    print (len(nota.split(';')))
    dibujo_nota= nota.split(';')
    if len(dibujo_nota)==2:
        if dibujo_nota[1] =="0\n":
            pg.draw.circle(screen,'Gray',(100,500),50)
        if dibujo_nota[1] =="1\n":
            pg.draw.circle(screen,'Gray',(300,500),50)
        if dibujo_nota[1] =="2\n":
            pg.draw.circle(screen,'Gray',(500,500),50)
        if dibujo_nota[1] =="3\n":
            pg.draw.circle(screen,'Gray',(700,500),50)
    music_time()
    pg.display.update()
        
    clock.tick(60)