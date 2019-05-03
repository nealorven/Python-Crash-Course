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

        # X координата.
        # Центр определяется атрибутами center, centerx или centery.
        self.rect.centerx = self.screen_rect.centerx
        # Y координата.
        # Стороны определяются атрибутами top, bottom, left и right.
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Два блока if для одновременного нажатия клавиш.
        # Обновляется атрибут self.center, не self.rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 3
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 3
            self.center -= self.ai_settings.ship_speed_factor
        # Обновление атрибута rect.centerx на основании self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
