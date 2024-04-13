import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom of the scree

        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        #storing the decimal position for the vertical postion of the ship
        self.y = float(self.rect.y)

        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False




    def update(self):
        if(self.moving_right and self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if(self.moving_left and self.rect.left >0):
            self.x -= self.settings.ship_speed
        if(self.moving_top and self.rect.top > 0 ):
            self.y -= self.settings.ship_speed_v
        if(self.moving_bottom  and self.rect.bottom <= 700): #and
            self.y += self.settings.ship_speed_v

        #update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def biltime(self):
        self.screen.blit(self.image,self.rect)
