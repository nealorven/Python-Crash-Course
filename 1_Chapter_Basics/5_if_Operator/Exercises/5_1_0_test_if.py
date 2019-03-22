mails = [
    'nealorven@gmail.com',
    'robertgreen@gmail.com',
    'alenfrojer@gmail.com',
    'boberon@gmail.com'
    ]
mail_search = input("Write postal address to search the database: ")

for mail in mails:
    if mail == mail_search:
        print(f"This email address: {mail} is in the database.")
        break
    else:
        print("This postal address is not found.")
        break
