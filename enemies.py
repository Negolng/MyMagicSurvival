from screen_settings import load_image, FPS, WIDTH, HEIGHT
import pygame
import math


class Enemy(pygame.sprite.Sprite):
    image = load_image("enemy.png", -1)

    def __init__(self, enemy_group, x, y):
        super().__init__(enemy_group)
        self.image = self.__class__.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        self.mask = pygame.mask.from_surface(self.image)
        self.damage = 4

    def _chase(self, player):
        xv, yv = self._speed_calc(
            player.rect.x, player.rect.y, self.rect.x, self.rect.y
        )
        if self.rect.x < player.rect.x:
            self.rect.x += xv
        if self.rect.x > player.rect.x:
            self.rect.x += xv
        if self.rect.y < player.rect.y:
            self.rect.y += yv
        if self.rect.y > player.rect.y:
            self.rect.y += yv

    def _speed_calc(self, target_x, target_y, sender_x, sender_y):
        xv = ((target_x - sender_x) / FPS)
        yv = ((target_y - sender_y) / FPS)
        if xv != 0 and yv != 0:
            mult = math.sqrt(self.speed ** 2 / (xv ** 2 + yv ** 2))
        else:
            mult = 1
        return xv * mult, yv * mult

    def _touch_player(self, player):
        if pygame.sprite.collide_mask(self, player):
            player.hp -= self.damage / FPS

    def update(self, player):
        self._chase(player)
        self._touch_player(player)
        self._thor_screen_teleport()

    def _thor_screen_teleport(self):
        if self.rect.x + self.rect.width < 0:
            self.rect.x = WIDTH
        elif self.rect.x > WIDTH:
            self.rect.x = -self.rect.width

        if self.rect.y + self.rect.height < 0:
            self.rect.y = HEIGHT
        elif self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
