# Page 146
# Использование функции в цикле while

# Функции могут использоваться со всеми структурами Python, уже известными вам.
# Например, используем функцию get_formatted_name() в цикле while.

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: roma
# Last name: orven

# Hello, Roma Orven!

# Please tell me your name:
# (enter 'q' at any time to quit)
# First name: q
