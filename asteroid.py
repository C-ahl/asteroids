"""Asteroid class for a game."""

from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


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

    def split(self):
        """Split the asteroid into two smaller asteroids."""
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vec1 * 1.2
        a2.velocity = vec2 * 1.2
