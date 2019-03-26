# Создаем кортеж с вложенными списками.

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', 'php'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are: ")
    # Перебираем списки вложенные в кортежи.
    for language in languages:
        print(f"{language.title()}")

# Jen's favorite languages are:
# Python
# Ruby
# Sarah's favorite languages are:
# C
# Php
# Edward's favorite languages are:
# Ruby
# Go
# Phil's favorite languages are:
# Python
# Haskell
