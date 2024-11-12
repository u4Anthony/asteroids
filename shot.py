import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(surface=screen, center=(self.position), color="white", radius=self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt * PLAYER_SHOOT_SPEED
