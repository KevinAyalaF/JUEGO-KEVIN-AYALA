import pygame, sys
from config import *
from pygame.locals import *
from animacion import *
from class_character_practice import *
from modo import *



#########################################
def actualizar_pantalla(pantalla, personaje, fondo, lados_piso):

    pantalla.blit(fondo, ORIGIN)
    personaje.update(pantalla, lados_piso)


pygame.init()

screen = pygame.display.set_mode(SIZE_SCREEN)

fondo = pygame.transform.scale(pygame.image.load(r"src\resources\image\background.png"), SIZE_SCREEN)
# rect_fondo = fondo.get_rect()
# rect_fondo.topleft = ORIGIN

icono = pygame.image.load("src/resources/image/icono-espada.png")
pygame.display.set_icon(icono)

pygame.mixer.music.load(r"src\resources\sound\sound_dificult_3.mp3")
pygame.mixer.music.play()


time = pygame.time.Clock()


#ANIMACIONES PERSONAJE
posicion_inicial = (WIDTH // 2, HEIGHT - 100)
diccionario_animaciones_personaje = {}
diccionario_animaciones_personaje["quieto_derecha"] = player_idle_right
diccionario_animaciones_personaje["quieto_izquierda"] = player_idle_left
diccionario_animaciones_personaje["camina_derecha"] = player_walk_right
diccionario_animaciones_personaje["camina_izquierda"] = player_walk_left
diccionario_animaciones_personaje["salta_derecha"] = player_jump_right
diccionario_animaciones_personaje["salta_izquierda"] = player_jump_left
diccionario_animaciones_personaje["ataca_derecha"] = player_attack_right
diccionario_animaciones_personaje["ataca_izquierda"] = player_attack_left
diccionario_animaciones_personaje["guardia_camina_con_escudo_derecha"] = player_guard_walk_right
diccionario_animaciones_personaje["guardia_camina_con_escudo_izquierda"] = player_guard_walk_left
diccionario_animaciones_personaje["guardia_camina_con_escudo_arriba_derecha"] = player_guard_up_walk_right
diccionario_animaciones_personaje["guardia_camina_con_escudo_arriba_izquierda"] = player_guard_project_up_left
diccionario_animaciones_personaje["guardia_recibe_impacto_escudo_derecha"] = player_guard_project_right
diccionario_animaciones_personaje["guardia_recibe_impacto_escudo_izquierda"] = player_guard_project_left
diccionario_animaciones_personaje["guardia_recibe_impacto_con_escudo_arriba_derecha"] = player_guard_project_up_right
diccionario_animaciones_personaje["guardia_recibe_impacto_con_escudo_arriba_izquierda"] = player_guard_project_up_left
diccionario_animaciones_personaje["muere_derecha"] = player_death_right
diccionario_animaciones_personaje["muere_izquierda"] = player_death_left



mi_personaje = Personaje(diccionario_animaciones_personaje, posicion_inicial)



piso = pygame.Rect(0, 0, WIDTH, 20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulo(piso)

aux = 1
con = 0

while True:
    time.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
            cambiar_modo()


    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_SPACE]:
        mi_personaje.que_hace = "salta"
    elif keys[pygame.K_q]:
        mi_personaje.que_hace = "ataca"
    else:
        mi_personaje.que_hace = "quieto"


    actualizar_pantalla(screen, mi_personaje, fondo, lados_piso)
    if get_modo():
        for lado in lados_piso:
            pygame.draw.rect(screen, "green", lados_piso[lado], 2)
        for lado in mi_personaje.lados:
            pygame.draw.rect(screen, "blue", mi_personaje.lados[lado], 2)




    # screen.blit(fondo, ORIGIN)
    pygame.display.flip()
