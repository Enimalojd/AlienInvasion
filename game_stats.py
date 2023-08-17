class GameStats():
    #отслеживание статистики игры

    def __init__(self, ai_game):
        #инициализирует статистику
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.pause = False

    def reset_stats(self):
        #Инициализирует статистику, которая меняется в ходе игры
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1