import pygame
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = pygame.image.load("images/bg.png")
        self.bg_color = pygame.transform.scale(self.bg_color, (self.screen_width, self.screen_height))
        self.ship_speed = 0.7
        #поведение снаряда
        self.bullet_speed = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.alien_speed = 0.3
        self.fleet_drop_speed = 15
        self.fleet_direction = 1 # 1 вправо, -1 влево
