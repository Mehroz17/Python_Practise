import pygame

from pygame.sprite import  Sprite

class Bullet(Sprite):
    # class to manage the bullets fired from the ship
    def __init__(self,ai_game):
        # create the bullet object at ships current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color


        #creating a bullet
        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet position
        self.y = float(self.rect.y)




    #update function
    def update(self):
        # moving the bullet up screen
        self.y -= self.settings.bullet_speed # for y position we subtract to go upwards

        self.rect.y = self.y

    #
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)