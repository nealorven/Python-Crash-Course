foods = [
    'pizza', 'falafel', 'carrot cake',
    'cannoli', 'ice cream'
    ]
for food in foods:
    print(f"Each the food is good: {food.title()}")

foods_str = ", ".join(foods)
print(f"All foods: {foods_str.title()}.")

# Each the food is good: Pizza
# Each the food is good: Falafel
# Each the food is good: Carrot Cake
# Each the food is good: Cannoli
# Each the food is good: Ice Cream
# All foods: Pizza, Falafel, Carrot Cake, Cannoli, Ice Cream.
