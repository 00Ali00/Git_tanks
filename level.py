import pygame
from enemy import *
from settings import TILESIZE, WORLD_MAP
from tile import Tile
from player import Player
class Level:
    def __init__(self):
        # pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.mixer.music.load('sounds/Фон.mp3')
        pygame.mixer.music.set_volume(0.08)
        pygame.mixer.music.play(-1)
        self.display_surface = pygame.display.get_surface() # задаем поверхность на которой будет расположена стенка
        self.level = 1 # задаем что в классе self будет level 1 
        self.visible_sprites = pygame.sprite.Group() # create visible sprites
        self.obstacle_sprites = pygame.sprite.Group() #create obstacle sprites
        self.destroy = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.create_map() # create map
        self.end = False

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP): # пронумеровываем списки 
            for col_index, col in enumerate(row): # пронумеровываем столбцы списков
                x = col_index*TILESIZE
                y = row_index*TILESIZE
                if col == 'x':
                    Tile((x,y),'images/sten1.png', [self.visible_sprites, self.obstacle_sprites]) #указываем что Tile 
                if col == 'p':
                    self.player = Player((x,y),'images/tank.png', [self.visible_sprites, self.players], self.obstacle_sprites, self.destroy)
                if col == 'e':
                    self.player = Enemy((x,y),'images/tank.png', [self.visible_sprites, self.destroy], self.obstacle_sprites, self.players)
    
    def run(self):
        self.visible_sprites.draw(self.display_surface) #рисуем по заданным координатам 
        self.visible_sprites.update() #обновляем
        if len(self.players) == 0:
            self.end = True
