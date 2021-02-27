import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)
class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((170, 200, 0))
        self.rect = self.surf.get_rect()
    def update(self,pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -50)
            if pressed_keys[K_DOWN]:
                    self.rect.move_ip(0, 50)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-50, 0)
            if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(50, 0)