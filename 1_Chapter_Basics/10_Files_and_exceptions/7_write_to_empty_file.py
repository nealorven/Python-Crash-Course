# Page 193
# Запись в пустой файл

# Файлы можно открывать в режиме:
# ('r') чтения,
# ('w') записи,
# ('a') присоединения,
# ('r+') чтение и запись.

# Если аргумент режима не указан, Python по умолчанию открывает файл в режиме
# только для чтения.
# Если файл, открываемый для записи, еще не существует, функция open()
# автоматически создает его.

# Будьте внимательны, открывая файл в режиме записи ('w'):
# если файл существует, то Python уничтожит его данные перед возвращением
# объекта файла.

file_name = 'programming.txt'

# 'w' файл должен быть открыт в режиме записи.
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")

# Чтение записи из текстового файла.
with open(file_name) as text_file:
    each_lines = text_file.readlines()

print(each_lines)

# ['I love programming.']

for each_line in each_lines:
    print(each_line)

# I love programming.

# ПРИМЕЧАНИЕ
# Python может записывать в текстовые файлы только строковые данные. Если вы
# захотите сохранить в текстовом файле числовую информацию, данные придется
# предварительно преобразовать в строки функцией str().
