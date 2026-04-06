
from pygame import *
import sys

init()

imagem = image.load('C:\Users\G2610993\Documents\-Atividade-5---Famosa-Casinha-Recursos---2026.1\pngtree-flock-of-birds-silhouettes-flying-birds-clipart-png-image_5371927.png')

window = display.set_mode((1280 , 720))

window.fill((151, 209, 250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # desenhar a partir daqui - formas geometricas
    draw.rect(window , (100, 100, 100) , (300 , 300 , 200 ,250)), 
    draw.circle(window , (255, 242, 81), (150 , 100) , 50)
    draw.line( window , (255, 242, 81) , (200 , 200) , (100 , 100) , 5) 
    # para desenhar a imagem
    window.blit(imagem)
    display.update() 
