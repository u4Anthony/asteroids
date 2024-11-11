import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		print("asteroid drawn")
		pygame.draw.circle(surface=screen, center=(self.position), color="white", radius=self.radius, width=2)

	def update(self, dt):
		print("asteroid updated")
		self.position += self.velocity * dt
