# Page 170
# Наследование.

# Один класс, наследующий от другого, автоматически получает все атрибуты и
# методы первого класса. Исходный класс называется родителем, а новый класс —
# потомком. Класс-потомок наследует атрибуты и методы родителя, но при этом
# также может определять собственные атрибуты и методы.

# Метод __init__() класса-потомка.

# Первое, что делает Python при создании экземпляра класса-потомка,
# присваивает значения всем атрибутам класса-родителя. Для этого методу
# __init__() класса-потомка необходима помощь со стороны родителя.


class Car:
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Имя super происходит из распространенной терминологии: класс-родитель
# называется суперклассом, а класс-потомок — субклассом.
class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 2016 Tesla Model S
