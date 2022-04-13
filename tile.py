import pygame 
from settings import *
class Tile(pygame.sprite.Sprite): #добавление фун-й из другой папки 
    def __init__(self, pos, name, groups):
        super().__init__(groups) #инициализация функций, которые мы добавили
        self.image = pygame.image.load(name)#добавление картинки 
        self.rect = self.image.get_rect(topleft=pos) #создаем переменную в которую заносим расположение нашей картинки