# Вместо того чтобы полностью прерывать выполнение цикла без выполнения
# оставшейся части кода, вы можете воспользоваться командой continue для
# возвращения к началу цикла и проверке условия.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # Отсеивает числа кратные двум
        continue
    print(current_number)

# 1
# - continue
# 3
# - continue
# 5
# - continue
# 7
# - continue
# 9

number = 0
while number <=4:
    number += 1
    if number == 2:
        continue
    print(number)

# 1
# Пропущенная цифра командой continue
# 3
# 4
# 5
