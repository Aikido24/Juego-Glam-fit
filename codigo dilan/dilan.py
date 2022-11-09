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
centecimas=0
tiempo=pg.time.get_ticks
#variables#
size=(800,600)
screen=pg.display.set_mode(size)

def music_time():
    tiempo=pg.time.get_ticks()/100
    return tiempo
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
    global button1 , button2 , button3 , button4 , Partitura , nota , play_song , centecimas , lista_notas
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.play()
                centecimas=music_time()
                Partitura=open(f"data_{canciones[0]}.txt" , "r")
                play_song=True
                nota=Partitura.readline()

        if play_song:            
            if event.type==time_music:
                numero=music_time()-centecimas
                dibujo_nota= nota.split(';')
                if int (dibujo_nota[0])== int(numero):

                    if dibujo_nota[1] =="0\n":
                        lista_notas.append([100,0])

                    if dibujo_nota[1] =="1\n":
                        lista_notas.append([300,0])

                    if dibujo_nota[1] =="2\n":
                        lista_notas.append([500,0])

                    if dibujo_nota[1] =="3\n":
                        lista_notas.append([700,0])

        
                    nota=Partitura.readline()
                print(int (numero))
                print (int (dibujo_nota[0]))
            
while True:
    events()
    screen.fill("Black")
# zona de dibujo
    # print (nota.split(';'))
    # print (len(nota.split(';')))
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
    if len (lista_notas)>0:
        for i in range(len (lista_notas)):
            pg.draw.circle(screen,"Red",lista_notas[i],50)
            lista_notas[i][1]+=5
            print (i)
    music_time()
    pg.display.update()
        
    clock.tick(60)