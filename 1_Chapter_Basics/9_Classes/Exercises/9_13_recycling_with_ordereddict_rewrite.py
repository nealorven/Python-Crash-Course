from collections import OrderedDict

# Создаем экземпляр класса и наполняем словарь.
languages = OrderedDict()
languages['python'] = 'dynamic'
languages['ruby'] = 'dynamic'
languages['go'] = 'static'

print(languages)
# OrderedDict([('python', 'dynamic'), ('ruby', 'dynamic'), ('go', 'static')])

for lang, lang_type in languages.items():
    print("{}: {}.".format(lang.title(), lang_type.title()))

# Python: Dynamic.
# Ruby: Dynamic.
# Go: Static.
