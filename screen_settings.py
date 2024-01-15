import pygame

__all__ = ["SIZE", "WIDTH", "HEIGHT", "DISPLAY", "load_image", "BACKGROUND_IMAGE", "FPS", "CLOCK"]


def load_image(path, colorkey=None):
    image = pygame.image.load("textures/" + path)
    if colorkey:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
DISPLAY_INFO = pygame.display.Info()
SIZE = WIDTH, HEIGHT = DISPLAY_INFO.current_w, DISPLAY_INFO.current_h
DISPLAY = pygame.display.set_mode(SIZE)

BACKGROUND_IMAGE = pygame.surface.Surface(SIZE)
BACKGROUND_TILE = load_image("background_tile.png")

for i in range(9):
    for j in range(16):
        BACKGROUND_IMAGE.blit(BACKGROUND_TILE, (j * 120, i * 120))

FPS = 120
CLOCK = pygame.time.Clock()
