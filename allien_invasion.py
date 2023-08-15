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
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
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
