import pygame
from settings import *
from tile import Tile

class Start_game:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() 
        self.level = 0
        self.isStart = False
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.isStart = True

    def start_text(self):
        self.main_font = pygame.font.SysFont('comicsans', 50)
        self.text = self.main_font.render('To play press ENTER', 1, 'white', 'black')
        self.pos = self.text.get_rect(center=(WIDTH//2, HEIGHT//2 - 90))



    def run(self):
        self.input()
        self.start_text()
        self.display_surface.blit(self.text, self.pos)