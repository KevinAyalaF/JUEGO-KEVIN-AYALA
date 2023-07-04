import pygame




#################################################
def girar_imagenes(lista: list, flip_x: bool=True, flip_y: bool=False) -> list:
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada


# -----------LISTA MOVIMIENTO-------------
# *************************************** PERSONAJE **************************************
#QUIETO DERECHA
player_idle_right = [pygame.image.load("src/resources/image/personaje/idle (1).png"),
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
player_idle_left = girar_imagenes(player_idle_right)
#CAMINAR DERECHA
player_walk_right = [pygame.image.load("src/resources/image/personaje/walk (1).png"),
                    pygame.image.load("src/resources/image/personaje/walk (2).png"),
                    pygame.image.load("src/resources/image/personaje/walk (3).png"),
                    pygame.image.load("src/resources/image/personaje/walk (4).png"),
                    pygame.image.load("src/resources/image/personaje/walk (5).png"),
                    pygame.image.load("src/resources/image/personaje/walk (6).png")
]
#CAMINA IZQUIERDA
player_walk_left = girar_imagenes(player_walk_right)
#SALTAR DERECHA
player_jump_right = [pygame.image.load("src/resources/image/personaje/jump (1).png"),
                    pygame.image.load("src/resources/image/personaje/jump (2).png"),
                    pygame.image.load("src/resources/image/personaje/jump (3).png"),
                    pygame.image.load("src/resources/image/personaje/jump (4).png"),
                    pygame.image.load("src/resources/image/personaje/jump (5).png"),
                    pygame.image.load("src/resources/image/personaje/jump (6).png")
]
# SALTAR IZQUIERDA
player_jump_left = girar_imagenes(player_jump_right)
#ATAQUE DE DERECHA
player_attack_right = [pygame.image.load("src/resources/image/personaje/attack (1).png"),
                        pygame.image.load("src/resources/image/personaje/attack (2).png"),
                        pygame.image.load("src/resources/image/personaje/attack (3).png"),
                        pygame.image.load("src/resources/image/personaje/attack (4).png"),
                        pygame.image.load("src/resources/image/personaje/attack (5).png"),
                        pygame.image.load("src/resources/image/personaje/attack (6).png"),
]
#ATAQUE IZQUIERDA
player_attack_left = girar_imagenes(player_attack_right)
#CAMINAR CON ESCUDO DE DERECHA
player_guard_walk_right = [pygame.image.load("src/resources/image/personaje/guard_walk (1).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (2).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (3).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (4).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (5).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (6).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (7).png"),
                        pygame.image.load("src/resources/image/personaje/guard_walk (8).png")
]
#CAMINAR CON ESCUDO DE IZQUIERDA
player_guard_walk_left = girar_imagenes(player_guard_walk_right)
#CAMINAR CON ESCUDO DE DERECHA PROTEGIENDOSE DE ARRIBA
player_guard_up_walk_right = [pygame.image.load("src/resources/image/personaje/guard_up_walk (1).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (2).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (3).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (4).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (5).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (6).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (7).png"),
                            pygame.image.load("src/resources/image/personaje/guard_up_walk (8).png")
]
#CAMINAR CON ESCUDO DE IZQUIERDA PROTEGIENDOSE DE ARRIBA
player_guard_up_walk_left = girar_imagenes(player_guard_up_walk_right)
#IMPACTO CON ESCUDO DE DERECHA
player_guard_project_right = [pygame.image.load("src/resources/image/personaje/guard_protects (1).png"),
                            pygame.image.load("src/resources/image/personaje/guard_protects (2).png"),
                            pygame.image.load("src/resources/image/personaje/guard_protects (3).png"),
                            pygame.image.load("src/resources/image/personaje/guard_protects (4).png")
]
#IMPACTO CON ESCUDO DE IZQUIERDA
player_guard_project_left = girar_imagenes(player_guard_project_right)
#IMPACTO CON ESCUDO DE DERECHA DE ARRIBA
player_guard_project_up_right = [pygame.image.load("src/resources/image/personaje/guard_protects_up (1).png"),
                                pygame.image.load("src/resources/image/personaje/guard_protects_up (2).png"),
                                pygame.image.load("src/resources/image/personaje/guard_protects_up (3).png")
]
#IMPACTO CON ESCUDO DE IZQUIERDA DE ARRIBA
player_guard_project_up_left = girar_imagenes(player_guard_project_up_right)
#MUERTE DERECHA
player_death_right = [pygame.image.load("src/resources/image/personaje/death (1).png"),
                    pygame.image.load("src/resources/image/personaje/death (2).png"),
                    pygame.image.load("src/resources/image/personaje/death (3).png"),
                    pygame.image.load("src/resources/image/personaje/death (4).png"),
                    pygame.image.load("src/resources/image/personaje/death (5).png"),
                    pygame.image.load("src/resources/image/personaje/death (6).png"),
                    pygame.image.load("src/resources/image/personaje/death (7).png")
]
#MUERTE IZQUIERDA
player_death_left = girar_imagenes(player_death_right)

# ***************************************************************************************************

# -------------------ENEMIGOS-------------------------

#ENEMIGO CRAB MOVIMIENTO-----------------------
enemy_crag = [pygame.image.load("src/resources/image/enemigos/crab (1).png"),
            pygame.image.load("src/resources/image/enemigos/crab (2).png"),
            pygame.image.load("src/resources/image/enemigos/crab (3).png"),
            pygame.image.load("src/resources/image/enemigos/crab (4).png")
]
#ATAQUE ENEMIGO (CUALQUIER ENEMIGO PUEDE USARLO)------------------
enemy_attacK = [pygame.image.load("src/resources/image/ataques/fire (1).png"),
                pygame.image.load("src/resources/image/ataques/fire (2).png"),
                pygame.image.load("src/resources/image/ataques/fire (3).png")
]
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
