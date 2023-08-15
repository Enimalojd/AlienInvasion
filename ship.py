import pygame


class Ship:
    # класс управления кораблём
    def __init__(self, ai_game):
        # инициализирует корабль и задаёт его начальную форму

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загружаем картинку корабля
        self.image = pygame.image.load("images/rocket.png")
        self.rect = self.image.get_rect()
        # каждый новый корабль появляется снизу по центру
        self.rect.midbottom = self.screen_rect.midbottom
        #сохранение вещественной координаты центра коробля
        self.x = float(self.rect.x)
        #флажки для перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x =self.x

    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
