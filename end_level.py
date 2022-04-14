import pygame
from settings import *
from tile import Tile

class End_level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() 
        self.level = 1 
        self.visible_sprites = pygame.sprite.Group() 
        self.create_map() 
        self.isRun = False
        self.isRestart = False
    
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row): 
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),'images/sten1.png', [self.visible_sprites])

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.isRun = True
        elif keys[pygame.K_ESCAPE]:
            self.isRestart = True

    def restart(self):
        self.main_font = pygame.font.SysFont('comicsans', 50)
        self.text = self.main_font.render('Game over', 1, 'white', 'black')
        self.text_space = self.main_font.render('Press X to QUIT', 1, 'white', 'black')
        self.text_p = self.main_font.render('Press ENTER to RESTART', 1, 'white', 'black')
        self.pos = self.text.get_rect(center=(WIDTH//2, HEIGHT//2 - 90))
        self.pos_space = self.text.get_rect(center=(WIDTH//2 - 90, HEIGHT//2 ))
        self.pos_p = self.text.get_rect(center=(WIDTH//2 - 175, HEIGHT//2 + 100))


    def run(self):
        self.input()
        self.restart()
        self.display_surface.fill('black')
        self.display_surface.blit(self.text, self.pos)
        self.display_surface.blit(self.text_space, self.pos_space)
        self.display_surface.blit(self.text_p, self.pos_p)