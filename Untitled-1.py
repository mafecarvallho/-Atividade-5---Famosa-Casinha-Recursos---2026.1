
from pygame import *
import sys

init()

window = display.set_mode((1280 , 720))

window.fill((151, 209, 250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # desenhar a partir daqui - formas geometricas

    #Chao 
    draw.rect(window, (0, 200, 0) , (0, 550 , 1280, 170))

    #sol
    draw.circle(window, (255, 255, 0) , (150 , 120,) , 50)
    draw.line(window, (255, 255, 0), (150, 40), (150, 210), 7)  
    draw.line(window, (255, 255, 0), (70, 120), (240, 120), 7)  

    #casa
    draw.rect(window , (100, 100, 100) , (330 , 350 , 200, 200))

   #telhado
    draw.polygon(window, (255, 140 , 0), [(330, 350), (530,350), (430, 180)])

    #porta
    draw.rect(window, (139 , 69, 19), (350, 430 , 50, 120))
    draw.circle(window, (0 , 0 , 0), (360,490), 5)

    #janela
  

    #arvore
    draw.rect(window , (139 , 69 , 19), (750 , 400, 40, 150))
    draw.circle(window, (0, 200, 0) , (770, 350) , 80)


    # para desenhar a imagem

    display.update() 


