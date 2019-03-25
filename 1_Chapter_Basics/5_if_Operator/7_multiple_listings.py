### Множественные списки:

# Доступное дополнение
available_toppings = [
    'mushrooms', 'olives', 'green peppers',
    'pepperoni', 'pineapple', 'extra cheese'
    ]
# Заказанное дополнение
requested_toppings = [
    'mushrooms', 'french fries', 'extra cheese'
    ]
# Перебирает список заказанных дополнений
for requested_topping in requested_toppings:
    # Проверяем каждое заказанное дополнение в списке доступных
    if requested_topping in available_toppings:
        # Если дополнение доступно
        print(f"Adding {requested_topping}.")
    else:
        # Если дополнение не доступно
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")

# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.
# Finished making your pizza!
