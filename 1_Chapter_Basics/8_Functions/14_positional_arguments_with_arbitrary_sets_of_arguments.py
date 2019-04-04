# Page 153
# Использование произвольного набора именованных аргументов

#                                ↓ Принимает информацию и вносит в словарь
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    # profile = {}
    # profile['first_name'] = first
    # profile['last_name'] = last
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# {'first_name': 'albert',
# 'last_name': 'einstein',
# 'location': 'princeton',
# 'field': 'physics'}
