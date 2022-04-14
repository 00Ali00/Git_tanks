import pygame
from settings import *
from tile import Tile

class Start_game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() 
        self.level = 0
        self.visible_sprites = pygame.sprite.Group() 
        self.create_map() 
        self.isRun = False
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row): 
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),'images/sten1.png', [self.visible_sprites])

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.isRun = True

    def restart(self):
        self.main_font = pygame.font.SysFont('comicsans', 50)
        self.text = self.main_font.render('To play press ENTER', 1, 'white', 'black')
        self.pos = self.text.get_rect(center=(WIDTH//2, HEIGHT//2 - 90))



    def run(self):
        self.input()
        self.restart()
        self.display_surface.fill('black')
        self.display_surface.blit(self.text, self.pos)