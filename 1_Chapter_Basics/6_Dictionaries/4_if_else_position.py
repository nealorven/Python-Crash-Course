# Рассмотрим более интересный пример: отслеживание позиции пришельца,
# который может двигаться с разной скоростью:

alien_ship = {
    'x_position': 0,
    'y_position': 0,
    'speed': 'medium'
    }
print(f"Original 'y_position': {alien_ship['y_position']}.")

# Пришелец двигается со скоростью - 1
if alien_ship['speed'] == 'slow':
    x_increment = 1

# Пришелец двигается со скоростью - 2
elif alien_ship['speed'] == 'medium':
    x_increment = 2

# Пришелец двигается со скоростью - 3
else:
    x_increment = 3

# Перезапись переменной
alien_ship['y_position'] = alien_ship['y_position'] + x_increment
print(f"New 'y_position': {alien_ship['y_position']}.")

# Original 'y_position': 0.
# New 'y_position': 2.
