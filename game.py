import pygame
from settings import *
from start_game import Start_game
from level import Level
from end_level import End_level

class Game:
    def __init__(self):
        pygame.init() # инициализируем 
        pygame.display.set_caption('Tanks') # задаем имя
        pygame.display.set_icon(pygame.image.load('images/Иконка.bmp')) # создаем иконку в углу экрана
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # задаем высоту и ширину нашего экрана
        self.clock = pygame.time.Clock()
        self.start_game = Start_game()
        self.level = Level() # класс 
        self.end_level = End_level() # класс
        
    def run(self):
        isRun = True
        while isRun:
            for event in pygame.event.get(): # создаем события 
                if event.type == pygame.QUIT: # если пользователь нажал крестик, цикл останавливается 
                    isRun = False
            self.screen.fill('black') # заполняем экран черным цветом
            if self.level.finish_level == False:
                self.start_game.run()
                if self.start_game.isStart == True:
                    self.screen.fill('black')
                    self.level.run()
            else:
                self.end_level.run()
                if self.end_level.isQuit == True:
                    isRun = False
                if self.end_level.isRestart == True: 
                    self.level.finish_level = False
                    self.level = Level()
                    self.end_level.isRestart = False                
            pygame.display.update() # обновляем экран 
            self.clock.tick(FPS) # задаем количество выполнений цикла в секунду (FPS)
            
if __name__ == '__main__': # проверяет программа или пакет
    pygame.font.init()
    game = Game()
    game.run()  
