# Creating pygame window and responding to user input

import sys

import pygame

# make an empty pygame window by creating a class to represent the game


class AlienInvasion:
    """ overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize game, and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # the 1200, 800 is a tuple that defines the dimensions of the game window
        # we assign self.screen so it will be available in all methods

        # set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start main loop for the game"""
        while True:
            # what for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
