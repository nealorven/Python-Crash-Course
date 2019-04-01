# Выход через break
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) asd
# I'd love to go to Asd!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) quit

"""Переделать, добавить что то новое"""
