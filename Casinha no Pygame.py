
from pygame import *
import sys

init()

passarinhos_png = image.load(' ')

window = display.set_mode((1280 , 720))

window.fill((151, 209, 250))


while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # desenhar a partir daqui
    draw.rect(window , (100, 100, 100) , (300 , 300 , 200 ,250)), 
    draw.circle(window , (255, 242, 81), (150 , 100) , 50)
    draw.line( window , (255, 242, 81) , (200 , 200) , (100 , 100) , 5) 
    display.update() 
