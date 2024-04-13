import pygame
from pygame.sprite import  Sprite


class Alien(Sprite):
    # class to represent a single alien fleet


    def __init__(self,ai_game):
        #initializing the alien
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #loading the image of alien
        self.image = pygame.image.load("alien3.bmp")
        self.rect =self.image.get_rect()

        #start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y =self.rect.h

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x