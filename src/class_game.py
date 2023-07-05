import pygame, sys
from windows import *
from settings import *
from windows import *

class Menu:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        self.background = pygame.transform.scale(pygame.image.load("src/resources/image/menu/screen_main_menu.jpg"), SIZE_SCREEN)
        self.font = pygame.font.Font("src/resources/fonts/Dark College.otf", 60)
        self.playing = True
        self.time = pygame.time.Clock()
        self.running = False
        self.go_levels= False
        self.play_level_1 = False
        self.font = pygame.font.Font("src/resources/fonts/Dark College.otf", 60)
        self.menu = Item(menu_items, self.font)
        self.music = pygame.mixer.Sound("src/resources/sound/sound_menu.mp3")
        self.chanel = pygame.mixer.Channel(0)
        self.chanel.set_volume(0.5)
        #niveles
        self.levels = Item(level_item, self.font)


    def play(self):
        self.running = True
        self.play_music()
        while self.running:
            self.time.tick(FPS)
            self.handle_event()
            self.render()
        self.return_opcion()


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not self.go_levels:
                self.menu.handle_event(event)
                if self.menu.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.go_levels = True
                elif self.menu.items[-1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    sys.exit()
                self.levels.handle_event(event)
            else:
                self.levels.handle_event(event)
                if self.levels.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    print("1")
                elif self.levels.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    print("2")
                elif self.levels.items[2].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    print("3")
                elif self.levels.items[3].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.go_levels = False

    def return_level(self):
        pass

    def render(self):
        self.screen.blit(self.background, ORIGIN)
        if not self.go_levels:
            self.menu.draw(self.screen)
        else:
            self.levels.draw(self.screen)

        pygame.display.flip()

    def play_music(self):
        self.chanel.play(self.music, -1)  # Reproduce la música en bucle infinito

    def pause_music(self):
        self.chanel.pause() # Pausa la reproducción de la música

    def resume_music(self):
        self.chanel.unpause()  # Reanuda la reproducción de la música

    def stop_music(self):
        self.chanel.stop()  # Detiene la reproducción de la música

menu = Menu()
menu.play()
