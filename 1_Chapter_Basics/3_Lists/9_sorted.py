# Временная сортировка списка функцией sorted()
# Для временного представления:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the sorted list:")
print(sorted(cars))

# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']

print("Here is the original list again:")
print(cars)

# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']

# Передадим аргумент (reverse=True) в метод sorted():
print("Here is the reverse list by sorted:")
print(sorted(cars, reverse=True))

# Here is the reverse list by sorted:
# ['toyota', 'subaru', 'bmw', 'audi']
