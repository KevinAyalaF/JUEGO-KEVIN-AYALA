import pygame
# from pygame.sprite import _Group
from animation_settings import *
from settings import *

class Character(pygame.sprite.Sprite):
    def __init__(self, screen, list_platform):
        super().__init__()
        #Imagenes del personaje
        self.animations = dic_animations_character
        self.image = None
        #Plataformas
        self.plataforms = list_platform
        self.floor = self.plataforms[0].top
        #Rectagunlo del personaje
        self.rect = self.animations["quieto_derecha"][0].get_rect()
        self.rect.midbottom = (WIDTH // 2, self.floor)
        self.rectbottom = pygame.Rect(self.rect.left, self.rect.bottom - 15, self.rect.width, 15)
        #velocidad dezplamiento
        self.speed_x = 0
        self.displacement_y = 0
        #Salto
        self.gravity = 1
        # self.limit_fall = 15
        self.jumping = False
        self.fall = False
        #Direccion animacion
        self.left = False
        #Ataque
        self.stroke = False
        #Animacion
        self.state = "quieto"
        self.what_animation = "quieto_derecha"
        #Indice imagen
        self.step_counter = 0
        #Pantalla
        self.screen = screen
        #ataque
        self.count = 0

        
    #Animaciones
    def animate(self, animation):
        animations = self.animations[animation]  #Lista de Animaciones
        tam = len(animations)
        if self.step_counter >= tam:   #Si el contador es mayor al tamaño de la lista se reinicia el contador a 0
            self.step_counter = 0
        self.image = animations[int(self.step_counter)]
        self.step_counter += 0.1

    #Movimiento
    def move(self):
        if self.speed_x > 0 and self.rect.right < pygame.display.get_surface().get_width():  # Movimiento hacia la derecha
            self.rectbottom.x +=  self.speed_x  #Se mueve mientra no supere los limete de la pantalla
            self.rect.x += self.speed_x
        elif self.speed_x < 0 and self.rect.left > 0:  # Movimiento hacia la izquierda
            self.rectbottom.x +=  self.speed_x
            self.rect.x += self.speed_x

    #animacion muerte
    def animate_death(self):
        pass

    def jump(self):
        if self.jumping or self.fall:
            self.rect.y += self.displacement_y
            self.rectbottom.y += self.displacement_y
            self.displacement_y += self.gravity

        for platform in self.plataforms:
            if self.rectbottom.colliderect(platform) and self.displacement_y > 0:
                self.jumping = False
                self.fall = False
                self.displacement_y = 0
                self.rect.bottom = platform.top
                self.rectbottom.bottom = platform.top
                break
            else:
                self.fall = True
            
    #Ataque
    def attack(self):
        pass
    
    #Detener animaciones y movimientos
    def stop(self):
        pass
    #MOVIMIENTOS
    def update(self):
        match(self.state):
            #DERECHA-------
            case "camina_derecha":
                if not self.jumping:
                    self.what_animation = "camina_derecha"
                self.move()
            #IZQUIERDA----------------------------
            case "camina_izquierda":
                if not self.jumping:
                    self.what_animation = "camina_izquierda"
                self.move()
            #--------------------------------------------------------------------------
            case "salta":
                if not self.jumping:
                    self.jumping = True
                    self.displacement_y = -15
            # case "ataque":
            #     if self.left:
            #         self.what_animation = "ataca_izquierda"
            #     else:
            #         self.what_animation = "ataca_derecha"
            #Animacion cuando esta quieto
            case "quieto":
                if not self.jumping:
                    if self.left:
                        self.what_animation = "quieto_izquierda"
                    else:
                        self.what_animation = "quieto_derecha"

        if self.jumping:   #Mientra esta saltando se carga las animaciones
            if self.left:
                self.what_animation = "salta_izquierda"
            else:
                self.what_animation = "salta_derecha"

        self.animate(self.what_animation)
        self.jump()
            
