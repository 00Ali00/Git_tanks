import pygame
from settings import *

class End_level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface() 
        self.isQuit = False
        self.isRestart = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_x]:
            self.isQuit = True
        elif keys[pygame.K_RETURN]:
            self.isRestart = True

    def end_text(self):
        self.main_font = pygame.font.SysFont('comicsans', 50)
        self.text = self.main_font.render('Game over', 1, 'white', 'black')
        self.text_space = self.main_font.render('Press X to QUIT', 1, 'white', 'black')
        self.text_p = self.main_font.render('Press ENTER to RESTART', 1, 'white', 'black')
        self.pos = self.text.get_rect(center=(WIDTH//2, HEIGHT//2 - 90))
        self.pos_space = self.text.get_rect(center=(WIDTH//2 - 90, HEIGHT//2 ))
        self.pos_p = self.text.get_rect(center=(WIDTH//2 - 175, HEIGHT//2 + 100))


    def run(self):
        self.input()
        self.end_text()
        self.display_surface.blit(self.text, self.pos)
        self.display_surface.blit(self.text_space, self.pos_space)
        self.display_surface.blit(self.text_p, self.pos_p)