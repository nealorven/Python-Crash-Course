import time

# Пишем цикл for с оператором if else:
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    # Начало измерения времени программы
    start_time = time.time()
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    # Конец измерения времени программы
    end_time = time.time()
# Вывод времени работы программы
print(end_time-start_time)

# Audi
# BMW
# Subaru
# Toyota
# 0.0
