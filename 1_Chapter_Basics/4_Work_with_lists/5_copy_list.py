# Чтобы скопировать список, создайте срез, включающий весь
# исходный список без указания первого и второго индекса [:].
# Список неполучится скопировать присвоением: friend_foods = my_foods:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Создаем копию списка в переменной

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']

# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']
