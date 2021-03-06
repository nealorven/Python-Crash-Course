# Page 135
# Определение функции

# В определении функции указывается имя функции и, если нужно,
# описание информации, необходимой функции для решения ее задачи.

#       ↓ определение функции
def greet_user(username):
#                 ↑ имя функции
    print(f"Hello, {username.title()}!") # тело функции

greet_user('jesse')
#             ↑ аргумент

# Hello, Jesse!

# ПРИМЕЧАНИЕ
# Иногда в литературе термины «аргумент» и «параметр» используются как синонимы.
# Не удивляйтесь, если переменные в определении функции вдруг будут названы
# аргументами, а значения, переданные при вызове функции, — параметрами.
