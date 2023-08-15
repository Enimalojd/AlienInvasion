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
        self.ship = Ship(self)






    def run_game(self):
        # Запуск основного цикла игры
        while True:
            # отслеживание клавиатуры и мыши
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        #обрабатывает нажатия клавиш и события мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        #обновляет изображение на экране и отоброжает новый экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()




if __name__ == "__main__":
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
