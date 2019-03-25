mails = [
    'nealorven@gmail.com',
    'robertgreen@gmail.com',
    'alenfrojer@gmail.com',
    'boberon@gmail.com'
    ]
mail_search = input("Write postal address to search the database: ")

for mail in mails:
    if mail_search in mail:
        print(f"This email address: {mail} is in the database.")

print("This postal address is not found.")
