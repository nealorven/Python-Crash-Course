
pixels = []
pixel_0 = {'r': 'red', 'g': 'green', 'b': 'blue'}

pixels = {
    'pixel_0': ['r', 'g', 'b'],
    'pixel_1': ['r', 'g', 'b'],
    'pixel_2': ['r', 'g', 'b'],
    'pixel_3': ['r', 'g', 'b'],
    }

# Создание пустого списка для хранения пришельцев.
aliens = []

# Создаем список с вложенным кортежем.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Вывод первых 5 пришельцев:
for alien in aliens[:5]:
    print(alien)
print("...")

# Вывод количества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))

# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...
# Total number of aliens: 30
