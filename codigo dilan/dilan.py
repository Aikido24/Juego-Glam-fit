import pygame as pg 
from sys import exit
pg.init()
#canciones 
canciones=["Iron-man"]
pg.mixer.music.load(f"./audios/{canciones[0]}.mp3")
error= pg.mixer.Sound(f"./sounds/error.wav")
Partitura=""
nota=""
play_song=False
lista_notas_0=[]
lista_notas_1=[]
lista_notas_2=[]
lista_notas_3=[]
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
    global Partitura , nota , play_song , centecimas 
    global lista_notas_0,lista_notas_1,lista_notas_2,lista_notas_3, error
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
            if event.type==pg.KEYDOWN:          
                if event.key == pg.K_q:
                    if len (lista_notas_0)>0:
                        if (lista_notas_0[0][1]>430 and lista_notas_0[0][1]<550):
                            pass 
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                        lista_notas_0.pop(0)
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_w:
                    if len (lista_notas_1)>0:
                        if (lista_notas_1[0][1]>430 and lista_notas_1[0][1]<550):
                            pass 
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_e:
                    if len (lista_notas_2)>0:
                        if (lista_notas_2[0][1]>430 and lista_notas_2[0][1]<550):
                            pass 
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_r:
                    if len (lista_notas_3)>0:
                        if (lista_notas_3[0][1]>430 and lista_notas_3[0][1]<550):
                            pass 
                        else:
                            error.play()
                    else:
                        error.play()
            if event.type==time_Music:
                numero=music_time()-centecimas
                if nota != "":
                    dibujo_nota= nota.split(';')
                    if int(dibujo_nota[0])-20<= int(numero):

                        if dibujo_nota[1] =="0\n":
                            lista_notas_0.append([100,0])
                        
                        if dibujo_nota[1] =="1\n":
                            lista_notas_1.append([300,0]) 
                        
                        if dibujo_nota[1] =="2\n":
                            lista_notas_2.append([500,0])
                            
                        if dibujo_nota[1] =="3\n":
                            lista_notas_3.append([700,0])
                        
                        nota=Partitura.readline()    
                    # print(nota)
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


    if len (lista_notas_0)>0:
        for i in range(len(lista_notas_0)):
            pg.draw.circle(screen,"Blue",lista_notas_0[i],50)
            lista_notas_0[i][1]+=5

    if len (lista_notas_1)>0:
        for i in range(len(lista_notas_1)):
            pg.draw.circle(screen,"Red",lista_notas_1[i],50)
            lista_notas_1[i][1]+=5
    if len (lista_notas_2)>0:
        for i in range(len(lista_notas_2)):
            pg.draw.circle(screen,"Yellow",lista_notas_2[i],50)
            lista_notas_2[i][1]+=5

    if len (lista_notas_3)>0:
        for i in range(len(lista_notas_3)):
            pg.draw.circle(screen,"Green",lista_notas_3[i],50)
            lista_notas_3[i][1]+=5
    music_time()
    pg.display.update()
    for i in range(len(lista_notas_0)):
            if lista_notas_0[i][1]>800:
                lista_notas_0.pop(i)
                error.play()
                break 

    for i in range(len(lista_notas_1)):
            if lista_notas_1[i][1]>800:
                lista_notas_1.pop(i)
                error.play()
                break

    for i in range(len(lista_notas_2)):
            if lista_notas_2[i][1]>800:
                lista_notas_2.pop(i)
                error.play()
                break 

    for i in range(len(lista_notas_3)):
            if lista_notas_3[i][1]>800:
                lista_notas_3.pop(i)
                error.play()
                break 
            
    clock.tick(60)
    # print (lista_notas_0)
