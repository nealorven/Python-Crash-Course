names = {
    'neal orven':'nealorven@gmail.com',
    'robert green':'robertgreen@gmail.com',
    'alen frojer':'alenfrojer@gmail.com',
    'bob eron':'boberon@gmail.com'
    }
name_search = input("Write your username to search for a mailing address: ")

for name, mail in names.items():
    if name == name_search:
        print(f"This user: {name.title()} owns this email address: {mail}.")
        break
    else:
        print(f"User with this mail is not found.")
        break

# Найти адрес почты по пользователю +
# Найти пользователя по майл адресу
