from screen_settings import DISPLAY, BACKGROUND_IMAGE, CLOCK, FPS, WIDTH, HEIGHT
from player import Player
from enemies import Enemy
import pygame


if __name__ == '__main__':
    player_group = pygame.sprite.Group()
    player = Player(player_group, WIDTH // 2, HEIGHT // 2)

    enemy_group = pygame.sprite.Group()
    Enemy(enemy_group, WIDTH // 2 + 50, HEIGHT // 2)

    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()

        DISPLAY.blit(BACKGROUND_IMAGE, (0, 0))

        player_group.update()
        player_group.draw(DISPLAY)

        enemy_group.update(player)
        enemy_group.draw(DISPLAY)

        pygame.display.flip()
        CLOCK.tick(FPS)
