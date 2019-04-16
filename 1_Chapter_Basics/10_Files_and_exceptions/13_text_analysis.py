# Page 199
# Анализ текста

# Метод split() разделяет строку на части по всем позициям, в которых
# обнаружит пробел, и сохраняет все части строки в элементах списка.
# В результате создается список слов, входящих в строку. Для подсчета
# слов в книге мы воспользуемся вызовом split() для всего текста, а
# затем подсчитаем элементы списка, чтобы получить примерное количество
# слов в тексте:

filename = 'text.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()

except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)

else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    msg = f"The file {filename} has about {str(num_words)} words."
    print(msg)

# The file text.txt has about 64 words.
