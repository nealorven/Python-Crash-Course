# Page 161
# Создание и использование класса

# Классы позволяют моделировать практически все что угодно. Начнем с написания
# простого класса Dog, представляющего собаку — не какую-то конкретную, а собаку
# вообще.

# В каждом экземпляре, созданном на основе класса Dog, будет храниться кличка
# и возраст; кроме того, в нем будут присутствовать методы sit() и roll_over():


class Dog:
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        # Любая переменная с префиксом self доступна каждому методу в классе
        # и вы также сможете обращаться к этим переменным в каждом экземпляре,
        # созданном на основе класса.
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")