# Page 140
# Значения по умолчанию

# Если при вызове функции передается аргумент, соответствующий данному
# параметру, Python использует значение аргумента, если нет, то по умолчанию.
# Если вы заметили, что большинство вызовов describe_pet() используется для
# описания собак, задайте animal_type значение по умолчанию 'dog'.

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')

# I have a dog.
# My dog's name is Willie.

describe_pet('willie')

# I have a dog.
# My dog's name is Willie.

# Так как аргумент для параметра animal_type задан явно, Python игнорирует
# значение параметра по умолчанию.
describe_pet(pet_name='harry', animal_type='hamster')

# I have a hamster.
# My hamster's name is Harry.

# ПРИМЕЧАНИЕ
# Если вы используете значения по умолчанию, все параметры со значением по умо-
# лчанию должны следовать после параметров, у которых значений по умолчанию нет.
# Это необходимо для того, чтобы Python правильно интерпретировал позиционные
# аргументы.
