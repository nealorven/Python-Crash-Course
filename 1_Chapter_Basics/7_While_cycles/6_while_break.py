# Чтобы немедленно прервать цикл while без выполнения оставшегося кода в цикле
# независимо от состояния условия, используйте команду 'break'.

# ПРИМЕЧАНИЕ
# Команда break может использоваться в любых циклах Python.
# Например, ее можно включить в цикл for для перебора элементов словаря.
# Цикл, который начинается с while True, будет выполняться бесконечно
# если только в нем не будет выполнена команда break.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) quit
