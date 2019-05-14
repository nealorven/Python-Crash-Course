import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    # Переместить корабль вправо если КНОПКА ВПРАВО нажата.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # Переместить корабль влево если КНОПКА ВЛЕВО нажата.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # Переместить корабль вверх если КНОПКА ВЛЕВО нажата.
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    # Переместить корабль вниз если КНОПКА ВЛЕВО нажата.
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # Стрелять если КНОПКА ПРОБЕЛ нажата.
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение ее в группу bullets.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    # Корабль остается на месте если КНОПКА ВПРАВО НЕ нажата.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Корабль остается на месте если КНОПКА ВЛЕВО НЕ нажата.
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    # Корабль остается на месте если КНОПКА ВВЕРХ НЕ нажата.
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    # Корабль остается на месте если КНОПКА ВНИЗ НЕ нажата.
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Если КНОПКА нажата то...
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # Если КНОПКА НЕ нажата то...
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Обновляет изображения на экране и обновляет окно."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
