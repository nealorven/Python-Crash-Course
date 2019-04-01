# Page 137
# Позиционные аргументы

# Значения, связываемые с аргументами подобным образом,
# называются позиционными аргументами.

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My {}'s name is {}.".format(animal_type, pet_name.title()))

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# I have a hamster.
# My hamster's name is Harry.

# I have a dog.
# My dog's name is Willie.
