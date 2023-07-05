import pygame, sys
from settings import *
from class_character import Character
# from animation_settings import dic_animations_character
from class_platform import Platform
from animation_settings import *
import random
from class_fire import Enemy_fire
from class_enemy_phamton import Enemy_phantom
from class_time import Cronometro
from windows import Item
# --------------------------------------------

class Level_1:
    def __init__(self):
        pygame.init()
        #pantalla 
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.background =  pygame.transform.scale(pygame.image.load("src/resources/image/background.png"), SIZE_SCREEN)
        #plataforma
        self.platforms = Platform(lista_superficie)
        self.floor = self.platforms.rectangles[0]
        #personaje 
        self.character = Character(self.screen, self.platforms.rectangles)
        self.live = 3
        self.character_restart_game = self.character.rect
        #enemigos level 1
        self.sprite_phantom = pygame.sprite.Group()
        self.sprite_fire = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.character)
        #musica
        # pygame.mixer.music.load("src/resources/sound/sound_dificult_1.mp3")
        # pygame.mixer.music.set_volume(0.5)  # Ajusta el volumen de la música (opcional)
        self.music_level1 = pygame.mixer.Sound("src/resources/sound/sound_dificult_1.mp3")
        self.chanel_level1 = pygame.mixer.Channel(0)
        #Cronometro
        self.time = pygame.time.Clock()
        #evento bull
        #esta jugando 
        self.playing = False
        self.running = False
        self.is_game_over = False
        #fuente
        self.font_time = pygame.font.Font("src/resources/fonts/DS-DIGI.TTF", 80)
        self.font = pygame.font.Font("src/resources/fonts/Dark College.otf", 50)
        #cronometro
        self.cronometro = Cronometro(2)
        self.is_pause = False
        self.menu_pause = Item(menu_items, self.font)

    # --------------------------------------------------------------------------------------------------
    def play(self):
        self.is_pause = False
        self.GENERAR_EVENTO_PHANTOM = pygame.USEREVENT + 1
        pygame.time.set_timer(self.GENERAR_EVENTO_PHANTOM, 6000)
        #evento fire
        self.GENERAR_EVENTO_FIRE = pygame.USEREVENT + 2
        pygame.time.set_timer(self.GENERAR_EVENTO_FIRE, 6000)
        self.cronometro.start()
        self.running = True
        self.playing = True
        self.play_music()
        while self.running:
            self.time.tick(FPS)
            self.handle_events()
            self.update()
            self.render()



        self.return_opcion()

    # ------------------------------------------------------------------------------------------------
    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if not self.is_pause:
                        self.is_pause = True
                        self.pause_game()
                    else:
                        self.is_pause = False
                        self.resume_game()

            elif event.type == self.GENERAR_EVENTO_FIRE and not self.is_pause:
                for _ in range(random.randint(1, 5)):
                    direction = random.choice(["derecha", "izquierda", "arriba"])
                    velocidad = random.randint(2, 5)
                    fire = Enemy_fire(enemy_fire, direction , velocidad)
                    self.all_sprites.add(fire)
                    self.sprite_fire.add(fire)
                pygame.time.set_timer(self.GENERAR_EVENTO_FIRE, random.randint(5000, 10000))
                
            elif event.type == self.GENERAR_EVENTO_PHANTOM and not self.is_pause:
                self.generate_phantom()
                pygame.time.set_timer(self.GENERAR_EVENTO_PHANTOM, random.randint(5000, 10000))

            if self.is_pause:
                self.menu_pause.handle_event(event)
                if self.menu_pause.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.is_pause = False
                    self.resume_game()
                if self.menu_pause.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and not keys[pygame.K_a]:   #CAMINA DERECHA
            self.character.left = False
            self.character.state = "camina_derecha"
            self.character.speed_x = SPEED
        
        elif keys[pygame.K_a] and not keys[pygame.K_d]: #CAMINA IZQUIERDA
            self.character.left = True
            self.character.state = "camina_izquierda"
            self.character.speed_x = -SPEED

        elif keys[pygame.K_SPACE]:
            self.character.state = "salta"
        elif keys[pygame.K_q]:
            self.character.state = "ataque"
        else:
            self.character.state = "quieto"
    # ----------------------------------------------------------------------------------------------------------
    def update(self):
        self.kill_enemy()
        self.detectet_collide()
        self.all_sprites.update()
        self.cronometro.update()

    # -------------------------------------------------
    def render(self):
        self.screen.blit(self.background, ORIGIN)
        self.all_sprites.draw(self.screen)
        self.cronometro.draw(self.screen, self.font_time, (WIDTH // 2, 0), WHITE)
        txt = self.font.render("vidas: " + str(self.live), True, WHITE)
        self.screen.blit(txt, (1000, 20))
        if self.is_pause:
            self.menu_pause.draw(self.screen)
        pygame.display.flip()

    # --------------------------------------------------------------------------}
    def generate_phantom(self):
        if len(self.sprite_phantom) == 0:
            for _ in range(5):
                rectangle = random.choice(self.platforms.rectangles)
                location = (random.randrange(rectangle.left, rectangle.right), rectangle.top)
                phantom = Enemy_phantom(dic_enemy_phantom, location, rectangle.right, rectangle.left)
                self.all_sprites.add(phantom)
                self.sprite_phantom.add(phantom)
    # -----------------------------------------------------------------------------------
    def detectet_collide(self):
        phantom_collide = pygame.sprite.spritecollide(self.character, self.sprite_phantom, True)
        if len(phantom_collide) != 0:
            self.live -= 1
            if self.live == 0:
                self.character.kill()

        fire_collide = pygame.sprite.spritecollide(self.character, self.sprite_fire, True)
        if len(fire_collide) != 0:
            self.live -= 1
            if self.live == 0:
                self.character.kill()
                self.is_game_over = True
    # ---------------------------------------------------------------------------------------
    def kill_enemy(self):
        self.character.update_attack(self.all_sprites)
    # --------------------------------------------------------------------------
    def play_music(self):
        self.chanel_level1.play(self.music_level1, -1)  # Reproduce la música en bucle infinito

    def pause_music(self):
        self.chanel_level1.pause() # Pausa la reproducción de la música

    def resume_music(self):
        self.chanel_level1.unpause()  # Reanuda la reproducción de la música

    def stop_music(self):
        self.chanel_level1.stop()  # Detiene la reproducción de la música

    # ----------------------------------------------------------------------------------------
    def game_over(self):
        pass
    # -----------------------------------------------------------------------------------------
    def reset_game(self):
        self.live = 3
        self.sprite_phantom.empty()
        self.sprite_fire.empty()
        self.all_sprites.empty()
        self.all_sprites.add(self.character)
        self.cronometro.reset(2)
        self.is_game_over = False
        self.play_music()
        self.running = True
        self.resume_game()
        self.is_pause = False


    # --------------------------------------------------------------------------------------------------------------------
    def pause_game(self):
        self.pause_music()  
        self.cronometro.pause() 
        for sprite in self.all_sprites:
            sprite.stop()
    # ------------------------------------------------------------------------------------------------------------------------
    def resume_game(self):
        self.resume_music()  
        self.cronometro.resume()  
        for sprite in self.all_sprites:
            sprite.resume()

    def return_opcion(self):
        if not self.running:
            return "menu"



game = Level_1()
game.play()