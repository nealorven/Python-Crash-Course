sandwich_orders = [
    'pastrami',
    'hot dog',
    'pastrami',
    'hamburger',
    'pastrami',
    'cheeseburger'
    ]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("Pastrami is no more.")

while sandwich_orders:
    sorted_foods = sandwich_orders.pop()
    print(f"Sandwiches are preparing: {sorted_foods.title()}")
    finished_sandwiches.append(sorted_foods)

for finished_sandwich in finished_sandwiches:
    print(f"Finished foods: {finished_sandwich.title()}")

# Pastrami is no more.
# Sandwiches are preparing: Cheeseburger
# Sandwiches are preparing: Hamburger
# Sandwiches are preparing: Hot Dog
# Finished foods: Cheeseburger
# Finished foods: Hamburger
# Finished foods: Hot Dog
