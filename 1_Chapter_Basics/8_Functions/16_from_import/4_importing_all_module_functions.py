# Page 157
# Импортирование всех функций модуля

# Также можно приказать Python импортировать каждую функцию в модуле;
# для этого используется оператор *:

### ПРИМЕЧАНИЕ
# После импортирования всех функций вы сможете вызывать каждую функцию по
# имени без точечной записи.

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese
