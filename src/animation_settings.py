import pygame




#################################################
def girar_imagenes(lista: list, flip_x: bool=True, flip_y: bool=False) -> list:
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

SIZE_CHARACTER = (34, 56)

# -----------LISTA MOVIMIENTO-------------
# *************************************** PERSONAJE **************************************
#QUIETO DERECHA

character_idle_right = [pygame.image.load("src/resources/image/personaje/idle (1).png"),
                    pygame.image.load("src/resources/image/personaje/idle (2).png"),
                    pygame.image.load("src/resources/image/personaje/idle (3).png"),
                    pygame.image.load("src/resources/image/personaje/idle (4).png"),
                    pygame.image.load("src/resources/image/personaje/idle (5).png"),
                    pygame.image.load("src/resources/image/personaje/idle (6).png"),
                    pygame.image.load("src/resources/image/personaje/idle (7).png"),
                    pygame.image.load("src/resources/image/personaje/idle (8).png"),
                    pygame.image.load("src/resources/image/personaje/idle (9).png"),
                    pygame.image.load("src/resources/image/personaje/idle (10).png"),
                    pygame.image.load("src/resources/image/personaje/idle (11).png"),
                    pygame.image.load("src/resources/image/personaje/idle (12).png"),
                    pygame.image.load("src/resources/image/personaje/idle (13).png"),
                    pygame.image.load("src/resources/image/personaje/idle (14).png"),
                    pygame.image.load("src/resources/image/personaje/idle (15).png")
]
#QUIETO IZQUIERDA
character_idle_left = girar_imagenes(character_idle_right)
#CAMINAR DERECHA
character_walk_right = [pygame.image.load("src/resources/image/personaje/walk (1).png"),
                    pygame.image.load("src/resources/image/personaje/walk (2).png"),
                    pygame.image.load("src/resources/image/personaje/walk (3).png"),
                    pygame.image.load("src/resources/image/personaje/walk (4).png"),
                    pygame.image.load("src/resources/image/personaje/walk (5).png"),
                    pygame.image.load("src/resources/image/personaje/walk (6).png")
]
#CAMINA IZQUIERDA
character_walk_left = girar_imagenes(character_walk_right)
#SALTAR DERECHA
character_jump_right = [pygame.image.load("src/resources/image/personaje/jump (1).png"),
                    pygame.image.load("src/resources/image/personaje/jump (2).png"),
                    pygame.image.load("src/resources/image/personaje/jump (3).png"),
                    pygame.image.load("src/resources/image/personaje/jump (4).png"),
                    pygame.image.load("src/resources/image/personaje/jump (5).png"),
                    pygame.image.load("src/resources/image/personaje/jump (6).png")
]
# SALTAR IZQUIERDA
character_jump_left = girar_imagenes(character_jump_right)
#ATAQUE DE DERECHA
character_attack_right = [pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (1).png"), (45, 56)),
                        pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (2).png"), (107, 56)),
                        pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (3).png"), (108, 56)),
                        pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (4).png"), (68, 56)),
                        pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (5).png"), (72, 56)),
                        pygame.transform.scale(pygame.image.load("src/resources/image/personaje/attack (6).png"), (54, 56))
]
#ATAQUE IZQUIERDA
character_attack_left = girar_imagenes(character_attack_right)
#CAMINAR CON ESCUDO DE DERECHA
#MUERTE DERECHA
character_death_right = [pygame.image.load("src/resources/image/personaje/death (1).png"),
                    pygame.image.load("src/resources/image/personaje/death (2).png"),
                    pygame.image.load("src/resources/image/personaje/death (3).png"),
                    pygame.image.load("src/resources/image/personaje/death (4).png"),
                    pygame.image.load("src/resources/image/personaje/death (5).png"),
                    pygame.image.load("src/resources/image/personaje/death (6).png"),
                    pygame.image.load("src/resources/image/personaje/death (7).png")
]
#MUERTE IZQUIERDA
character_death_left = girar_imagenes(character_death_right)

