import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.display.set_caption("EVE Online")
    # Инициализирует pygame, settings и объект экрана.
    ai_settings = Settings()
    pygame.init()
    # Переменные с класса Settings вкладываются в кортеж.
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))

    # Создание экземпляра класса. Отображение корабля игрока.
    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update_ship_moving()
        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, ship)


run_game()
