# Page 196
# Использование исключений для предотвращения аварийного завершения программы

# Правильная обработка ошибок особенно важна в том случае, если программа
# должна продолжить работу после возникновения ошибки. Создадим простой
# калькулятор, который выполняет только операцию деления

# Пример с трассировкой ошибки, где нужно ее исключить
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

# Give me two numbers, and I'll divide them.
# Enter 'q' to quit.
#
# First number: 5
# Second number: 0
#
# Traceback (most recent call last):
#   File "division.py", line 9, in <module>
#     answer = int(first_number) / int(second_number)           <- ошибка
# ZeroDivisionError: division by zero

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    # Блок try включает только код, способный породить ошибку.
    try:
        answer = int(first_number) / int(second_number)
    # Блок except сообщает Python, как поступать при возникновении ошибки.
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# Give me two numbers, and I'll divide them.
# Enter 'q' to quit.
#
# First number: 5
# Second number: 0
# You can't divide by 0!
