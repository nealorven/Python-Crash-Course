# Page 198
# Обработка исключения FileNotFoundError

# Одна из стандартных проблем при работе с файлами — отсутствие необходимых
# файлов. Тот файл, который вам нужен, может находиться в другом месте, в имени
# файла может быть допущена ошибка, или файл может вообще не существовать.
# Все эти ситуации достаточно прямолинейно обрабатываются в блоках try-except.

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)

# Sorry, the file alice.txt does not exist.

with open(filename) as f_obj:
    contents = f_obj.read()

# Traceback (most recent call last):
#   File 12_FileNotFoundError_exception_handling.py", line 11, in <module>
#     with open(filename) as f_obj:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
