# Page 131
# Начинаем с двух списков: пользователей для проверки и пустого списка для
# хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Цикл while выполняется, пока в списке unconfirmed_users остаются элементы.
# Проверяем каждого пользователя, пока остаются непроверенные пользователи.
# Каждый пользователь, прошедший проверку, перемещается в список проверенных.
while unconfirmed_users:
    # Изымаем элементы методом .pop и передаем в переменную current_user
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    # В список confirmed_users передаем элементы методом .append
    confirmed_users.append(current_user)

# Вывод всех проверенных пользователей.
print("\nThe following users have been confirmed:")

# Перебираем confirmed_users
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice

# The following users have been confirmed:
# Candace
# Brian
# Alice
