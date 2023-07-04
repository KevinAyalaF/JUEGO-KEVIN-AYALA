import pygame

# Definir la clase Cronometro
class Cronometro:
    def __init__(self, minutos, segundos=0):
        # self.font = pygame.font.Font(None, 40)
        self.minutos = minutos
        self.segundos = segundos
        self.total_segundos = (self.minutos * 60) + self.segundos
        self.start_time = pygame.time.get_ticks()
        self.is_finished = False

    def update(self):
        elapsed_time = pygame.time.get_ticks() - self.start_time
        remaining_time = max(0, self.total_segundos - elapsed_time // 1000)
        self.minutos = remaining_time // 60
        self.segundos = remaining_time % 60

        if self.minutos == 0 and self.segundos == 0:
            self.is_finished = True

    def get_time_text(self):
        return f"{self.minutos:02d}:{self.segundos:02d}"

    def draw(self, surface, font,  position: tuple, color):
        text = font.render(self.get_time_text(), True, color)
        rect_text = text.get_rect()
        rect_text.midtop = position
        surface.blit(text, rect_text)



