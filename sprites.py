import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.group1 = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    #Coppied from collide with wall. Will eventually be a door. Probably needs to be edited.
    def collide_with_passableWalls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def placeWall(self):
        print("place wall")
        new_wall = Wall(self.game,self.x,self.y)
        self.groups.add(new_wall)
        self.group1.add(new_wall)



class Wall(pg.sprite.Sprite):   #traditional, non-passable wall
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class PassableWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls #groups what passable wall are included in
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE)) #making it our TILESIZE
        self.image.fill(SKYBLUE)  #changes the color of the block
        self.rect = self.image.get_rect() #creates a rectangle
        self.x = x #x position
        self.y = y #y position
        self.rect.x = x * TILESIZE  #set's its x position
        self.rect.y = y * TILESIZE  #set's its y position

class Stone(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(Stone, self).__init__()
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("stone.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

class rabbit(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.last = pg.time.get_ticks()
        self.coolDown = 300
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        now = pg.time.get_ticks()
        print(now)
        if not self.collide_with_walls(dx, dy):
            if(now % 100 == 0):
                self.x += dx
                self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    #Coppied from collide with wall. Will eventually be a door. Probably needs to be edited.
    def collide_with_passableWalls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE