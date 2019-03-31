prompt = "\nEnter 'exit' to end the program."
prompt += "\nPress 1 to: Print 'One' word: "
prompt += "\nPress 2 to: Print 'Two' word: "
prompt += "\nYour choice: "

message = ""

# Выход из цикла по условию while
while message != 'exit':
    message = input(prompt)

    if message == '1':
        print("One")
    elif message == '2':
        print("Two")

# Enter 'exit' to end the program.
# Press 1 to: Print 'One' word:
# Press 2 to: Print 'Two' word:
# Your choice: 1
# One

# Enter 'exit' to end the program.
# Press 1 to: Print 'One' word:
# Press 2 to: Print 'Two' word:
# Your choice: 2
# Two

# Enter 'exit' to end the program.
# Press 1 to: Print 'One' word:
# Press 2 to: Print 'Two' word:
# Your choice: exit
