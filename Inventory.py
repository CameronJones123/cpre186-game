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
class text:
    def __init__(self, game,userText,isMiningText,player):
        self.game = game
        self.font = pg.font.Font('freesansbold.ttf', 30)
        self.textSurface = self.font.render(str(userText), True, WHITE)
        self.textSurfaceRect = self.textSurface.get_rect()
        self.isMiningText = isMiningText
        self.remove = False
        self.textSurfaceRect.x = player.rect.x+10
        self.textSurfaceRect.y = player.rect.y-40
    def unload(self):
        now = pg.time.get_ticks()
        if(self.isMiningText == True and now % 100 == 0):
            self.remove = True
