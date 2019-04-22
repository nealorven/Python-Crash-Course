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


def get_new_username():
    """Запрашивает новое имя пользователя."""
    # Создает файл и делает запись, возвращает в 'get_new_username'.
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        # Создает файл и запись в 'username.json'.
        json.dump(username, f_obj)
    # Возвращает username в 'greet_user'.
    return username


def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    # Читает данные из 'username.json'.
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        # Возвращает None в 'if username' > 'greet_user'
        return None
    else:
        # Возвращает username в 'greet_user'
        return username


def greet_user():
    """Приветствует пользователя по имени."""
    # Запрос на наличие файла 'username.json'.
    username = get_stored_username()

    if username:
        print("Welcome back, " + username + "!")
    else:
        # Если if не определил вложение то...
        # то обращаемся к 'get_new_username'.
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
