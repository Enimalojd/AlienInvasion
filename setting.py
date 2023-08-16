import pygame
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colors = (230, 230, 230)
        self.bg_image = pygame.image.load("images/bg.png")
        self.bg_color = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))
       # self.ship_speed = 0.7
        self.ship_limit = 3
        #поведение снаряда
      #  self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        #характеристики пришельца
      #  self.alien_speed = 0.3
        self.fleet_drop_speed = 15
      #  self.fleet_direction = 1 # 1 вправо, -1 влево

        #ускоряющиеся характеристики
        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #инициализирует меняющиеся настройки
        self.ship_speed = 0.7
        self.alien_speed = 0.3
        self.bullet_speed = 1
        self.fleet_direction = 1  # 1 вправо, -1 влево

    def increase_speed(self):
        #увеличивает настройки скорости
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed += self.speedup_scale

