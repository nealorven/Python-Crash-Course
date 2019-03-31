prompt = "\nEnter 'exit' to end the program."
prompt += "\nYour age: "

age = ""

while age != "exit":
    age = int(input(prompt))

    if age <= 3: print("Ticket free")
    elif age <= 12: print("Ticket price 10$")
    else: print("Ticket price 15$")

    if age != 'exit':
        print(f"Your age: {age}")

# Enter 'exit' to end the program.
# Your age: 3
# Ticket free
# Your age: 3

# Enter 'exit' to end the program.
# Your age: 12
# Ticket price 10$
# Your age: 12

# Enter 'exit' to end the program.
# Your age: 15
# Ticket price 15$
# Your age: 15

"""
Traceback (most recent call last):
  File "7_5_movie_tickets.py", line 7, in <module>
    age = int(input(prompt))
ValueError: invalid literal for int() with base 10: 'exit'

Дописать корректный выход из цикла
"""
