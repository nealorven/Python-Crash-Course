import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


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

    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        # Обновляет положение корабля.
        ship.update()
        # При каждом проходе цикла перерисовывается экран.
        # Ссылается в модуль game_functions.py в метод update_screen.
        gf.update_screen(ai_settings, screen, ship)


run_game()
