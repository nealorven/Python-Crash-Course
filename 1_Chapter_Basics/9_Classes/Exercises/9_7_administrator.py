class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
        self.login_attempts = 0
        self.privileges = [
            'allowed to add messages',
            'allowed to delete users',
            'allowed to ban users'
            ]

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        reset_attempts = self.login_attempts = 0
        return reset_attempts

    def read_attempts(self):
        read_att = self.login_attempts
        return read_att

    def show_privileges(self):
        privileges = self.privileges
        for privilege in privileges:
            print(f"Privilege: {privilege}.")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


administrator = Admin('neal', 'orven')
administrator.show_privileges()

# Privilege: allowed to add messages.
# Privilege: allowed to delete users.
# Privilege: allowed to ban users.
