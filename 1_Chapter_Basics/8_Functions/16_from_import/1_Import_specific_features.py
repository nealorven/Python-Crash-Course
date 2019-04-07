# Page 156
# Импортирование конкретных функций

### Также возможно импортировать конкретную функцию из модуля.
# Общий синтаксис выглядит так:
# from имя_модуля import имя_функции

### Вы можете импортировать любое количество функций из модуля, разделив их
# имена запятыми:
# from имя_модуля import функция_0, функция_1, функция_2

### Если ограничиться импортированием только той функции, которую вы
# намереваетесь использовать, пример making_pizzas.py будет выглядеть так:

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
