import pygame
from settings import Settings


class Ship:
    def __init__(self, ai_game):
        self.settings = Settings()

        # initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rectangle
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()

        self.set_location()
        # Movement flag; start with a ship that is no moving
        self.moving_right = False

        self.moving_left = False
        self.x = float(self.rect.x)

    def set_location(self):
        # start each new ship at the bottom center of the screen
        self.rect.center = self.screen_rect.center

    def update(self):
        # Update the ship's position based on the movement flag
        # Update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        elif self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def show_ship(self):
        # draw the ship at its current location
        self.screen.blit(self.image, self.rect)
