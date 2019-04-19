# Page 207
# Рефакторинг

# Часто возникает типичная ситуация: код работает, но вы понимаете, что его
# структуру можно усовершенствовать, разбив его на функции, каждая из которых
# решает свою конкретную задачу. Этот процесс называется рефакторингом.

# В процессе рефакторинга 18_refactoring.py мы можем переместить основную
# часть логики в одну или несколько функций. Основной задачей 18_refactoring.py
# является вывод приветствия для пользователя, поэтому весь существующий код
# будет перемещен в функцию greet_user():

import json


def great_user():
    """Приветствует пользователя по имени."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # Если файл .json отсутствует то выполняется следующее.
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, "
                  + username.title() + "!")
    else:
        print("Welcome back, " + username.title() + "!")


great_user()

# What is your name? neal
# We'll remember you when you come back, Neal!

# Welcome back, Neal!
