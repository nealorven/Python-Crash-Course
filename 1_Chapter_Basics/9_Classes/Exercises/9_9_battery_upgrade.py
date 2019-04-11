class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = 80
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())

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
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    # мощности аккумулятора
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    # Запас хода для аккумулятора.
    def get_range(self):
        global range_kwh
        if self.battery_size <= 70:
            range_kwh = 250
        elif self.battery_size >= 85:
            range_kwh = 270
        message = f"This car can go approximately {range_kwh}"
        message += " miles on a full charge."
        print(message)

    # Обнавляет можность аккумулятора.
    def upgrade_battery(self):
        self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Атрибут как экземпляр.
        self.battery = Battery()

    # Переопределение методов класса-родителя
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")


model_s = ElectricCar('tesla', 'model s', 2017)
model_s.get_descriptive_name()
# 2017 Tesla Model S

model_s.battery.get_range()
# This car can go approximately 250 miles on a full charge.

model_s.battery.upgrade_battery()
model_s.battery.get_range()
# This car can go approximately 270 miles on a full charge.

model_s.battery.get_range()
# This car can go approximately 270 miles on a full charge.
