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
        # Атрибуты
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = 80
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Переопределение методов класса-родителя
    def fill_gas_tank(self):
        gas = self.gas_tank
        return gas


class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=68):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""

        #global range_kwh
        if self.battery_size >= 70:
            range_kwh = 248
        elif self.battery_size <= 85:
            range_kwh = 274

        message = f"This car can go approximately {range_kwh}"
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        # Добавляем атрибут с именем self.battery и создаем экземпляр Battery()
        # Теперь любой экземпляр ElectricCar будет иметь автоматически
        # создаваемый экземпляр Battery.
        # Экземпляры как атрибуты
        self.battery = Battery()

    # Переопределение методов класса-родителя
    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# 2016 Tesla Model S
# This car doesn't need a gas tank!
# This car has a 70-kWh battery.
# This car can go approximately 240 miles on a full charge.
