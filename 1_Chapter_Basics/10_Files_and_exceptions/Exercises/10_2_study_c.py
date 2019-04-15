file_name = 'learning_python.txt'

with open(file_name) as text_file:
    each_lines = text_file.readlines()

print(each_lines)
# ['In Python you can make a program\n',
# 'In Python you can make clear code\n',
# 'In Python you can get a good job']

format_lines = ''
for each_line in each_lines:
    # Без метода .rstrip() данные выводятся построчно.
    # Для замены слоов: each_line.replace('Python', 'C')
    format_lines += each_line

print(format_lines)
# In Python you can make a program
# In Python you can make clear code
# In Python you can get a good job

print(format_lines.replace('Python', 'C'))
# In C you can make a program
# In C you can make clear code
# In C you can get a good job
