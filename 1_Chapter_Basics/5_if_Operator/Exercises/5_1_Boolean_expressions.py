car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

# Is car == 'subaru'? I predict True.
# True

# is car == 'audi'? I predict False.
# False


true = True and True
if true == True:
    print(true)

false = True and False
if false == False:
    print(false)

# True
# False

print("\n1. Example: True.")

mails = [
    'nealorven@gmail.com',
    'robertgreen@gmail.com',
    'alenfrojer@gmail.com',
    'boberon@gmail.com'
    ]
for mail in mails:
    if mail == 'nealorven@gmail.com':
        print(f"This mailing address: {mail} is listed.")

# This mailing address: nealorven@gmail.com is listed.

print("\n2. Example: True.")

names = {
    'neal orven':'nealorven@gmail.com',
    'robert green':'robertgreen@gmail.com',
    'alen frojer':'alenfrojer@gmail.com',
    'bob eron':'boberon@gmail.com'
    }
for name, mail in names.items():
    if name == 'neal orven' and mail == 'nealorven@gmail.com':
        print("This mail address: {} belongs to {}."
                                .format(mail, name.title()))
    else:
        print(f"User with this mail is not found.")
        break

# This mail address: nealorven@gmail.com belongs to Neal Orven.
# User with this mail is not found.
