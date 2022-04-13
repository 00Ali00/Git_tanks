import pygame 
from settings import *
from boom import Boom
class Bullet(pygame.sprite.Sprite):  
    def __init__(self, pos, groups, angle, obstacle_sprites, destroy):
        super().__init__(groups) 
        self.image = pygame.transform.rotate(BULLET_SPRITE, angle * 90)
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprite = obstacle_sprites
        self.destroy = destroy
        self.angle = angle 
        self.speed = 5
        self.groups = groups

    def move(self):
        if self.angle == 0:
            self.rect.y -= self.speed
        elif self.angle == 1:
            self.rect.x -= self.speed
        elif self.angle == 2:
            self.rect.y += self.speed
        elif self.angle == 3:
            self.rect.x += self.speed    
        self.collision('horizontal')
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect((self.rect.x + 10, self.rect.y + 10, 10, 10)):
                    sprite.isAlive = False
                    Boom([self.groups], (self.rect.x, self.rect.y))
                    self.kill()
            for sprite in self.destroy:
                if sprite.rect.colliderect((self.rect.x + 10, self.rect.y + 10, 10, 10)):
                    sprite.isAlive = False
                    Boom([self.groups], (self.rect.x, self.rect.y))
                    self.kill()
        if direction == 'vertical':
            for sprite in self.obstacle_sprite:
                if sprite.rect.colliderect((self.rect.x + 10, self.rect.y + 10, 10, 10)):
                    sprite.isAlive = False
                    self.kill()
            for sprite in self.destroy:
                if sprite.rect.colliderect((self.rect.x + 10, self.rect.y + 10, 10, 10)):
                    sprite.isAlive = False
                    Boom([self.groups], (self.rect.x, self.rect.y))
                    self.kill()

    def update(self):
        self.move()