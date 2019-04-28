# Импортируем модуль Pygame
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

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
