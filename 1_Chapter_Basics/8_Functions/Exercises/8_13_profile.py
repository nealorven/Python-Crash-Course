def build_profile(first, last, **user_info):
    user_profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        user_profile[key] = value
    return user_profile


new_profile = build_profile('neal', 'orven',
                            mail='nealorven@gmail.com',
                            location='new york')
print(new_profile)

# {'first_name': 'neal',
# 'last_name': 'orven',
# 'mail': 'nealorven@gmail.com',
# 'location': 'new york'}
