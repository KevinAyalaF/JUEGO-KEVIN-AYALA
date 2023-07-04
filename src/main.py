import pygame, sys
from settings import *
from class_character import Character
# from animation_settings import dic_animations_character
from class_platform import Platform
from class_bull import Bull
from animation_settings import *
import random
from class_fire import Enemy_fire
from class_enemy_phamton import Enemy_phantom
from class_enemy_crab import Enemy_crab
from class_time import Cronometro
# -----------------------------------------------------
def generate_phantom(group_sprite: pygame.sprite.Sprite, sprite_phantom: pygame.sprite.Sprite, lista_superficie: list, count: int) -> None:
    if len(sprite_phantom) == 0:
        for _ in range(count):
            rectangulo = random.choice(lista_superficie)
            ubicacion = (random.randrange(rectangulo.left, rectangulo.right), rectangulo.top)
            phantom = Enemy_phantom(dic_enemy_phantom, ubicacion, rectangulo.right, rectangulo.left)
            group_sprite.add(phantom)
            sprite_phantom.add(phantom)
# -----------------------------------------------------------

def generate_crag(group_sprite: pygame.sprite.Sprite, sprite: pygame.sprite.Sprite, plataformas: list, count: int):
    if len(sprite) == 0:
        for _ in range(count):
            rectangulo = random.choice(plataformas[1:])
            ubicacion = (random.randrange(rectangulo.left, rectangulo.right), rectangulo.top + 5)
            crab = Enemy_crab(enemy_crag, ubicacion, attack, plataformas[0].top)
            group_sprite.add(crab)
            sprite.add(crab)


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
#toro
sprite_bull = pygame.sprite.Group()
GENERAR_BULL_EVENTO = pygame.USEREVENT + 1
pygame.time.set_timer(GENERAR_BULL_EVENTO, random.randint(5000, 20000))
a = pygame.Surface((10, 19))
b = a.get_rect()
#fuegito 
GENERAR_EVENTO_FIRE = pygame.USEREVENT + 2
pygame.time.set_timer(GENERAR_EVENTO_FIRE, 3000)

sprite_phantom = pygame.sprite.Group()
# fantom = Enemy_phantom(dic_enemy_phantom, (WIDTH // 2, piso.top))
# all_sprites.add(fantom)

sprite_crab = pygame.sprite.Group()
sprite_attack = pygame.sprite.Group()

# ----------------------------------------------------
cronometro = Cronometro(0, 10)
fuente = pygame.font.Font(None, 80)

x = 0

while True:
    time.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif evento.type == pygame.K_q:
            personaje.attack()


        elif evento.type == GENERAR_BULL_EVENTO:
            nuevo_bull = Bull(dic_bull, piso)
            nuevo_bull.sound.play()
            all_sprites.add(nuevo_bull)
            pygame.time.set_timer(GENERAR_BULL_EVENTO, random.randint(5000, 20000))


        elif evento.type == GENERAR_EVENTO_FIRE:
            for _ in range(random.randint(1, 5)):
                direction = random.choice(["derecha", "izquierda", "arriba"])
                velocidad = random.randint(2, 5)
                fire = Enemy_fire(enemy_fire, direction , velocidad)
                all_sprites.add(fire)
            pygame.time.set_timer(GENERAR_EVENTO_FIRE, random.randint(5000, 10000))


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
    # elif keys[pygame.K_q]:
    #     personaje.state = "ataque"

    else:
        personaje.state = "quieto"

    generate_phantom(all_sprites, sprite_phantom, lista_plataformas.rectangles, 10)
    generate_crag(all_sprites, sprite_crab, lista_plataformas.rectangles, 4)

    pantalla.blit(fondo, ORIGIN)
    all_sprites.update()
    all_sprites.draw(pantalla)
    pygame.draw.rect(pantalla, ORANGE, personaje.rect, 3)
    pygame.draw.rect(pantalla, ORANGE, personaje.rectbottom, 3)
    
    
    cronometro.update()
    cronometro.draw(pantalla, fuente, (WIDTH // 2, 0), WHITE)
    if x % 200 == 0:
        for crag in sprite_crab:
            crag.attack(all_sprites, sprite_attack)
    x += 1


    
    pygame.display.flip()

