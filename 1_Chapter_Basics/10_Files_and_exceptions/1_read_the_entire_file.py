# Page 186
# Чтение всего файла

with open('python_work/text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 3.1415926535
# 8979323846
# 2643383279
