# Page 202
# Ошибки без уведомления пользователя

# Иногда при возникновении исключения программа должна просто проигнорировать
# сбой и продолжать работу, словно ничего не произошло, командой pass:


def count_words(file_name):
    """Подсчет приблизительного количества строк в файле."""
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        msg = f"The file {file_name} has about {str(num_words)} words."
        print(msg)


books = [
    'alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'
]

for book in books:
    count_words(book)

# The file alice.txt has about 64 words.
# The file moby_dick.txt has about 448 words.
# The file little_women.txt has about 256 words.
