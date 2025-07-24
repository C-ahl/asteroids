"""Player class for Asteroids."""

import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
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

    def rotate(self, dt):
        """Rotate the player based on the turn speed."""
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right
            self.rotate(dt)

        if keys[pygame.K_w]:
            # Move forward
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward
            self.move(-dt)

    def move(self, dt):
        """Move the player in the direction it is facing."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
