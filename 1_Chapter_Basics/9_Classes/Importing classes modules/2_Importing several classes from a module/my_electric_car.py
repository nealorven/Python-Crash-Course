# Page 179
# Импортирование нескольких классов из модуля

from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# 2016 Tesla Model S

my_tesla.battery.describe_battery()
# This car has a 60-kWh battery.

my_tesla.battery.get_range()
# This car can go approximately <class 'range'> miles on a full charge.
