from pygame import *
import sys

init()
mixer.init()

window = display.set_mode((1280, 720))

borboleta = image.load("borboletinha.png").convert_alpha()
borboleta = transform.scale(borboleta, (300, 300))

fonte = font.Font("LobsterTwo.ttf", 40)
texto = fonte.render("Uma borboleta!" , True , (0 , 0 ,0))

mixer.music.load("musica.mp3")
mixer.music.play(-1)

running = True
clock = time.Clock()

nuvem_x_inicial = 800
nuvem_x = nuvem_x_inicial
nuvem_y = 150
velocidade_nuvem = 100

sol_x = 150
sol_y = 150

while running :

    clock.tick(60)
    fill_color = (135, 237, 237)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    
    #uptade 

    dt = clock.get_time()/1000
    keys = key.get_pressed()

    # acoes continuas
    if keys[K_a]:
        sol_x = sol_x- 100 * dt
    elif keys[K_d]:
        sol_x = sol_x + 100 * dt
    elif keys[K_w]:
        sol_y = sol_y - 100 * dt
    elif keys[K_s]:
         sol_y = sol_y + 100 * dt

    if  426 <  sol_x  < 852:
        fill_color = (237, 135, 71)
    elif sol_x >  852:
        fill_color = (23, 14, 110)


    #ceu
    window.fill(fill_color) 

    # Chao
    draw.rect(window, (28, 133, 33), (0, 550, 1280, 170))

    # Sol
    draw.circle(window, (255, 255, 0), (sol_x, sol_y) , 50)

    # Raios
    draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x, (sol_y - 100)), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), (sol_x, (sol_y + 100)), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x - 100), sol_y), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x + 100), sol_y), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x - 70), (sol_y - 70)), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x + 70), (sol_y - 70)), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x - 70) , (sol_y + 70)), 8)
    draw.line(window, (255, 255, 0), (sol_x, sol_y), ((sol_x + 70), (sol_y + 70)), 8)

    # Casa
    draw.rect(window, (252, 3, 198), (330, 350, 200, 200))

    # Telhado
    draw.polygon(window, (71, 13, 61), [(330, 350), (530, 350), (430, 180)])

    # Porta
    draw.rect(window, (158, 90, 147), (370, 430, 60, 120))
    draw.circle(window, (0, 0, 0), (420, 490), 5)

    # Janela
    draw.rect(window, (0, 0, 139), (450, 440, 50, 70))

    # Arvore
    draw.rect(window, (130, 67, 20), (750, 400, 40, 150))
    draw.circle(window, (28, 133, 33), (770, 350), 80)

    # Nuvem -
    draw.circle(window, (255, 255, 255), (nuvem_x, nuvem_y), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 60, nuvem_y), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 100, nuvem_y), 50)
    draw.circle(window, (255, 255, 255), (nuvem_x + 160, nuvem_y), 50)  

    
    # Imagem - borboleta
    window.blit(borboleta, (900, 300))

    # texto 
    window.blit(texto, (900 , 270))


    #EXTRA - nuvem se mexer
    nuvem_x = nuvem_x + 2
    if nuvem_x == 1280:
         nuvem_x = nuvem_x * (-2)

    elif nuvem_x == 1:
        nuvem_x = nuvem_x * (2)


 
    display.update()