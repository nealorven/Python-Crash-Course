# Page 153
# Использование произвольного набора именованных аргументов

# Иногда программа должна получать произвольное количество аргументов, но вы
# не знаете заранее, какая информация будет передаваться функции. В таких
# случаях можно написать функцию, получающую столько пар «ключ—значение»

#                                ↓ Принимает информацию и вносит в словарь
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    # profile = {}
    # profile['first_name'] = first
    # profile['last_name'] = last
    # Попробовать сделать два параллельных словаря
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


<<<<<<< HEAD
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
=======
user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics')

>>>>>>> 22c3f03323503d9ac99e218539a693f5367169ef
print(user_profile)

# {
# 'first_name': 'albert',
# 'last_name': 'einstein',
# 'location': 'princeton',
# 'field': 'physics'
# }
