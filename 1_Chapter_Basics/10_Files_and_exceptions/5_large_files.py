# Page 191
# Большие файлы: миллион цифр

# До настоящего момента мы ограничивались анализом текстового файла, который
# состоял всего из трех строк, но код этих примеров будет работать и с намного
# большими файлами.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
# 3.14159265358979323846264338327950288419716939937510...

print(len(pi_string))
# 51199

# ПРИМЕЧАНИЕ
# Python не устанавливает никаких ограничений на длину данных, с которыми
# вы можете работать. Она ограничивается разве что объемом памяти вашей
# системы.