import pygame.font

class Scoreboard():
    #класс для вывода счёта игрока
    def __init__(self, ai_game):
        #инициализирует атрибуты подсчёта игровой информации
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats



        #настройки шрифта
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_level()


    def prep_score(self):
        #преобразует текущий счёт в графическое изображение
        score_str = str(self.stats.score)
        self.score_image = self.font.render(f"Текущий счёт: {score_str}", True, self.text_color, None)

        #вывод счёта в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #выводит изображение на экран
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        #преобразует текущий уровень в графическое изображение
        level_str = str(self.stats.level)
        self.level_image = self.font.render(f"Уровень: {level_str}", True, self.text_color, None)

        #выводит графическое изображение под счётом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
