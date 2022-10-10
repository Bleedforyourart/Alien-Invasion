import pygame

class Settings:
    """A Class to store all settings for game"""

    def __init__(self):
        """initialize the game's settings"""
    #screen settings
        self.screen_width = 800 
        self.screen_height = 600

        #background
        self.bg_color = (0,0,0)
        self.background = pygame.image.load("images\space.jpg")


    #ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

    #bullet settings - drk frey bullets that are 3 pixels wide and 15 pixels high. Bullets travel slower than the ship
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        self.alien_points = 1
        self.ships_hit = 1

        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_points = int(self.alien_points)
        self.ship_points = int(self.ships_hit)


