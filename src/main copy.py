import pygame, sys
from settings import *
from class_character_copy import Character
from class_platform import Platform


# -------------------------------------------------------------
pygame.init()

pantalla = pygame.display.set_mode(SIZE_SCREEN)

fondo = pygame.image.load(r"src\resources\image\background.png")
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)

lista_plataformas = Platform(lista_superficie)
personaje = Character(pantalla, lista_plataformas.rectangles)

time = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(personaje)

music = pygame.mixer.music.load(r"src\resources\sound\sound_dificult_2.mp3")
pygame.mixer.music.play()

#piso
piso = lista_plataformas.rectangles[0]


posicion = (300, 300)

image_r = pygame.image.load("src/resources/image/personaje/attack (3).png").convert_alpha()
rect_image_1 = image_r.get_rect()
rect_image_1.midright = posicion

image_l = pygame.transform.flip(image_r, True, False)
rect_image_2 = image_r.get_rect()
rect_image_2.midleft = posicion



while True:
    time.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] and not keys[pygame.K_a]:   #CAMINA DERECHA
        personaje.left = False
        personaje.state = "camina_derecha"
        personaje.speed_x = SPEED
    
    elif keys[pygame.K_a] and not keys[pygame.K_d]: #CAMINA IZQUIERDA
        personaje.left = True
        personaje.state = "camina_izquierda"
        personaje.speed_x = -SPEED

    elif keys[pygame.K_SPACE]:
        personaje.state = "salta"
    elif keys[pygame.K_q]:
        personaje.state = "ataque"

    else:
        personaje.state = "quieto"
        personaje.speed_x = 0

    pantalla.blit(fondo, ORIGIN)
    all_sprites.update()
    all_sprites.draw(pantalla)


    pantalla.blit(image_r, rect_image_1)
    pantalla.blit(image_l, rect_image_2)


    pygame.draw.rect(pantalla, RED, personaje.rect, 3)
    
    pygame.display.flip()

