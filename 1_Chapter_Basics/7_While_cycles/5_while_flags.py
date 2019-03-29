# Если программа должна выполняться только при истинности нескольких условий,
# определите одну переменную-флаг, который мы назовем active.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program. quit
