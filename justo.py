import pygame as pg 
from sys import exit
pg.init()
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
song ='smooth'
pg.mixer.music.load(f"./audios/{song}.mp3") 
data = open(f"data_{song}.txt", "a")
button1 =False
button2 =False
button3 =False
#Funcion de eventos#
def events():
    global button1 , button2 , button3
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                button1 =True
                data.write(f'{current_time};0\n')
            if event.key == pg.K_DOWN:
                button2 =True
                data.write(f'{current_time};1\n')
            if event.key == pg.K_RIGHT:
                button3 =True
                data.write(f'{current_time};2\n')
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                button1 =False
            if event.key == pg.K_DOWN:
                button2 =False
            if event.key == pg.K_RIGHT:
                button3 =False
pg.mixer.music.play()
while True:
    events()

    screen.fill("White")
    pg.draw.circle(screen,'Red',(100,500),50)
    pg.draw.circle(screen,'Red',(300,500),50)
    pg.draw.circle(screen,'Red',(500,500),50)

    if button1:
        pg.draw.circle(screen,'#C71EE8',(100,500),50)
    if button2:
        pg.draw.circle(screen,'#F28C1F',(300,500),50)
    if button3:
        pg.draw.circle(screen,'#561FF2',(500,500),50)
    pg.display.update()

    my_time()
    if not pg.mixer.music.get_busy():
        data.close()
        pg.quit()
        exit()
        
    clock.tick(60)