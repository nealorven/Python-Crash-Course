# Page 194
# Присоединение данных к файлу

# Если файл еще не существует, то Python автоматически создаст пустой файл.
# Файлы можно открывать в режиме:
# ('r') чтения,
# ('w') записи,
# ('a') присоединения,
# ('r+') чтение и запись.

file_name = 'programming.txt'
# Режим присоединения
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

with open(file_name) as file_object:
    each_lines = file_object.readlines()

for each_line in each_lines:
    print(each_line.rstrip())

# I love programming.
# I love creating new games.
# I also love finding meaning in large datasets.
# I love creating apps that can run in a browser.
