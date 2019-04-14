# Page 182
# Стандартная библиотека Python

# Для примера рассмотрим класс OrderedDict из модуля collections.
# Если вы хотите создать словарь, но при этом сохранить порядок добавления пар
# «ключ—значение», воспользуйтесь классом OrderedDict из модуля collections.

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print("{}'s favorite language is {}."
          .format(name.title(), language.title()))

# Jen's favorite language is Python.
# Sarah's favorite language is C.
# Edward's favorite language is Ruby.
# Phil's favorite language is Python.

print(favorite_languages)

# OrderedDict([
#   ('jen', 'python'),
#   ('sarah', 'c'),
#   ('edward', 'ruby'),
#   ('phil', 'python')])
