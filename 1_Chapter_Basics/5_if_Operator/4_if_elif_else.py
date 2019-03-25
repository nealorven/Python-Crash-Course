### Часто в программе необходимо выполнить одно действие в том случае,
### если условие истинно, и другое действие, если оно ложно.
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!

### Цепочка if-elif-else:
age = 12
if age < 4: price = 0
elif age < 18: price = 5
elif age < 65: price = 10
elif age >= 65: price = 5
print("Your admission cost is $" + str(price) + ".")

# Your admission cost is $5.

### Цепочки if-elif-else эффективны, но они подходят только в том случае,
### если истинным должно быть только одно условие.
requested_toppings = [
    'mushrooms', 'extra cheese'
    ]
if 'mushrooms' in requested_toppings: print("Adding mushrooms.")
if 'pepperoni' in requested_toppings: print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: print("Adding extra cheese.")

# Adding mushrooms.
# Adding extra cheese.
# Finished making your pizza!

### Чтобы в программе выполнялся только один блок кода,
### используйте цепочку if-elif-else.
### Если же выполняться должны несколько блоков,
### используйте серию независимых команд if.
