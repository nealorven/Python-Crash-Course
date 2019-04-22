import json

prompt = "\nEnter your name to continue the session."
prompt += "\nPress 'q' to Exit or 'enter' to Next: "

while True:
    user_prompt = input(prompt)

    def get_new_username():
        """Должен выполнять четкую функцию записи нового юзера."""
        username = input("Enter your account name again: ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        return username


    def get_stored_username():
        """Только проверяет наличие пользователя."""
        file_name = 'username.json'
        try:
            with open(file_name) as f_obj:
                user_name = json.load(f_obj)
        except FileNotFoundError:
            return None
        else:
            return user_name


    def user_check():
        user_name = get_stored_username()
        if user_name is not None:

            user_verification = input("Enter name to continue the session: ")
            if user_name == user_verification:
                print("You are logged in as {}".format(user_name.title()))

            user_answer = input("To continue working (y/n): ")
            if user_answer == 'y':
                register_user = get_new_username()
                print("{}, you are logged in with your account."
                      .format(register_user.title()))
            else:
                print("You are currently logged in as {}."
                      .format(user_name.title()))
        else:
            print("You are logged in as {}.".format(user_name.title()))


    if user_prompt == 'q':
        break

    user_check()

# Все слишком сложно шо пздц
