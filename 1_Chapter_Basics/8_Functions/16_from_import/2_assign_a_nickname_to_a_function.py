# Page 156
# Назначение псевдонима для функции

# Если имя импортируемой функции может конфликтовать с именем существующей
# функции или функция имеет слишком длинное имя, его можно заменить коротким
# уникальным псевдонимом (alias) — альтернативным именем для функции.
# from имя_модуля import имя_функции as псевдоним.

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
