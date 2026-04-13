from pygame import *
import sys

init()
mixer.init()

window = display.set_mode((1280, 720))

# definir variavel


#borboleta = image.load("borboletinha.png").convert_alpha()
#borboleta = transform.scale(borboleta, (300, 300))

#fonte = font.Font("LobsterTwo.ttf", 40)
#texto = fonte.render("Uma borboleta!" , True , (0 , 0 ,0))

#mixer.music.load("musica.mp3")
#mixer.music.play(-1)

running = True
clock = time.Clock()

# Numevm - extra  

nuvem_x_inicial = 800
nuvem_x = nuvem_x_inicial
nuvem_y = 150

sol_x = 150

ceu = (151, 209, 250)


while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        if ev.type == KEYDOWN:  
            tecla = ev.key 
            if tecla == K_SPACE: 
                ceu = (237, 145, 59)

            
            

    # update
    dt = clock.get_time()/1000
    
    #ceu

    window.fill(ceu)
    

    # Chao
    draw.rect(window, (28, 133, 33), (0, 550, 1280, 170))

    # Sol
    draw.circle(window, (255, 255, 0), (sol_x, 150), 50)

    # Raios
    draw.line(window, (255, 255, 0), (150, 150), (150, 50), 8)
    draw.line(window, (255, 255, 0), (150, 150), (150, 250), 8)
    draw.line(window, (255, 255, 0), (150, 150), (50, 150), 8)
    draw.line(window, (255, 255, 0), (150, 150), (250, 150), 8)
    draw.line(window, (255, 255, 0), (150, 150), (80, 80), 8)
    draw.line(window, (255, 255, 0), (150, 150), (220, 80), 8)
    draw.line(window, (255, 255, 0), (150, 150), (80, 220), 8)
    draw.line(window, (255, 255, 0), (150, 150), (220, 220), 8)

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
    #window.blit(borboleta, (900, 300))

    # texto 
    #window.blit(texto, (900 , 270))

    #EXTRA - nuvem se mexer
    keys = key.get_pressed()

    if keys[K_d]:   
        nuvem_x = nuvem_x + 100 * dt
    elif keys[K_a]:
         nuvem_x = nuvem_x - 100 * dt
    


    if nuvem_x > 1280:
        nuvem_x = nuvem_x_inicial


    display.update() 