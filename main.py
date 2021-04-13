#Group 1's city builder main program.
#Last updated 03/09/21
#Members Names: Isaac Vrba, Cameron Jones, Dan.


import pygame as pg #changes pygame to pg so we don't have to type 'pygames' out each time
import sys
from os import path
from settings import *
from sprites import *
import random
from Inventory import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #creates the size of the screen
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        #self.usedInventory = inventory(pg)
        self.texts = []


    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def itemSpawner(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        #item_list is a list of possible items to add to the map
        item_list = ['R', 'S', 'F', 'G', 'W']
        #item_qty is a list containing the quantities of each item
        item_qty = [0, 0, 0, 0, 0]
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '.':
                    randNum = random.randint(0,100)
                    if randNum == 1:
                        if item_qty[1] < 10:
                            Stone(self, col, row)
                            item_qty[1] = item_qty[1] + 1
                    elif randNum == 2:
                        if item_qty[2] < 5:
                            Food(self, col, row)
                            item_qty[2] = item_qty[2] + 1
                    elif randNum == 3:
                        if item_qty[2] < 5:
                            Gold(self, col, row)
                            item_qty[2] = item_qty[3] + 1
                    elif randNum == 4:
                        if item_qty[2] < 15:
                            Wood(self, col, row)
                            item_qty[2] = item_qty[4] + 1
                    #elif randNum == 0:
                        #if item_qty[0] < 3:
                            #self.rabbit = rabbit(self, col, row)
                            #item_qty[0] = item_qty[0] + 1
                elif tile == '1':
                    Wall(self, col, row)
                elif tile == 'P':
                    self.player = Player(self, col, row)
                elif tile == "R":
                    self.Rabbit = rabbit(self,col,row)


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.rabbits = pg.sprite.Group()
        self.stone = pg.sprite.Group()
        self.food = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1': #loads a traditional, non-passable wall
                    Wall(self, col, row)
                if tile == 'P': #loads the player in the tile with a 'P'
                    self.player = Player(self,col, row)
                if tile == '2': #loads spaces with 2 with a passable wall
                    PassableWall(self, col, row)
                if tile == 'S': #loads stone
                    Stone(self, col, row)
                if tile == 'F': #loads food
                    Food(self, col, row)
                if tile == 'G': #loads in gold
                    Gold(self, col, row)
                if tile == "W": #loads in wood
                    Wood(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    #defining what happens when the program is closed/quits
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def inventory(self):
        inventoryRunning = True
        while inventoryRunning:
            self.screen.fill((0, 0, 0))

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_TAB:
                        inventoryRunning = False

            pg.display.update()

    def draw(self):
        self.screen.blit(BACKGROUND,(0,0))
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
        #if self.usedInventory.isLoaded == True:
            #self.screen.blit(self.usedInventory.image,self.usedInventory.rect)
        for text in self.texts:
            self.screen.blit(text.textSurface,text.textSurfaceRect)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT and self.player.isShooting == False:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT and self.player.isShooting == False:
                    self.player.move(dx=1)
                if event.key == pg.K_UP and self.player.isShooting == False:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN and self.player.isShooting == False:
                    self.player.move(dy=1)
                if event.key == pg.K_SPACE:
                    self.player.placeWall()
                if event.key == pg.K_f and self.player.isShooting == False:
                    self.player.isShooting = True
                elif event.key == pg.K_f and self.player.isShooting == True:
                    self.player.isShooting = False
                if event.key == pg.K_UP and self.player.isShooting == True:
                    self.player.shoot(0, -1)
                    self.player.isShooting = False
                if event.key == pg.K_DOWN and self.player.isShooting == True:
                    self.player.shoot(0, 1)
                    self.player.isShooting = False
                if event.key == pg.K_RIGHT and self.player.isShooting == True:
                    self.player.shoot(1, 0)
                    self.player.isShooting = False
                if event.key == pg.K_LEFT and self.player.isShooting == True:
                    self.player.shoot(-1, 0)
                    self.player.isShooting = False
                if event.key == pg.K_0:
                    self.player.collect()
                #if event.key == pg.K_i and self.usedInventory.isLoaded == False:
                    #self.usedInventory.isLoaded = True
                #elif event.key == pg.K_i and self.usedInventory.isLoaded == True:
                    #self.usedInventory.isLoaded = False
                if event.key == pg.K_TAB:
                    self.inventory()


        Movex = random.randint(-1,1)
        Movey = random.randint(-1,1)

        self.Rabbit.move(dx=Movex, px=self.player.x, py=self.player.y)
        self.Rabbit.move(dy=Movey, px=self.player.x, py=self.player.y)

        for bullet in self.bullets:
            bullet.move()
        for text in self.texts:
            text.unload()
            if(text.remove == True):
                self.texts.remove(text)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.itemSpawner()
    g.run()
    g.show_go_screen()
        
