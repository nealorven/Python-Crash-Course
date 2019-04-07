class User:
    def __init__(self, first_name, last_name, **user_info):
        self.f_name = first_name
        self.l_name = last_name
        self.u_info = user_info

    def describe_user(self):
        """Напишите метод describe_user(), который выводит сводку с
        информацией о пользователе."""
        profile = {'first_name': self.f_name, 'last_name': self.l_name}
        for key, value in self.u_info.items():
            profile[key] = value
        for label, content in profile.items():
            print("{}: {}.".format(label, content))

    def greet_user(self):
        """Создайте еще один метод greet_user() для вывода персонального
        приветствия для пользователя."""
        pass


new_user = User('neal', 'orven', mail_addr='nealorven@gmail.com', age=27)
print(new_user.describe_user())

# first_name: neal.
# last_name: orven.
# mail_addr: nealorven@gmail.com.
# age: 27.
# None
