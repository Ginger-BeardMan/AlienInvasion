import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	'''overall class to manage game assets and behavior'''

	def __init__(self):
		'''initialize the game, and create game resources'''
		pygame.init()
		'''define the clock to control frame rate'''
		self.clock = pygame.time.Clock()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		'''set background color'''
		self.bg_color = (230, 230, 230)

		self.ship = Ship(self)

	def run_game(self):
		'''start the main loop for the game'''
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()
			#instance of clock that ticks at the end of the while loop
			self.clock.tick(60)

	def _check_events(self):
		'''respond to keypresses and mouse events'''
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#move the ship to the right
					self.ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					#move the ship to the left
					self.ship.moving_left = True
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					self.ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					self.ship.moving_left = False
				

	def _update_screen(self):
		#update images on the screen, and flip to the new screen
		#'fill' fills the screen with the color
		self.screen.fill(self.settings.bg_color)
		#draw the ship using the blitme function in the Ship class
		self.ship.blitme()

		#make the most recently drawn screen visible
		pygame.display.flip()

if __name__ == '__main__':
	#make a game instance, and run the game
	ai = AlienInvasion()
	ai.run_game()