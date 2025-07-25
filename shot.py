"""Handle shots in the Asteroids game."""

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    """Shot class to represent the player's shots in the Asteroids game."""

    def __init__(self, x, y):
        """Initialize a shot with position and radius."""
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        """Draw the shot on the screen."""
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        """Update the shot's position based on its velocity."""
        self.position += self.velocity * dt
