import pygame as pg
import random
from settings import *
from Inventory import *


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
        self.isShooting = False
        self.wood = 0
        self.food = 0
        self.stone = 0
        self.pickAxes = [pickAxe(game,self.x,self.y)]
        self.pickAxe = 1

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    # Coppied from collide with wall. Will eventually be a door. Probably needs to be edited.
    def collide_with_passableWalls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def collect(self):
        for rabbit in self.game.rabbits:
            if rabbit.x == self.x + 1 and rabbit.y == self.y or (rabbit.x == self.x - 1 and rabbit.y == self.y) or (rabbit.y == self.y + 1 and rabbit.x == self.x)or(rabbit.y == self.y - 1 and rabbit.x == self.x):
                rabbit.kill()
        for stone in self.game.stone:
            if stone.x == self.x +1 and stone.y == self.y or (stone.x == self.x -1 and stone.y == self.y) or (stone.y == self.y+1 and stone.x == self.x) or (stone.y == self.y-1 and stone.x == self.x):
                if(len(self.pickAxes) != 0):
                    stoneChange = random.randint(1,5)
                    self.stone += stoneChange
                    stone.stone -= stoneChange
                    self.pickAxes[0].swing()
                    stone.mining()
                    newText = text(self.game,stoneChange,True,self)
                    self.game.texts.append(newText)
                    if(self.pickAxes[0].isBroken == True):
                        self.pickAxes.pop(0)



    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def placeWall(self):
        print("place wall")
        new_wall = Wall(self.game, self.x, self.y)
        self.groups.add(new_wall)
        self.group1.add(new_wall)

    def shoot(self,x,y):
        Bullet = bullet(self.game, self.x, self.y)
        Bullet.dirx = x
        Bullet.dirY = y
        Bullet.add(self.groups)
        Bullet.add(self.game.bullets)


class bullet(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self.group1 = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.last = pg.time.get_ticks()
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.dirx = 0
        self.dirY = 0

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def collide_with_rabbit(self, dx=0, dy=0):
        for rabbit in self.game.rabbits:
            if rabbit.x == self.x + dx and rabbit.y == self.y + dy:
                rabbit.isDead = True
                rabbit.image.fill(WHITE)
                return True
        return False

    def move(self):
        print(self.x)
        print("fesf")
        now = pg.time.get_ticks()
        if self.collide_with_rabbit():
            self.kill()
        if not self.collide_with_walls(self.dirx, self.dirY):
            if (now % 25 == 0):
                self.x += self.dirx
                self.y += self.dirY
        else:
            self.kill()


class Wall(pg.sprite.Sprite):  # traditional, non-passable wall
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
        self.groups = game.all_sprites, game.walls  # groups what passable wall are included in
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))  # making it our TILESIZE
        self.image.fill(SKYBLUE)  # changes the color of the block
        self.rect = self.image.get_rect()  # creates a rectangle
        self.x = x  # x position
        self.y = y  # y position
        self.rect.x = x * TILESIZE  # set's its x position
        self.rect.y = y * TILESIZE  # set's its y position


class Stone(pg.sprite.Sprite):  # How stones in the game will be created
    def __init__(self, game, x, y):
        super(Stone, self).__init__()
        self.groups = game.all_sprites,game.stone
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("stone.png").convert()  # loads in the stone.png file
        self.image.set_colorkey((255, 255, 255))  # don't need for this one, but the background color will be white
        self.rect = self.image.get_rect()  # saying that the image is the rectagle
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.stone = 10
    def mining(self):
        if self.stone <= 0:
            self.kill()


class Food(pg.sprite.Sprite):  # Creating Food for the game
    def __init__(self, game, x, y):
        super(Food, self).__init__()  # gives access to methods and properties
        self.groups = game.all_sprites  # groups Food with all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("food.png").convert()  # loads in our food.png file
        self.image.set_colorkey((255, 255, 255))  # sets the transparent's background color to white
        self.rect = self.image.get_rect()  # says the image is in the rectangle
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Gold(pg.sprite.Sprite):  # Creating Gold Ore for the game
    def __init__(self, game, x, y):
        super(Gold, self).__init__()  # gives access to methods and properties
        self.groups = game.all_sprites  # groups gold with all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("gold_ore.png").convert()  # loads in our gold.png file
        self.image.set_colorkey((255, 255, 255))  # sets the transparent's background color to white
        self.rect = self.image.get_rect()  # says the image is in the rectangle
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Wood(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(Wood, self).__init__()  # gives access to methods and properties
        self.groups = game.all_sprites  # groups wood with all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("wood.png").convert()  # loads in our wood.png file
        self.image.set_colorkey((255, 255, 255))  # sets the transparent's background color to white
        self.rect = self.image.get_rect()  # says the image is in the rectangle
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class rabbit(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.rabbits
        pg.sprite.Sprite.__init__(self, self.groups)
        self.last = pg.time.get_ticks()
        self.coolDown = 300
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.isDead = True

    def move(self, dx=0, dy=0, px=0, py=0):

        now = pg.time.get_ticks()
        if(self.isDead == False):
            if not self.collide_with_walls(dx, dy):
                if (now % 200 == 0):
                    self.x += dx
                    self.y += dy
            if (now % 75 == 0):
                if (self.x - px < 0 and self.y == py):
                    print("right")
                    if not self.collide_with_walls(-1, 0):
                        self.x -= 1
                if (px - self.x < 0 and self.y == py):
                    print("left")
                    if not self.collide_with_walls(1, 0):
                        self.x += 1
                if (self.y - py < 0 and self.x == px):
                    print("up")
                    if not self.collide_with_walls(0, -1):
                        self.y -= 1
                if (py - self.y < 0 and self.x == px):
                    print("down")
                    if not self.collide_with_walls(0, 1):
                        self.y += 1

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    # Coppied from collide with wall. Will eventually be a door. Probably needs to be edited.
    def collide_with_passableWalls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    #def randomSpawnedItems(pg.sprite.Sprite)

class pickAxe(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        super(pickAxe, self).__init__()  # gives access to methods and properties
        self.groups = game.all_sprites  # groups wood with all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.image.load("wood.png").convert()  # loads in our wood.png file
        self.image.set_colorkey((255, 255, 255))  # sets the transparent's background color to white
        self.rect = self.image.get_rect()  # says the image is in the rectangle
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.isBroken = False
        self.durability = 100
    def swing(self):
        durabiltiyLost = random.randint(1,5)
        self.durability -= durabiltiyLost
        if(self.durability <= 0):
            print("broken")
            self.isBroken = True