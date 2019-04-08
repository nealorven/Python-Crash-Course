class User:
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
        self.login_attempts = 0

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        reset_attempts = self.login_attempts = 0
        return reset_attempts

    def read_attempts(self):
        read_att = self.login_attempts
        return read_att


new_user = User('neal', 'orven')

new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)

print(new_user.read_attempts())
# 3

new_user.reset_login_attempts()
print(new_user.read_attempts())
# 0
