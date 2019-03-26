# Метод keys используется для получания списка ключей без значений

favorite_languages = {
    'jen': 'ruby',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi {}, i see your favorite language is {}!"
        .format(name.title(), favorite_languages[name].title()))

# Jen
# Sarah
# Hi Sarah, i see your favorite language is C!
# Edward
# Phil
# Hi Phil, i see your favorite language is Python!
