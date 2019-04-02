# Page 141
# Эквивалентные вызовы функций

# Так как...
# 'позиционные аргументы'
# 'именованные аргументы'
# 'значения по умолчанию'
# могут использоваться одновременно, часто существуют несколько эквивалентных
# способов вызова функций.

# При таком определении аргумент для параметра pet_name должен задаваться в
# любом случае, но это значение может передаваться как в позиционном, так и в
# именованном формате.
#                               ↓ значения по умолчанию
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Все следующие вызовы являются допустимыми для данной функции:
describe_pet('willie')

# I have a dog.
# My dog's name is Willie.

describe_pet(pet_name='willie')

# I have a dog.
# My dog's name is Willie.

#               ↓         ↓ Позиционные аргументы
describe_pet('harry', 'hamster')

# I have a hamster.
# My hamster's name is Harry.

#                   ↓                   ↓ Именованные аргументы
describe_pet(pet_name='harry', animal_type='hamster')

# I have a hamster.
# My hamster's name is Harry.

describe_pet(animal_type='hamster', pet_name='harry')

# I have a hamster.
# My hamster's name is Harry.

# ПРИМЕЧАНИЕ
# На самом деле не так важно, какой стиль вызова вы используете.
# Если ваша функция выдает нужный результат, выберите тот стиль,
# который вам кажется более понятным.
