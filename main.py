#Group 1's city builder main program.
#Last updated 03/09/21
#Members Names: Isaac Vrba, Cameron Jones, Dan.


import pygame as pg #changes pygame to pg so we don't have to type 'pygames' out each time
import sys
from os import path
from settings import *
from sprites import *
import random

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #creates the size of the screen
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def itemSpawner(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        item_list = ['R', 'S', 'F']
        item_qty = [0, 0, 0]
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '.':
                    randNum = random.randint(0,100)
                    if randNum == 2:
                        if item_qty[1] < 10:
                            Stone(self, col, row)
                            item_qty[1] = item_qty[1] + 1
                    elif randNum == 1:
                        if item_qty[2] < 5:
                            Food(self, col, row)
                            item_qty[2] = item_qty[2] + 1
                    #elif randNum == 0:
                        #if item_qty[0] < 3:
                            #self.rabbit = rabbit(self, col, row)
                            #item_qty[0] = item_qty[0] + 1
                elif tile == '1':
                    Wall(self, col, row)
                elif tile == 'P':
                    self.player = Player(self, col, row)

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1': #loads a traditional, non-passable wall
                    Wall(self, col, row)
                if tile == 'P': #loads the player in the tile with a 'P'
                    self.player = Player(self,col, row)
                if tile == '2': #loads spaces with 2 with a passable wall
                    PassableWall(self, col, row)
                if tile == 'R': #loads a rabbit
                    self.rabbit = rabbit(self, col,row)
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

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        for entity in self.all_sprites:
            self.screen.blit(entity.image, entity.rect)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
                if event.key == pg.K_SPACE:
                    self.player.placeWall()
                if event.key == pg.K_f:
                    self.player.shoot();
        Movex = random.randint(-1,1)
        Movey = random.randint(-1,1)

        self.rabbit.move(dx=Movex, px=self.player.x, py=self.player.y)
        self.rabbit.move(dy=Movey, px=self.player.x, py=self.player.y)

        for bullet in self.bullets:
            bullet.move(1)

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