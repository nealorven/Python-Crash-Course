names = {
    'robert green':'robertgreen@gmail.com',
    'neal orven':'nealorven@gmail.com',
    'alen frojer':'alenfrojer@gmail.com',
    'bob eron':'boberon@gmail.com'
    }
name_search = input("Write your username to search for a mailing address: ")

for name, mail in names.items():
    if name_search in name:
        print(f"User: {name_search.title()} owns this email address: {mail}.")

# Дописать вывод отсутствия имени и почты
