# Page 165
# Создание нескольких экземпляров

# Одной из первых задач станет изменение атрибутов, связанных с конкретным
# экземпляром. Атрибуты экземпляра можно изменять напрямую или же написать
# методы, изменяющие атрибуты по особым правилам.


class Car:
    """Простая модель автомобиля."""

    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        # Назначение атрибуту значения по умолчанию.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}."
        # Вызов данной функции выводится только через print()
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
        При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
# 2016 Audi A4.

my_new_car.read_odometer()
# This car has 0 miles on it.

# Прямое изменение значения атрибута
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# This car has 23 miles on it.

# Изменение значения атрибута с использованием метода.
my_new_car.update_odometer(25)
my_new_car.read_odometer()
# This car has 25 miles on it.

# Проверим условие в функции update_odometer.
my_new_car.update_odometer(20)
my_new_car.read_odometer()
# You can't roll back an odometer!
# This car has 25 miles on it.

# Изменение значения атрибута с приращением
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
# 2013 Subaru Outback.

my_used_car.update_odometer(23500)
my_used_car.read_odometer()
# This car has 23500 miles on it.

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# This car has 23600 miles on it.

# ПРИМЕЧАНИЕ
# Подобные методы управляют обновлением внутренних значений экземпляров
# (таких, как показания одометра), однако любой пользователь, имеющий
# доступ к программному коду, сможет напрямую задать атрибуту любое значение.
# Эффективная схема безопасности должна уделять особое внимание таким
# подробностям, не ограничиваясь простейшими проверками.
