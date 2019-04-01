sandwich_orders = [
    'hot dog',
    'hamburger',
    'cheeseburger'
    ]
finished_sandwiches = []

while sandwich_orders:
    sorted_foods = sandwich_orders.pop()
    print(f"Sandwiches are preparing: {sorted_foods.title()}")
    finished_sandwiches.append(sorted_foods)

for finished_sandwich in finished_sandwiches:
    print(f"Cooked sandwiches: {finished_sandwich.title()}")

# Sandwiches are preparing: Cheeseburger
# Sandwiches are preparing: Hamburger
# Sandwiches are preparing: Hot Dog
# Cooked sandwiches: Cheeseburger
# Cooked sandwiches: Hamburger
# Cooked sandwiches: Hot Dog
