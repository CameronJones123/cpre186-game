class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((170, 200, 0))
        self.rect = self.surf.get_rect()