import pygame


class Ship:
    # класс управления кораблём
    def __init__(self, screen):
        # инициализирует корабль и задаёт его начальную форму

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # загружаем картинку корабля
        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется снизу по центру
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
