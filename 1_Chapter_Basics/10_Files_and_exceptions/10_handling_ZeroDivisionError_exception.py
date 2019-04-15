# Page 195
# Обработка исключения ZeroDivisionError

# Для управления ошибками, возникающими в ходе выполнения программы,
# в Python используются специальные объекты, называемые исключениями.
# Вот как выглядит блок try-except для обработки исключений ZeroDivisionError:

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# You can't divide by zero!
