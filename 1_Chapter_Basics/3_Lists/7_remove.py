# Удаление элементов используя метод remove()
# Метод remove() удаляет только первое вхождение заданного значения:

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']

# Удаляет значение 'ducati' и выводит причину удаления:
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("A " + too_expensive.title() + " is too expensive for me.")

# ['honda', 'yamaha']
# A ['Suzuki'] is too expensive for me.
# Значение ['Suzuki'] было удалено из списка, но продолжает храниться в переменной too_expensive.
