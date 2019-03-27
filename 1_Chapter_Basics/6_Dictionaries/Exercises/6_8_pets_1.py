kuzya = {
    'cat': 'neal'
    }
bobby = {
    'dog': 'den'
    }
kitty = {
    'tiger': 'michael'
    }
pets = [
    kuzya, bobby, kitty
    ]
for pet in pets:
    for animal, owner in pet.items():
        print("The animal: {}, owner: {}."
            .format(animal.title(), owner.title()))

# The owner of this Cat is Neal.
# The owner of this Dog is Den.
# The owner of this Tiger is Michael.

# Попробовать имя питомца определить в строку вывода.
