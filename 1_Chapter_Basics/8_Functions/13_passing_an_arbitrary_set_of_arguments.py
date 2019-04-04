# Page 151
# Передача произвольного набора аргументов

# В некоторых ситуациях вы не знаете заранее, сколько аргументов должно быть
# передано функции. К счастью, Python позволяет функции получить произвольное
# количество аргументов из вызывающей команды.

# Функция в следующем примере получает один параметр *toppings,
# но этот параметр объединяет все аргументы, заданные в командной строке:

# Звездочка в имени параметра *toppings приказывает Python создать
# пустой кортеж с именем toppings и упаковать в него все полученные значения.

# Python упаковывает аргументы в кортеж даже в том случае, если функция
# получает всего одно значение:
# ('pepperoni',)
# ('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')

# Making a pizza with the following toppings:
# - pepperoni

make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Making a pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
