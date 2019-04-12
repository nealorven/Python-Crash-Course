# Page 181
# Импортирование модуля в модуль

from basic_car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
# 2016 Volkswagen Beetle

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
# 2016 Tesla Roadster
