# Page 192
# Проверка дня рождения

file_name = 'pi_digits.txt'

with open(file_name) as file_project:
    lines = file_project.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mm-dd-yy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Enter your birthday, in the form mm-dd-yy: 060691
# Your birthday does not appear in the first million digits of pi.
