class ShipCenter:
    """Отображает корабль в центре экрана."""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # X координата.
        self.rect.centerx = self.screen_rect.centerx
        # Y координата.
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
