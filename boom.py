import pygame 
from settings import *

class Boom (pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)        
        self.index = 0
        self.image = BOOM_SPRITE[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.count = 10

    def update(self):
        if self.index + 1 == len(BOOM_SPRITE): 
            if self.count == 0:   
                self.kill()
            else:
                self.count -= 1
        else:
            if self.count == 0:
                self.index += 1
                self.image = BOOM_SPRITE[self.index]
                self.count = 10
            else:
                self.count -= 1