import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.ai_settings = ai_settings
        self.screen = screen

        # Загрузка изображения корабля и сохранение в self.image.
        self.image = pygame.image.load('images/ship.bmp')
        # get_rect используется для получения поверхности прямоугольника.
        self.rect = self.image.get_rect()
        # Сохраняем прямоугольник экрана в self.screen_rect.
        self.screen_rect = screen.get_rect()

        # Центр определяется атрибутами center, centerx или centery.
        # Стороны определяются атрибутами top, bottom, left и right.
        # X координата.
        self.rect.centerx = self.screen_rect.centerx
        # Y координата.
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center_y -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.ai_settings.ship_speed_factor

        # Обновление атрибута rect.centerx на основании self.center.
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
