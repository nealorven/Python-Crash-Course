### Иногда бывает важно проверить, содержит ли список
### некоторое значение, прежде чем выполнять действие:
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# True
# False

### Проверка отсутствия значения в списке 'not in':
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# Marie, you can post a response if you wish.
