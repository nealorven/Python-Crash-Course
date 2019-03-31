prompt = "\nEnter 'exit' to end the program."
prompt += "\nPizza extras: "

pizza_extras = ""

while pizza_extras != 'exit':
    pizza_extras = input(prompt)

    if pizza_extras != 'exit':
        print(f"Adding: {pizza_extras.title()}")

# Enter 'exit' to end the program.
# Pizza extras: salami
# Adding: Salami

# Enter 'exit' to end the program.
# Pizza extras: cheese
# Adding: Cheese

# Enter 'exit' to end the program.
# Pizza extras: olives
# Adding: Olives
