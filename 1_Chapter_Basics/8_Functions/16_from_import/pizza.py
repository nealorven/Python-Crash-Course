# Page 155
# Использование произвольного набора именованных аргументов

# Чтобы заняться импортированием функций, сначала необходимо создать модуль.
# Модуль представляет собой файл с расширением .py, содержащий код, который
# вы хотите импортировать в свою программу.

def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
