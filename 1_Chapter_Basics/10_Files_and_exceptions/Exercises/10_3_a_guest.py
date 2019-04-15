guest_name = 'guest.txt'

with open(guest_name, 'w') as guest_object:
    input_guest = input("Enter guest name: ")
    guest_object.write(input_guest.title())

with open(guest_name, 'r') as check_name:
    names_lists = check_name.readlines()

print(names_lists)

# Enter guest name: neal
# ['Neal']

for names_list in names_lists:
    print(names_list)

# Neal
