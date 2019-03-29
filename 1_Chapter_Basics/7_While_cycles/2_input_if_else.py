# При использовании функции input() Python интерпретирует все данные,
# введенные пользователем, как строку. Для ввода чисел нужен метод int()

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name.title()}!")

# Hello, Roman!

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# How tall are you, in inches? 67
# You're tall enough to ride!

# Оператор вычисления остатка
# При работе с числовыми данными может пригодиться оператор вычисления
# остатка (%), который делит одно число на другое и возвращает остаток

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {str(number)} is even.")
else:
    print(f"\nThe number {str(number)} is odd.")

# Enter a number, and I'll tell you if it's even or odd: 7
# The number 7 is odd.
