import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	
	clock =  pygame.time.Clock()
	dt = 0	
	
	# init pygame groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
	asteroidfield = AsteroidField()

	while True:
		# check for window quit event and gracefully close game
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		# fill the game window with color black
		screen.fill("black")		

		# update game objects
		for object in updatable:
			object.update(dt)

		# draw game objects
		for object in drawable:
			object.draw(screen)
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				return
			for shot in shots: 
				if asteroid.collision(shot):
					asteroid.kill()
					shot.kill()
	
		# update the full display
		pygame.display.flip()
		
		# tick the game clock 60 for 60fps
		tick = clock.tick(60)
		dt = tick / 1000 # convert from milliseconds to seconds

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
	main()
