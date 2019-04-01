# Не совсем правильное решение, смотреть PEP 8 style guide

# Recommended to use:
# if not seq:
# if seq:

# Not Recommended:
# if len(seq):
# if not len(seq):

requested_toppings = ['pizza']

if requested_toppings: # Возвращается True если в списке что то есть
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("Finished making your pizza!")
    else:
        print("Are you sure you want a plain pizza?")

print(requested_topping in requested_toppings)

# Adding pizza.
# Finished making your pizza!
# Are you sure you want a plain pizza?
# True
