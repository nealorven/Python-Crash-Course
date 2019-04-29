import pygame


class Ship:
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen

        # Загрузка изображения корабля и сохранение в self.image.
        self.image = pygame.image.load('images/ship.bmp')
        # get_rect используется для получения поверхности прямоугольника.
        self.rect = self.image.get_rect()
        # Сохраняем прямоугольник экрана в self.screen_rect.
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появился у нижнего края экрана.
        # Центр элемента определяется атрибутами center, centerx или centery.
        # X координата.
        self.rect.centerx = self.screen_rect.centerx
        # Стороны определяются атрибутами top, bottom, left и right.
        # Y координата.
        self.rect.bottom = self.screen_rect.bottom

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update_ship_moving(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


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
