class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((170, 200, 0))
        self.rect = self.surf.get_rect()
    def update(self,pressed_keys):
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -10)
                self.in_air = True
                self.collided_y = False
            if pressed_keys[K_DOWN]:
                if(self.in_air == True):
                    self.rect.move_ip(0, 5)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.collided_x = False
            if pressed_keys[K_RIGHT]:
                if(self.collided_x == False):
                    self.rect.move_ip(5, 0)
            if self.rect.left < 0:
                self.rect.left = 0
            if (self.in_air == True):
                self.rect.move_ip(0, 5)