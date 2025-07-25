"""Main entry point for the Asteroids game."""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PLAYER_RADIUS
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    """Main function to run the Asteroids game."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroidfield = AsteroidField()

    dt = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
        screen.fill("black")

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                running = False
                break

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000
        pygame.display.set_caption(f"Asteroids - FPS: {clock.get_fps():.2f}")


if __name__ == "__main__":
    main()
