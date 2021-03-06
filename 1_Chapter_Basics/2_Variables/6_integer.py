# Целые числа

addition = [2+3, 3-2, 2*3, 3/2]
for i in addition:
    print(i)

# 5
# 1
# 6
# 1.5

degree = [3**2, 3**3, 10**6]
for i in degree:
    print(i)

# 9
# 27
# 1000000

num_0 = 2+3*4
num_1 = (2+3)*4
print(num_0)
print(num_1)

# 14
# 20

# Вещественные числа  «числами с плавающей точкой»

numbers = [0.1+0.1, 0.2+0.2, 2*0.1, 2*0.2 ]
for i in numbers:
    print(i)

# 0.2
# 0.4
# 0.2
# 0.4

# Однако в некоторых ситуациях вдруг оказывается, что результат
# содержит неожиданно большое количество разрядов в дробной части:
# >>> 0.2 + 0.1
# 0.30000000000000004
# >>> 3 * 0.1
# 0.30000000000000004
# Python пытается подобрать как можно более точное представление результата, что иногда
# бывает нелегко из-за особенностей внутреннего представления чисел в компьютерах.

age = 23
message = "Happy " + str(age) + "'rd Birthday!"
print(message)

# Преобразование числа в строку
# Для этого переменная передается функции str(),
# преобразующей не-строковые значения к строковому виду:
# Happy 23'rd Birthday!
