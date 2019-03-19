pizzas = ['pepperoni', 'mushroomer', 'cazzarella', 'granite']
my_pizzas = pizzas
friend_pizzas = pizzas[:]

my_pizzas.append('gabini')
friend_pizzas.append('ice capazzo')

print("My favorite pizzas are:")
print(my_pizzas)
print("My friend’s favorite pizzas are:")
print(friend_pizzas)

# My favorite pizzas are:
# ['pepperoni', 'mushroomer', 'cazzarella', 'granite', 'gabini']
# My friend’s favorite pizzas are:
# ['pepperoni', 'mushroomer', 'cazzarella', 'granite', 'ice capazzo']
