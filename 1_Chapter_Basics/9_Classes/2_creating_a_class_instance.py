# Page 163
# Создание экземпляра класса

# Считайте, что класс — это своего рода инструкция по созданию экземпляров.
# Соответственно, класс Dog — инструкция по созданию экземпляров,
# представляющих конкретных собак.


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


# Создадим экземпляр my_dog, представляющий конкретную собаку:
my_dog = Dog('willie', 6)

# Для обращения к атрибутам экземпляра используется «точечная» запись.
# В данном случае Python обращается к экземпляру my_dog и ищет атрибут name,
# связанный с экземпляром my_dog.
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# My dog's name is Willie.
# My dog is 6 years old.

# Вызов методов. После создания экземпляра на основе класса Dog можно применять
# точечную запись для вызова любых методов, определенных в Dog:
my_dog.sit()
my_dog.roll_over()

# Willie is now sitting.
# Willie rolled over!
