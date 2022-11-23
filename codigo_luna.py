import pygame as pg 
from sys import exit

pg.init()
#variables#
size=(800,600)
screen=pg.display.set_mode(size)
clock=pg.time.Clock()
posicion_cancion=0

#fondos
tex_font = pg.font.Font(None,50)
fondo = pg.image.load('./imagenes/FONDO01.png').convert()
fondo_menu=pg.image.load("./imagenes/MENU/BACKGROUN ROCK CLASS.png").convert_alpha()
posicion= (0,0)
barra_de_puntaje=pg.image.load("./imagenes/BARRA VS.png").convert_alpha()
boton1= pg.image.load('./imagenes/BOTONES/AZUL/01.png').convert_alpha()
posicion1= (150,450)
boton2= pg.image.load('./imagenes/BOTONES/NARANJA/01.png').convert_alpha()
posicion2= (250,450)
boton3= pg.image.load('./imagenes/BOTONES/ROJO/01.png').convert_alpha()
posicion3= (350,450)
boton4= pg.image.load('./imagenes/BOTONES/VERDE/01.png').convert_alpha()
posicion4= (450,450)

boton1_p= pg.image.load('./imagenes/BOTONES/AZUL/02.png').convert_alpha()
boton2_p= pg.image.load('./imagenes/BOTONES/NARANJA/02.png').convert_alpha()
boton3_p= pg.image.load('./imagenes/BOTONES/ROJO/02.png').convert_alpha()
boton4_p= pg.image.load('./imagenes/BOTONES/VERDE/02.png').convert_alpha()

nota1= pg.image.load('./imagenes/BOTONES/AZUL/03.png').convert_alpha()
nota2= pg.image.load('./imagenes/BOTONES/NARANJA/03.png').convert_alpha()
nota3= pg.image.load('./imagenes/BOTONES/ROJO/03.png').convert_alpha()
nota4= pg.image.load('./imagenes/BOTONES/VERDE/03.png').convert_alpha()

b1=False
b2=False
b3=False
b4=False

#canciones 
canciones=["smooth","I’m-So-Sorry","by-the-way"]
numero_cancion=0
pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
error= pg.mixer.Sound(f"./sounds/error.wav")
error.set_volume(0.2)
Partitura=""
nota=""
play_song=False
lista_notas_0=[]
lista_notas_1=[]
lista_notas_2=[]
lista_notas_3=[]
centecimas=0
score_player_1 = 0
score_player_2 = 0
def music_time():
    tiempo=pg.time.get_ticks()/100
    return tiempo


#Funcion de eventos# 
time_Music=pg.USEREVENT +1
pg.time.set_timer(time_Music,100)
def events(): 
    global Partitura , nota , play_song , centecimas 
    global lista_notas_0,lista_notas_1,lista_notas_2,lista_notas_3, error
    global b1, b2, b3, b4, score_player_1, score_player_2, posicion_cancion
    global numero_cancion
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                pg.mixer.music.load(f"./audios/{canciones[numero_cancion]}.mp3")
                
                centecimas=music_time()
                Partitura=open(f"data_{canciones[0]}.txt", "r")
                play_song=True 
                nota=Partitura.readline()
                score_player_1=0
                score_player_2=0
                pg.mixer.music.play()
            if event.key==pg.K_LEFT:
                posicion_cancion +=1 
                numero_cancion +=1
                if numero_cancion>= len(canciones):
                    numero_cancion=0
        if play_song:
            if event.type==pg.KEYDOWN:          
                if event.key == pg.K_q:
                    b1 = True
                    if len (lista_notas_0)>0:
                        if (lista_notas_0[0][1]>430 and lista_notas_0[0][1]<550):
                            lista_notas_0.pop(0)
                            score_player_1+=10
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                        
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_w:
                    b2 = True
                    if len (lista_notas_1)>0:
                        if (lista_notas_1[0][1]>430 and lista_notas_1[0][1]<550):
                            lista_notas_1.pop(0)
                            score_player_1+=10
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                        
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_e:
                    b3 = True
                    if len (lista_notas_2)>0:
                        if (lista_notas_2[0][1]>430 and lista_notas_2[0][1]<550):
                            lista_notas_2.pop(0)
                            score_player_1+=10
                        else:
                        # print (lista_notas_0[0][1])
                            error.play()
                    else:
                        # print (lista_notas_0[0][1])
                        error.play()
                if event.key == pg.K_r:
                    b4 = True
                    if len (lista_notas_3)>0:
                        if (lista_notas_3[0][1]>430 and lista_notas_3[0][1]<550):
                            lista_notas_3.pop(0) 
                            score_player_2+=10
                        else:
                            error.play()
                    else:
                        error.play()
            if event.type==pg.KEYUP:
                if event.key == pg.K_q:
                    b1 = False 
                if event.key == pg.K_w:
                    b2 = False 
                if event.key == pg.K_e:
                    b3 = False 
                if event.key == pg.K_r:
                    b4 = False 

            if event.type==time_Music:
                numero=music_time()-centecimas
                if nota != "":
                    dibujo_nota= nota.split(';')
                    if int(dibujo_nota[0])-20<= int(numero):

                        if dibujo_nota[1] =="0\n":
                            lista_notas_0.append([150,0])
                        
                        if dibujo_nota[1] =="1\n":
                            lista_notas_1.append([250,0]) 
                        
                        if dibujo_nota[1] =="2\n":
                            lista_notas_2.append([350,0])
                            
                        if dibujo_nota[1] =="3\n":
                            lista_notas_3.append([450,0])
                        
                        nota=Partitura.readline()    
                    # print(nota)
                #print(int(dibujo_nota[0]))
               



while True:
    events()

    screen.fill("White")
    if play_song:
        
        screen.blit(fondo,posicion)
        screen.blit(boton1,posicion1)
        screen.blit(boton2,posicion2)
        screen.blit(boton3,posicion3)
        screen.blit(boton4,posicion4)

        if b1:
            screen.blit(boton1_p,posicion1)
        if b2:
            screen.blit(boton2_p,posicion2)
        if b3:
            screen.blit(boton3_p,posicion3)
        if b4:
            screen.blit(boton4_p,posicion4)

        if len (lista_notas_0)>0:
            for i in range(len(lista_notas_0)):
                screen.blit(nota1,lista_notas_0[i])
                lista_notas_0[i][1]+=5

        if len (lista_notas_1)>0:
            for i in range(len(lista_notas_1)):
                screen.blit(nota2,lista_notas_1[i])
                lista_notas_1[i][1]+=5
        if len (lista_notas_2)>0:
            for i in range(len(lista_notas_2)):
                screen.blit(nota3,lista_notas_2[i])
                lista_notas_2[i][1]+=5

        if len (lista_notas_3)>0:
            for i in range(len(lista_notas_3)):
                screen.blit(nota4,lista_notas_3[i])
                lista_notas_3[i][1]+=5
        music_time()
        text_score1=tex_font.render(str(score_player_1),True,'White')
        text_score2=tex_font.render(str(score_player_2),True,'White')
        screen.blit(barra_de_puntaje,(0,0))
        screen.blit(text_score1,(180,30))
        screen.blit(text_score2,(605,30))
        pg.display.update()

    
        if len(lista_notas_0) !=0:
            if lista_notas_0[0][1]>555:
                lista_notas_0.pop(0)
                error.play()
        
        if len(lista_notas_1) !=0:
            if lista_notas_1[0][1]>555:
                lista_notas_1.pop(0)
                error.play()
        
        if len(lista_notas_2) !=0:
            if lista_notas_2[0][1]>555:
                lista_notas_2.pop(0)
                error.play()
        
        if len(lista_notas_3) !=0:
            if lista_notas_3[0][1]>555:
                lista_notas_3.pop(0)
                error.play()
        play_song=(pg.mixer.music.get_busy())
    else:
        #dibujo menu 
        screen.blit(fondo_menu,(0,0))
        texto_cancion=tex_font.render(canciones[0],True,'Black')
        screen.blit(texto_cancion,[450,60])


        texto_cancion=tex_font.render(canciones[1],True,'Black')
        screen.blit(texto_cancion,[200*posicion_cancion,0])
        
        pg.display.update()


        
        

        
            
    clock.tick(60)
    # print (lista_notas_0)