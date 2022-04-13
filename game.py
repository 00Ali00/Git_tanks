import pygame
from settings import *
from level import Level
from end_level import End_level
class Game:
    def __init__(self):
        pygame.init() #инициализируем 
        pygame.display.set_caption('Tanks') #задаем имя
        pygame.display.set_icon(pygame.image.load('images/Иконка.bmp'))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #задаем высоту и ширину нашего экрана
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.end_level = End_level()
        
    def run(self):
        isRun = True
        while isRun:
            for event in pygame.event.get(): #создаем события 
                if event.type == pygame.QUIT: #если событие QUIT выходим из цикла
                    isRun = False
                    # exit()
                    # pygame.quit()
                    # sys.exit()
            self.screen.fill('black') #заполняем черным цветом
            
            if self.level.end == True:
                pygame.mixer.music.pause()
                self.end_level.run()
            else:
                self.level.run()
            if self.end_level.isRun == False:
                isRun = False
            pygame.display.update() #обновляем дисплей 
            self.clock.tick(FPS) #тормозим программу до заданного ФПС
            #pygame.time.delay(20)

        

if __name__ == '__main__': #проверяет программа или пакет
    pygame.font.init()
    game = Game()
    game.run() 
