import pygame
import sys

# Inicializar Pygame
pygame.init()

# Establecer el tamaño de la pantalla
width, height = 800, 600
pantalla = pygame.display.set_mode((width, height))

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Definir la clase MenuItem
class MenuItem:
    def __init__(self, text, position):
        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.position = position
        self.normal_color = WHITE
        self.hover_color = GREEN
        self.rendered_text = self.font.render(self.text, True, self.normal_color)
        self.rect = self.rendered_text.get_rect()
        self.rect.center = self.position

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_hovered(mouse_pos):
                self.rendered_text = self.font.render(self.text, True, self.hover_color)
            else:
                self.rendered_text = self.font.render(self.text, True, self.normal_color)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect)

# Definir la clase Menu
class Item:
    def __init__(self, items):
        self.items = []
        for item in items:
            menu_item = MenuItem(item, (width // 2, height // 2 + len(self.items) * 50))
            self.items.append(menu_item)

    def handle_event(self, event):
        for item in self.items:
            item.handle_event(event)

    def draw(self, surface):
        surface.fill(BLACK)
        for item in self.items:
            item.draw(surface)

# Crear el menú con los elementos deseados
menu_items = ["play", "exit"]
menu = Item(menu_items)
niveles = ["LEVEL 1", "LEVEL 2", "LEVEL 3", "salir"]
nivel = Item(niveles)
flag = False
# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        menu.handle_event(event)
        nivel.handle_event(event)
    if not flag:
        if menu.items[1].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
        if menu.items[0].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            flag = True
    
    if flag:
        if nivel.items[3].is_hovered(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            flag = False
    
    if not flag:
        menu.draw(pantalla)
    else:
        nivel.draw(pantalla)
    pygame.display.flip()  # Actualizar la pantalla


