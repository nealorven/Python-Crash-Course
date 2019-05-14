import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():

    pygame.init()
    # Задает название окна программы.
    pygame.display.set_caption("EVE Online")
    # Инициализирует Pygame, settings и объект экрана.
    ai_settings = Settings()
    # Переменные с класса Settings вкладываются в кортеж.
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    # Создание экземпляра класса. Отображение корабля игрока.
    # Передаем атрибут ship_speed_factor в ship.py.
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль. Экземпляр.
    bullets = Group()

    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Обновляет положение корабля.
        ship.update()
        # Обновляет положение снарядов.
        bullets.update()
        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
