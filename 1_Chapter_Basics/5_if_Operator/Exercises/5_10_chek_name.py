current_users = [
    'neal', 'admin', 'boris', 'yana', 'dima', 'dana'
    ]
new_users = [
    'neal', 'admin', 'boris', 'misha', 'yegor', 'marina'
    ]
for new_user in new_users:
    if new_user in current_users:
        print(f"This name: {new_user.title()}, already exists!")
    else:
        print(f"This name: {new_user.title()}, is free.")
