"""Asteroid class for a game."""

from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        """Initialize an asteroid with position and radius."""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw the asteroid on the screen."""
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        """Update the asteroid's position based on its velocity."""
        self.position += self.velocity * dt
