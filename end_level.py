import pygame
from settings import *
from tile import Tile

class End_level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() 
        self.main_font = pygame.font.SysFont('comicsans', 50)
        self.level = 1 
        self.visible_sprites = pygame.sprite.Group() 
        self.create_map() 
        self.isRun = True
    
    def create_map(self):
        for row_index, row in enumerate(END_WORLD_MAP):
            for col_index, col in enumerate(row): 
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),'images/sten1.png', [self.visible_sprites])

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.isRun = False

    def run(self):
        self.input()
        self.visible_sprites.draw(self.display_surface) 
        self.visible_sprites.update()