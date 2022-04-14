import pygame
from settings import *
from level import Level
from end_level import End_level
class Game:
    def __init__(self):
        pygame.init() # инициализируем 
        pygame.display.set_caption('Tanks') # задаем имя
        pygame.display.set_icon(pygame.image.load('images/Иконка.bmp')) # создаем иконку в углу экрана
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # задаем высоту и ширину нашего экрана
        self.clock = pygame.time.Clock()
        self.level = Level() # класс 
        self.end_level = End_level() # класс
        
    def run(self):
        isRun = True
        while isRun:
            for event in pygame.event.get(): # создаем события 
                if event.type == pygame.QUIT: # если пользователь нажал крестик, цикл останавливается 
                    isRun = False
                    # exit()
                    # pygame.quit()
                    # sys.exit()
            self.screen.fill('black') # заполняем экран черным цветом
            
            if self.level.end == True:
                pygame.mixer.music.pause()
                self.end_level.run()
                if self.end_level.isRun == True:
                    isRun = False
                if self.end_level.isRestart == True:
                    self.screen.fill('black')
                    self.level.run()
            else:
                self.level.run()
            pygame.display.update() # обновляем экран 
            self.clock.tick(FPS) # задаем количество выполнений цикла в секунду (FPS)
            #pygame.time.delay(20)

if __name__ == '__main__': # проверяет программа или пакет
    pygame.font.init()
    game = Game()
    game.run()  
