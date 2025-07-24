"""Player class for Asteroids."""

import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape


class Player(CircleShape):
    """Player class to represent the player in the Asteroids game."""

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        """draw the player as a triangle shape."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Update the player's position and rotation."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
