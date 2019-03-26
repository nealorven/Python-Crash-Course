# Метод values используется для получания списка значений без ключей

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for language in favorite_languages.values():
    print(language.title())

# Python
# C
# Ruby
# Python
