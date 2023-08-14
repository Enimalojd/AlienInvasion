import sys
import pygame
from setting import Settings
from ship import Ship

class AlienInvasion:
    # Класс для управления ресурсами и поведением игры
    def __init__(self):
        # инициализирует игру и создаёт игровые ресусры
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_wight, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)

    def run_game(self):
        # Запуск основного цикла игры
        while True:
            # отслеживание клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
