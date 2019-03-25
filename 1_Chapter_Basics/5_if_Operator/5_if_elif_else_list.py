requested_toppings = [
    'mushrooms',
    'green peppers',
    'extra cheese'
    ]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.
# Finished making your pizza!

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!")

# Adding mushrooms.
# Sorry, we are out of green peppers right now.
# Adding extra cheese.
# Finished making your pizza!
