
def create_new_user():
    guest_book = 'guest_book.txt'

    while True:
        prompt = "\nEnter 'exit' to end the program. "
        prompt += "\nEnter guest name: "
        with open(guest_book, 'a') as book_object:
            message = input(prompt)
            format_name = f"{message}\n"
            book_object.write(format_name)
        if message == 'exit':
            break

    with open(guest_book, 'r') as check_book:
        name_lists = check_book.readlines()

    print("Display all names from a saved list:")
    for name_list in name_lists:
        print(name_list.title().rstrip())

    print("Output naked list:")
    print(name_lists)


create_new_user()

# Enter 'exit' to end the program.
# Enter guest name: neal
#
# Enter 'exit' to end the program.
# Enter guest name: eva
#
# Enter 'exit' to end the program.
# Enter guest name: exit
# Display all names from a saved list:
# Neal
# Eva
# Exit
# Output naked list:
# ['neal\n', 'eva\n', 'exit\n']
