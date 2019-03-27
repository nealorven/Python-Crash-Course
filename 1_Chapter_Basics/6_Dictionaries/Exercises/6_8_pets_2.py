pets = {
    'kuzya': {
        'cat': 'neal'
        },
    'bobby': {
        'dog': 'den'
        },
    'kitty': {
        'tiger': 'michael'
        },
    }
for pet_name, description in pets.items():
    print(f"Pet name: {pet_name.title()}.")

    for animal, owner in description.items():
        print("Animal: {}, owner: {}."
            .format(animal.title(), owner.title()))

# Pet name: Kuzya.
# Animal: Cat, owner: Neal.
# Pet name: Bobby.
# Animal: Dog, owner: Den.
# Pet name: Kitty.
# Animal: Tiger, owner: Michael.
