# Page 143
# Необязательные аргументы

# Иногда бывает удобно сделать аргумент необязательным, чтобы разработчик,
# использующий функцию, мог передать дополнительную информацию только в том
# случае, если он этого захочет.

# Python интерпретирует непустые строки как истинное значение, и, если при
# вызове задан аргумент второго имени, middle_name дает результат True.

# Необязательные значения позволяют функциям работать в максимально широком
# спектре сценариев использования без усложнения вызовов.

#                                необязательный аргумент ↓
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name}, {middle_name}, {last_name}"
    else:
        full_name = f"{first_name}, {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Jimi Hendrix

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# John Lee Hooker

# ПРИМЕЧАНИЕ
# При использовании второго имени придется проследить за тем, чтобы второе имя
# было последним из передаваемых аргументов. Это необходимо для правильного
# связывания позиционных аргументов в строке.
