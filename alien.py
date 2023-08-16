import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #Класс представляющий одного пришельца
    def __init__(self, ai_game):
        #инициализируем пришельца и задаём первоначальную позицию
        super().__init__()
        self.screen = ai_game.screen

        #загрузка изображения пришельца
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        #каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)