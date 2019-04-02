# Page 145
# Возвращение словаря

# Функция может вернуть любое значение, нужное вам, в том числе и более сложную
# структуру данных.
# Функцию можно легко расширить так, чтобы она принимала дополнительные
# значения: — второе имя, возраст, профессию или любую другую информацию.

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# {'first': 'jimi', 'last': 'hendrix', 'age': 27}
