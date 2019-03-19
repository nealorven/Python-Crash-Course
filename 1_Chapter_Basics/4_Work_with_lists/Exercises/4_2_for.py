animals = ['tiger', 'lynx', 'cat']

for animal in animals:
    print(f"The {animal.title()} a good pet.")

print("These lists of animals are good: {}, {}, {}."
    .format(animals[0], animals[1], animals[2]))

# The Tiger a good pet.
# The Lynx a good pet.
# The Cat a good pet.
# These lists of animals are good: tiger, lynx, cat.

# Вариант интерполяции:
# print(f"These lists of animals are good: {animals[0]},
#                                          {animals[1]}, {animals[2]}.")
