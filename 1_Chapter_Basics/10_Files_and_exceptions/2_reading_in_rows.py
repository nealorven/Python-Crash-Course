# Page 188
# Чтение по строкам

# В процессе чтения файла часто бывает нужно обработать каждую строку. Для
# последовательной обработки каждой строки в файле можно воспользоваться
# циклом for.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# 3.1415926535
#
#   8979323846
#
#   2643383279
