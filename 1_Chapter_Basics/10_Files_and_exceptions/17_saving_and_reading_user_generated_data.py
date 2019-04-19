# Page 205
# Сохранение и чтение данных, сгенерированных пользователем

# Сохранение с использованием модуля json особенно полезно при работе с данными,
# сгенерированными пользователем, потому что без сохранения эта информация будет
# потеряна при остановке программы.

import json

filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    # Если файл .json отсутствует то выполняется следующее.
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

# What is your name? neal
# We'll remember you when you come back, neal!

# Welcome back, neal!
