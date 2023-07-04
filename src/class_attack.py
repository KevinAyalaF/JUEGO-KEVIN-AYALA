import pygame
from settings import *

class Attack(pygame.sprite.Sprite):
    def __init__(self, image: str, position: tuple, piso, speed_y: int):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.midbottom = position
        self.floor = piso
        self.speed_y = speed_y

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom > self.floor:
            self.kill()
    def stop(self):
        pass