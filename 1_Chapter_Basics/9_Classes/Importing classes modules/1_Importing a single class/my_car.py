<<<<<<< HEAD:1_Chapter_Basics/9_Classes/Importing a single class/my_car.py
=======
# Page 177
# Импортирование одного класса

>>>>>>> 8b9a517ad9a7e862e5e249a1870b5a806f7f92a8:1_Chapter_Basics/9_Classes/Importing classes modules/1_Importing a single class/my_car.py
from basic_car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 2016 Audi A4

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This car has 23 miles on it.
