# Page 190
# Работа с содержимым файла

# После того как файл будет прочитан в память, вы сможете обрабатывать данные
# так, как считаете нужным. Для начала попробуем построить одну строку со всеми
# цифрами из файла без промежуточных пропусков

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# Для хранения строк.
pi_string = ''
for line in lines:
    # Записываем построчно данные.
    pi_string += line.rstrip()

print(pi_string)
# 3.1415926535  8979323846  2643383279

print(len(pi_string))
# 36

# ПРИМЕЧАНИЕ
# Читая данные из текстового файла, Python интерпретирует весь текст в файле как
# строку. Если вы читаете из текстового файла число и хотите работать с ним в
# числовом контексте, преобразуйте его в целое число функцией int() или в
# вещественное число функцией float().
