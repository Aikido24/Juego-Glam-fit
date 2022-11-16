import pygame as pg 
from sys import exit


pg.init()
pg.display.set_caption('Iron-Man')
#canciones 
canciones=["Iron-Man"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
Partitura=""
nota=""
play_song=False
lista_notas=[]
centecimas=0
def music_time():
    tiempo=pg.time.get_ticks()/100
    return tiempo
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()




#Funcion de eventos# 
time_Music=pg.USEREVENT +1
pg.time.set_timer(time_Music,100)
def events(): 
    global Partitura , nota , play_song , centecimas , lista_notas
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.play()
                centecimas=music_time()
                Partitura=open(f"data_{canciones[0]}.txt", "r")
                play_song=True 
                nota=Partitura.readline() 
        if play_song:
            if event.type==time_Music:
                numero=music_time()-centecimas
                if nota != "":
                    dibujo_nota= nota.split(';')
                    if int(dibujo_nota[0])-20<= int(numero):

                        if dibujo_nota[1] =="0\n":
                            lista_notas.append([100,0])
                        
                        if dibujo_nota[1] =="1\n":
                            lista_notas.append([300,0]) 
                        
                        if dibujo_nota[1] =="2\n":
                            lista_notas.append([500,0])
                            
                        if dibujo_nota[1] =="3\n":
                            lista_notas.append([700,0])
                        
                        nota=Partitura.readline()    
                    print(nota)
                #print(int(dibujo_nota[0]))
               



while True:
    events()

    screen.fill("White")
    #zona de dibujo
    #print(nota.split(';'))
    #print(len(nota.split(';')))
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
    if len (lista_notas)>0:
        for i in range(len(lista_notas)):
            pg.draw.circle(screen,"Blue",lista_notas[i],50)
            lista_notas[i][1]+=5
    music_time()
    pg.display.update()
    for i in range(len(lista_notas)):
            if lista_notas[i][1]>800:
                lista_notas.pop(i)
                break 
    clock.tick(60)
