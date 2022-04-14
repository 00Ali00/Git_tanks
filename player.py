import pygame 
from settings import *
from bullet import Bullet

class Player(pygame.sprite.Sprite): #добавление фун-й из другой папки 
    def __init__(self, pos, name, groups, obstacle_sprites, destroy):
        super().__init__(groups) #инициализация функций, которые мы добавили
        self.image = pygame.image.load(name).convert_alpha() #добавление картинки 
        self.rect = self.image.get_rect(topleft=pos) #создаем переменную в которую заносим расположение нашего
        self.angle = 0
        self.groups = groups
        self.direction = pygame.math.Vector2() #задаем вектор направления
        self.obstacle_sprites = obstacle_sprites #задаем в конструктор спрайты для столкновения
        self.destroy = destroy
        self.time = 80
        self.isAlive = True
        self.isReady = True

    def input(self):
        keys = pygame.key.get_pressed() #задаем в переменную keys все нажатые кнопки в момент FPS
        sound_bullet = pygame.mixer.Sound('sounds/выстрел.ogg')
        self.direction.y = 0
        self.direction.x = 0

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.angle = 0
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.angle = 2

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.angle = 1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.angle = 3

        if not self.isReady:
            self.time -= 1
            if not self.time:
                self.isReady = True
                self.time = 80

        if keys[pygame.K_SPACE]:
            if self.isReady:
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
                sound_bullet.play()
        
    def move(self, speed):
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom                        
                                
    def update(self):
        self.input()
        self.move(3)
        self.image = pygame.transform.rotate(PLAYER_SPRITE, self.angle * 90)
        if not self.isAlive:
            self.kill()
