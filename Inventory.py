import pygame as pg
from settings import *

class inventory(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load("inventory.png").convert()
        self.rect = self.image.get_rect()
        self.isLoaded = False
        self.rect.x = 250
        self.rect.y = 250
