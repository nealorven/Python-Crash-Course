# Page 139
# Именованные аргументы

# Именованный аргумент представляет собой пару «имя—значение», передаваемую
# функции. Имя и значение связываются с аргументом напрямую, так что при
# передаче аргумента путаница с порядком исключается, а также проясняют роль
# каждого значения в вызове функции.

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# I have a hamster.
# My hamster's name is Harry.

# I have a hamster.
# My hamster's name is Harry.

# ПРИМЕЧАНИЕ
# При использовании именованных аргументов будьте внимательны — имена должны
# точно совпадать с именами параметров из определения функции.
