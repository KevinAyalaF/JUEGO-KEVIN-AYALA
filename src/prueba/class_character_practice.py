import pygame

def obtener_rectangulo(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 20)
    return diccionario



class Personaje:
    def __init__(self, animaciones: dict, posicion_inicial: tuple):
        #CONFECCION
        # self.ancho = tamaño[0]
        # self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        #RECTANGULOS
        rectangulo = self.animaciones["quieto_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(rectangulo)
        self.velocidad = 5
        self.posicion_actual = "quieto_derecha"
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.desplazamiento_y = 0
        self.esta_saltado = False
        self.lado_salta = "salta_derecha"

    # def reescalar_animaciones():
    #     pass


    def animar(self, pantalla, que_animacion: str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1


    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def aplicar_gravedad(self, pantalla, piso, lado):
        if self.esta_saltado:
            self.animar(pantalla, lado)

            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y


            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.esta_saltado = False
            self.lados["main"].bottom = piso["main"].top


    def update(self, pantalla, piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltado:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad)
                self.posicion_actual = "quieto_derecha"
                self.lado_salta = "salta_derecha"
            case "izquierda":
                if not self.esta_saltado:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(-self.velocidad)
                self.posicion_actual = "quieto_izquierda"
                self.lado_salta = "salta_izquierda"
            case "salta":
                if not self.esta_saltado:
                    self.esta_saltado = True
                    self.desplazamiento_y = self.potencia_salto
            case "ataca":
                self.animar(pantalla, "ataca_derecha")
            case "quieto":
                if not self.esta_saltado:
                    self.animar(pantalla, self.posicion_actual)
        self.aplicar_gravedad(pantalla, piso, self.lado_salta)
