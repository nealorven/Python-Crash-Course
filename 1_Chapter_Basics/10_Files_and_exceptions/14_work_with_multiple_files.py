# Page 201
# Работа с несколькими файлами

# Добавим еще несколько файлов с книгами для анализа. Но для начала переместим
# основной код программы в функцию с именем count_words(). Это упростит
# проведение анализа для нескольких книг:


def count_words(file_name):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = f"Sorry, the file {file_name} does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        msg = f"The file {file_name} has about {str(num_words)} words."
        print(msg)


file_name_1 = 'siddhartha.txt'
count_words(file_name_1)
# Sorry, the file siddhartha.txt does not exist.

file_name_2 = 'alice.txt'
count_words(file_name_2)
# The file alice.txt has about 64 words.

books = [
    'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'
    ]
for book in books:
    count_words(book)
# The file alice.txt has about 64 words.
# Sorry, the file siddhartha.txt does not exist.
# The file moby_dick.txt has about 448 words.
# The file little_women.txt has about 256 words.
