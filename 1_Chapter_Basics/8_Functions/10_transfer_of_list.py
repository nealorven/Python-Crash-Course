# Page 147
# Передача списка

# Часто при вызове функции удобно передать список — имен, чисел или более
# сложных объектов (например, словарей). При передаче списка функция получает
# прямой доступ ко всему его содержимому. Мы воспользуемся функциями для того,
# чтобы сделать работу со списком более эффективной.

#                 ↓ может быть любым именем
def greet_users(names):
    # Вывод простого приветствия для каждого пользователя в списке
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


# Объявление списка
usernames = ['hannah', 'tyra', 'margot']
# Обращение к функции с вложенным списком
greet_users(usernames)

# Hello, Hannah!
# Hello, Tyra!
# Hello, Margot!
