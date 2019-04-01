# Page 132
# Заполнение словаря данными, введенными пользователем
responses = {}
# Установка флага продолжения опроса
polling_active = True
while polling_active:
    # Запрос имени и ответа пользователя
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Ответ сохраняется в словаре
    responses[name] = response
    # Проверка продолжения опроса
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'yes': polling_active = True
    elif repeat == 'no': polling_active = False
    else: print("You entered an incorrect answer.")
    break
# Опрос завершен, вывести результаты
print("\nPoll results:")
for name, response in responses.items():
    print("{} would like to climb {}."
        .format(name.title(), response.title()))

# What is your name? roma
# Which mountain would you like to climb someday? everest
# Would you like to let another person respond? (yes/no) no

# Poll results:
# Roma would like to climb Everest.
