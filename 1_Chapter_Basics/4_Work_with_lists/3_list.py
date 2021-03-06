# Если вы хотите создать числовой список, преобразуйте
# результаты range() в список при помощи функции list():
numbers = list(range(1,6))
print(numbers)

# [1, 2, 3, 4, 5]

# Функция range() также может генерировать числовые последовательности,
# пропуская числа в заданном диапазоне. Начинает с 2 до 10(11) с шагом 2.
even_numbers = list(range(2,11,2))
print(even_numbers)

# [2, 4, 6, 8, 10]

# С помощью функции range() можно создать практически любой диапазон чисел:
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Чтобы сделать код более компактным:
squares = []
for value in range(1,11):
    squares.append(value**2)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Некоторые функции Python предназначены для работы с числовыми списками.
# Например, вы можете легко узнать минимум, максимум и сумму числового списка:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 0
# 9
# 45

# В следующем примере список квадратов, знакомый вам по предыдущим примерам,
# строится с использованием генератора списка:
squares = [value**2 for value in range(1,11)] # Цикл for..in в одну строку, создается список
print(squares)

# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
