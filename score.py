import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 42)
        
        self.count_score()
        self.count_ships()

    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.ships_image, self.ships_rect)

    def count_score(self):
        rounded_score = round(self.stats.score, 0)
        score_str = "Aliens hit: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.bottom = 750
    
    def count_ships(self):
        ship_str = "Ships Remaining: {}".format(self.stats.ships_left) 
        self.ships_image = self.font.render(ship_str, True, self.text_color, self.settings.bg_color)
        self.ships_rect = self.ships_image.get_rect()
        self.ships_rect.right = self.screen_rect.right - 20
        self.ships_rect.bottom = 700

    def display_gameover(self):
        self.font = pygame.font.SysFont('arial', 100)
        self.game_over_image = self.font.render("Game Over", True, (255,69,0), self.settings.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.right = self.screen_rect.right - 460
        self.game_over_rect.top = 200

        rounded_score = round(self.stats.score, 0)
        alien_str = "Alien kill count: {:,}".format(rounded_score)
        self.alien_points_image = self.font.render(alien_str, True, (255,69,0), self.settings.bg_color)
        self.alien_points_rect = self.alien_points_image.get_rect()
        self.alien_points_rect.right = self.screen_rect.right - 380
        self.alien_points_rect.top = 400

        self.screen.blit(self.game_over_image, self.game_over_rect)
        self.screen.blit(self.alien_points_image, self.alien_points_rect)