#DICCIONARIO PERSONAJE
dic_animations_character = {}
dic_animations_character["quieto_derecha"] = character_idle_right
dic_animations_character["quieto_izquierda"] = character_idle_left
dic_animations_character["camina_derecha"] = character_walk_right
dic_animations_character["camina_izquierda"] = character_walk_left
dic_animations_character["salta_derecha"] = character_jump_right
dic_animations_character["salta_izquierda"] = character_jump_left
dic_animations_character["ataca_derecha"] = character_attack_right
dic_animations_character["ataca_izquierda"] = character_attack_left
dic_animations_character["muere_derecha"] = character_death_right
dic_animations_character["muere_izquierda"] = character_death_left

# ***************************************************************************************************

# -------------------ENEMIGOS-------------------------
#ENEMIGO PHAMTON CAMINA DERECHA--------------------------------------
enemy_phantom_walk_right = [pygame.image.load("src/resources/image/enemigos/phantom_walk (1).png"),
                            pygame.image.load("src/resources/image/enemigos/phantom_walk (2).png"),
                            pygame.image.load("src/resources/image/enemigos/phantom_walk (3).png"),
                            pygame.image.load("src/resources/image/enemigos/phantom_walk (4).png")
]
# ENEMIGO PHAMTON CAMINA IZQUIERDA
enemy_phantom_walk_left = girar_imagenes(enemy_phantom_walk_right)
#ENEMIGO PHAMTON MUERE
enemy_phantom_death = [pygame.image.load("src/resources/image/enemigos/phantom_death (1).png"),
                        pygame.image.load("src/resources/image/enemigos/phantom_death (2).png")
]
#DICCIONARIO ENEMIGO PHANTOM
dic_enemy_phantom = {}
dic_enemy_phantom["camina_derecha"] = enemy_phantom_walk_right
dic_enemy_phantom["camina_izquierda"] = enemy_phantom_walk_left
# dic_enemy_phantom["muerte"] = enemy_phantom_death
#ENEMIGO TORO
bull_attack_left = [pygame.transform.scale_by(pygame.image.load("src/resources/image/enemigos/bull (5).png"), 0.7),
                    pygame.transform.scale_by(pygame.image.load("src/resources/image/enemigos/bull (6).png"), 0.7),
                    pygame.transform.scale_by(pygame.image.load("src/resources/image/enemigos/bull (7).png"), 0.7),
                    pygame.transform.scale_by(pygame.image.load("src/resources/image/enemigos/bull (8).png"), 0.7)
]
bull_attack_right = girar_imagenes(bull_attack_left)

dic_bull = {}
dic_bull["bull_derecha"] = bull_attack_right
dic_bull["bull_izquierda"] = bull_attack_left

#ENEMIGO CRAB MOVIMIENTO-----------------------
enemy_crag = [pygame.image.load("src/resources/image/enemigos/crab (1).png"),
            pygame.image.load("src/resources/image/enemigos/crab (2).png"),
            pygame.image.load("src/resources/image/enemigos/crab (3).png"),
            pygame.image.load("src/resources/image/enemigos/crab (4).png")
]
#ATAQUE ENEMIGO (CUALQUIER ENEMIGO PUEDE USARLO)------------------
# enemy_attack = [pygame.image.load("src/resources/image/ataques/fire (1).png"),
#                 pygame.image.load("src/resources/image/ataques/fire (2).png"),
#                 pygame.image.load("src/resources/image/ataques/fire (3).png")
# ]
attack = pygame.transform.scale_by(pygame.image.load("src/resources/image/ataques/fire (3).png"), 0.4)
#EXPLOSION ATAQUE-----------------------
explotion_attack = [pygame.image.load("src/resources/image/ataques/burst (1).png"),
                    pygame.image.load("src/resources/image/ataques/burst (1).png"),
                    pygame.image.load("src/resources/image/ataques/burst (2).png"),
                    pygame.image.load("src/resources/image/ataques/burst (3).png"),
                    pygame.image.load("src/resources/image/ataques/burst (4).png"),
                    pygame.image.load("src/resources/image/ataques/burst (5).png"),
                    pygame.image.load("src/resources/image/ataques/burst (6).png"),
                    pygame.image.load("src/resources/image/ataques/burst (7).png"),
                    pygame.image.load("src/resources/image/ataques/burst (8).png")
]

# enemigo fire
enemy_fire = pygame.image.load("src/resources/image/enemigos/fire.png")