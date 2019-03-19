### Удаление элемента с использованием метода pop()
### Метод pop() удаляет последний элемент из списка,
### но позволяет работать с ним после удаления:
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print("The bike " + popped_motorcycle.title() + " is crushed.")

# The bike ['Suzuki'] is crushed.
