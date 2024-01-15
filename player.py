from screen_settings import load_image, WIDTH, HEIGHT
import pygame


class Player(pygame.sprite.Sprite):
    image = load_image("player.png")

    def __init__(self, my_group, x, y):
        super().__init__(my_group)
        self.image = self.__class__.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 10
        self.speed = 5
        self.damage_coeff = 1
        self.mask = pygame.mask.from_surface(self.image)

    def _move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def update(self):
        self._move()
        self._thor_screen_teleport()
        self._check_hp()
        print(self.hp)

    def teleport(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def _thor_screen_teleport(self):
        if self.rect.x + self.rect.width < 0:
            self.rect.x = WIDTH
        elif self.rect.x > WIDTH:
            self.rect.x = -self.rect.width

        if self.rect.y + self.rect.height < 0:
            self.rect.y = HEIGHT
        elif self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height

    def _check_hp(self):
        if self.hp <= 0:
            self.kill()
