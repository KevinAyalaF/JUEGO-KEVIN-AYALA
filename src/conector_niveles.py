import pygame, sys
from class_game import Menu
from class_level1 import Level_1
from class_level2 import Level_2
from class_level3 import Level_3

class LevelConnector:
    def __init__(self):
        pygame.init()
        self.levels = {
            "menu": Menu(),
            "level_1": Level_1(),
            "level_2": Level_2(),
            "level_3": Level_3()
        }
        self.current_level = "menu"
        self.next_level = None
        self.running = True

    def run(self):
        while self.running:
            if self.next_level is not None:
                self.current_level = self.next_level
                self.next_level = None

            next_level = self.levels[self.current_level].play()

            if next_level == "exit":
                self.running = False
            else:
                self.next_level = next_level

        pygame.quit()
        sys.exit()

game = LevelConnector()
game.run()
