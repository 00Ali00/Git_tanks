import pygame
WIDTH = 704
HEIGHT = 704
FPS = 60
TILESIZE = 32

PLAYER_SPRITE = pygame.image.load('images/tank.png')
BULLET_SPRITE = pygame.image.load('images/bullet.png')
ENEMY_SPRITE = pygame.image.load('images/tank.png')
BOOM_SPRITE = [
pygame.image.load('images/boom1.png'),
pygame.image.load('images/boom2.png'),
pygame.image.load('images/boom3.png')
]
WORLD_MAP = [
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ['x','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','e','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','e',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','e',' ','x'],
    ['x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','x'],
    ['x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','x'],
    ['x',' ','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x',' ','x'],
    ['x',' ',' ','x',' ',' ','x','x',' ',' ',' ',' ',' ','x','x',' ',' ',' ','x',' ',' ','x'],
    ['x',' ',' ','e','e','x','x',' ',' ',' ',' ',' ',' ',' ','x','x','e','e',' ',' ',' ','x'],
    ['x',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ','x','x',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ','x',' ',' ','p',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x']
]

END_WORLD_MAP = [
]