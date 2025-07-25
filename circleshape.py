"""CircleShape class for Pygame"""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for circular game objects in Pygame."""

    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Update the position of the circle shape."""
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius, 2
        )

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other):
        """Check if this circle is colliding with another circle."""
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)
