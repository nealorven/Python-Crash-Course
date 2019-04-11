from basic_car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 2016 Audi A4

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This car has 23 miles on it.
