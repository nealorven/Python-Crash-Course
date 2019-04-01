# Объявляем кортеж для переменной и используем цикл:
dishes = (
    'pelmeny', 'vareniky', 'borsh',
    'salat', 'desert'
    )
for dish in dishes:
    print(dish.title())

# Добавить новый элемент методом .append не получится:
""" dishes.append('kakaha') """
# Traceback (most recent call last):
#   File "4_13_tuples.py", line 6, in <module>
#     dishes.append('kakaha')
# AttributeError: 'tuple' object has no attribute 'append'

# Присвоить новый элемент тоже не получится:
""" dishes[0] = 'kakaha' """
# Traceback (most recent call last):
#   File "4_13_tuples.py", line 12, in <module>
#     dishes[0] = 'kakaha'
# TypeError: 'tuple' object does not support item assignment

print(dishes)

# ('pelmeny', 'vareniky', 'borsh', 'salat', 'desert')

# Замена картежа с присвоением нового:
new_dishes = (
    'pelmihany', 'varenikany', 'borshevsky',
    'salatecky', 'desertsky'
    )
dishes = new_dishes

for dish in dishes:
    print(dish.title())
# Вставка элементов списка в строку.
list_dish = ", ".join(dishes)
print(f"New menu: {list_dish.title()}.")

# Pelmihany
# Varenikany
# Borshevsky
# Salatecky
# Desertsky
# New menu: Pelmihany, Varenikany, Borshevsky, Salatecky, Desertsky.
