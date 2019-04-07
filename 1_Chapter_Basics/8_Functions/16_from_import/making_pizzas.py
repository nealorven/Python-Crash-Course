# Ссылаемся ан отдельный файл .py с внутренней функцией
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# - pepperoni
#
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

### ПРИМЕЧАНИЕ
# Вам необходимо знать одно: любая функция, определенная в pizza.py,
# будет доступна в making_pizzas.py.

# Первый способ импортирования, при котором записывается команда import
# с именем модуля, открывает доступ программе ко всем функциям из модуля:

# имя_модуля.имя_функции()
