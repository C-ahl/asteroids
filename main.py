"""Main entry point for the Asteroids game."""

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, PLAYER_RADIUS
from player import Player


def main():
    """Main function to run the Asteroids game."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    dt = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
        screen.fill("black")

        updateable.update(dt)

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(FPS) / 1000
        pygame.display.set_caption(f"Asteroids - FPS: {clock.get_fps():.2f}")


if __name__ == "__main__":
    main()
