import pygame
import random

pygame.init()


x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Em busca do sapato perdido')

bg = pygame.image.load('images/bg.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x,y))

shoes = pygame.image.load('images/sapato.png').convert_alpha()
shoes = pygame.transform.scale(shoes, (50,50))

princess = pygame.image.load('images/princesa.png').convert_alpha()
princess = pygame.transform.scale(princess, (50,50))

glitter = pygame.image.load('images/glt.jpg').convert_alpha()
glitter = pygame.transform.scale(glitter, (25,25))

pos_shoes_x= 500
pos_shoes_y= 360

pos_princess_x= 200
pos_princess_y= 300

vel_glitter_x = 0
pos_glitter_x = 200
pos_glitter_y = 300

pontos = 10

triggered = False

rodando = True

#fonte para mostrar os pontos

#definição dos rects
player_rect = princess.get_rect()
shoes_rect = shoes.get_rect()
glitter_rect = glitter.get_rect()

#Funções

def respawn():
    x = 1350
    y = random.randint(1,640)
    return[x,y]

def respawn_glitter():
    triggered = False
    respawn_glitter_x = pos_princess_x
    respawn_glitter_y = pos_princess_y
    vel_glitter_x = 0
    return [respawn_glitter_x, respawn_glitter_y, triggered, vel_glitter_x]

def colisions():
    global pontos
    if player_rect.colliderect(shoes_rect) or shoes_rect.x ==60:
        pontos -= 1 
        return True
    elif glitter_rect.colliderect(shoes_rect):
        pontos +=1
        return True
    else:
        return False

while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0,0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) #cria background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    #teclas

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_princess_y > 1:
        pos_princess_y -= 1
        if not triggered:
            pos_glitter_y -= 1

    if tecla[pygame.K_DOWN] and pos_princess_y < 665:
        pos_princess_y += 1

        if not triggered:
            pos_glitter_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_glitter_x = 2

    if pontos == -1:
        rodando = False

    #respawn

    if pos_shoes_x == 50:
        pos_shoes_x = respawn()[0]
        pos_shoes_y = respawn()[1]

    if pos_glitter_x == 1300:
        pos_glitter_x, pos_glitter_y, triggered, vel_glitter_x = respawn_glitter()

    if pos_shoes_x == 50 or colisions():
        pos_shoes_x = respawn()[0]
        pos_shoes_y = respawn()[1]    

    #posição rect

    player_rect.y = pos_princess_y
    player_rect.x = pos_princess_x

    player_rect.y = pos_glitter_y
    player_rect.x = pos_glitter_x

    player_rect.y = pos_shoes_y
    player_rect.x = pos_shoes_x

    #movimento
    x -= 2
    pos_shoes_x -= 1

    pos_glitter_x += vel_glitter_x

    pygame.draw.rect(screen, (255, 0, 0), player_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), shoes_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), glitter_rect, 4)

    #imagens
    screen.blit(shoes, (pos_shoes_x, pos_shoes_y))
    screen.blit(glitter, (pos_glitter_x, pos_glitter_y))
    screen.blit(princess, (pos_princess_x, pos_princess_y))


    print(pontos)

    pygame.display.update()

