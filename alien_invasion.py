# Creating pygame window and responding to user input

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

# make an empty pygame window by creating a class to represent the game


class AlienInvasion:
    """ overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # the 1200, 800 is a tuple that defines the dimensions of the game window
        # we assign self.screen so it will be available in all methods
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        # set the background color
        self.bg_color = self.screen.fill(self.settings.bg_color)

    def run_game(self):
        """start main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # get rid of bullets that have disappeared
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)

    # responds to keypresses and mouse events
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

        # move the ship to the right
        # self.ship.rect.x += 1

    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
