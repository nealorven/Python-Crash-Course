# Page 194
# Многострочная запись

# Файлы можно открывать в режиме:
# ('r') чтения,
# ('w') записи,
# ('a') присоединения,
# ('r+') чтение и запись.

file_name = 'programming.txt'
# Режим записи
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

with open(file_name) as text_file:
    each_lines = text_file.readlines()

for each_line in each_lines:
    print(each_line)

# I love programming.I love creating new games.

with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(file_name) as text_file:
    each_lines = text_file.readlines()

for each_line in each_lines:
    print(each_line.rstrip())

# I love programming.
# I love creating new games.
