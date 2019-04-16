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
        # Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        msg = f"The file {file_name} has about {str(num_words)} words."
        print(msg)


filename_1 = 'alice.txt'
count_words(filename_1)
# Sorry, the file alice.txt does not exist.

filename_2 = 'text.txt'
count_words(filename_2)
# The file text.txt has about 64 words.
