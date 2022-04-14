import pygame 
from settings import *
from random import randrange 
from bullet import Bullet

class Enemy(pygame.sprite.Sprite): #добавление фун-й из другой папки 

    def __init__(self, pos, name, groups, obstacle_sprites, destroy):
        super().__init__(groups) #инициализация функций, которые мы добавили
        self.angle = 0
        self.image = pygame.transform.rotate(ENEMY_SPRITE, self.angle * 90)
        self.image = pygame.image.load(name) #добавление картинки 
        self.rect = self.image.get_rect(topleft=pos) #создаем переменную в которую заносим расположение нашего
        self.direction = pygame.math.Vector2() #задаем вектор направления
        self.random_direction()
        self.groups = groups
        self.obstacle_sprites = obstacle_sprites #задаем в конструктор спрайты для столкновения
        self.destroy = destroy
        self.speed = 3
        self.isReady = True
        self.time = 160
        self.isAlive = True
        self.isTheLife = True

    def random_direction(self):
        dir = randrange(0, 4)
        if dir == 0:
            self.direction.xy = (0, -1)
        elif dir == 1:
            self.direction.xy = (-1, 0)
        elif dir == 2:
            self.direction.xy = (0, 1)
        elif dir == 3:
            self.direction.xy = (1, 0)
        self.angle = dir 

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:                       
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
                    self.random_direction()

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:                       
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
                    self.random_direction()

    def shoot(self):
        if not self.isReady:
            self.time -= 1
            if not self.time:
                self.isReady = True
                self.time = 160
        else:
            self.isReady = False
            dx, dy = 0, 0
            if self.angle == 0:
                dy = -TILESIZE-10
            elif self.angle == 1:
                dx = -TILESIZE-10
            elif self.angle == 2:
                dy = TILESIZE+10
            elif self.angle == 3:
                dx = TILESIZE+10
            Bullet((self.rect.x + dx, self.rect.y + dy),[self.groups[0]], self.angle, self.obstacle_sprites, self.destroy)

    def move(self, speed):
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def update(self):
        self.move(3)
        self.shoot()
        self.image = pygame.transform.rotate(ENEMY_SPRITE, self.angle * 90)
        if not self.isAlive:
            self.kill()
        