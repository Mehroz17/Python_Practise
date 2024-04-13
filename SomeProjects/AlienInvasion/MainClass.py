## Making Alien Invasion Game using Pygame


# Starting the game

import sys
import pygame

from settings import Settings
from Ship_Class import Ship
from Bullet_Class import Bullet
from alien import Alien


class Alien_Invasion:
    """main class to manage the game assests and behaviour"""


    #constructor
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption("Alien Invasion")
        self.ship =Ship(self)
        #bullets
        self.bullets = pygame.sprite.Group()

        #aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()




    def run_game(self):
        # main loop
        while True:
            #watch for the events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()



    def _check_events(self):
        # responds to keypress
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif(event.type == pygame.KEYDOWN ):
                self._check_keydown_events(event)
            elif(event.type ==pygame.KEYUP):
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = True
        elif (event.key == pygame.K_LEFT):
            self.ship.moving_left = True
        elif(event.key == pygame.K_UP):
            self.ship.moving_top = True
        elif(event.key == pygame.K_DOWN):
            self.ship.moving_bottom = True
        elif(event.key == pygame.K_SPACE):
            self._fire_bullet()
        elif(event.key == pygame.K_q):
                sys.exit()

    def _check_keyup_events(self,event):
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = False
        elif (event.key == pygame.K_LEFT):
            self.ship.moving_left = False
        elif (event.key == pygame.K_UP ):
            self.ship.moving_top = False
        elif (event.key == pygame.K_DOWN):
            self.ship.moving_bottom = False


    # updating bullets method
    def _update_bullets(self):
        self.bullets.update()
        # getting rid of old bullets so that the system did not get slow
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    #bullet firing
    def _fire_bullet(self):
        # create a new bullet and add it to the bullets group
        if(len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)




    #update screen method
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.biltime()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    # Alien Creation
    def _create_fleet(self):
        # creating the fleet of the aliens
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        available_space_x = self.settings.screen_w -(2*alien_width)
        number_aliens_x = available_space_x // (2*alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_h - (3*alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)


    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien_x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien_x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_aliens(self):
        self.aliens.update()

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()