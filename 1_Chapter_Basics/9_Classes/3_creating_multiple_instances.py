# Page 164
# Создание нескольких экземпляров

# На основе класса можно создать столько экземпляров, сколько вам потребуется.
# Создадим второй экземпляр Dog с именем your_dog:


class Dog:
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")


# В этом примере создаются два экземпляра с именами Willie и Lucy. Каждый
# экземпляр обладает своим набором атрибутов и способен выполнять действия
# из общего набора:

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# My dog's name is Willie.
# My dog is 6 years old.
# Willie is now sitting.
#
# Your dog's name is Lucy.
# Your dog is 3 years old.
# Lucy is now sitting.

# ПРИМЕЧАНИЕ
# Даже если второй собаке будут назначены те же имя и возраст, Python все
# равно создаст отдельный экземпляр класса Dog. Вы можете создать сколько
# угодно экземпляров одного класса при условии, что эти экземпляры хранятся
# в переменных с разными именами или занимают разные позиции в списке или
# словаре:
