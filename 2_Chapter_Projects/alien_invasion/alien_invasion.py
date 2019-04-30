import pygame
from settings import Settings
from ship import Ship
import game_functions as game_fnc


def run_game():
    # Задает название окна программы.
    pygame.display.set_caption("EVE Online")
    # Инициализирует Pygame, settings и объект экрана.
    eve_settings = Settings()
    pygame.init()
    # Переменные с класса Settings вкладываются в кортеж.
    screen = pygame.display.set_mode((eve_settings.screen_width,
                                      eve_settings.screen_height))
    # Создание экземпляра класса. Отображение корабля игрока.
    ship = Ship(screen)

    while True:
        # Обновляет положение корабля.
        ship.update_ship_moving()
        # Отслеживание событий клавиатуры и мыши.
        game_fnc.check_events(ship)
        # При каждом проходе цикла перерисовывается экран.
        # Ссылается в модуль game_functions.py в метод update_screen.
        game_fnc.update_screen(eve_settings, screen, ship)


run_game()
