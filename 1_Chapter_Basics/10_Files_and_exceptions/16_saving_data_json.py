# Page 204
# Сохранение данных

# ПРИМЕЧАНИЕ
# Формат JSON (JavaScript Object Notation) был изначально разработан для
# JavaScript. Впрочем, с того времени он стал использоваться во многих языках,
# включая Python.

# Функции json.dump() и json.load()
# Напишем короткую программу для сохранения набора чисел и другую программу,
# которая будет читать эти числа обратно в память.

# Модуль json позволяет организовать простейший обмен данными между программами.

import json

numbers = [2, 3, 5, 7, 11, 13]

# Записать данные в .json
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# Прочитать данрные из .json
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

# [2, 3, 5, 7, 11, 13]
