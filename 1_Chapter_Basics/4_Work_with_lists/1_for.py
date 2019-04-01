# Цикл for может содержать сколько угодно строк кода:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.
 title() + ".\n")

# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.

# David, that was a great trick!
# I can't wait to see your next trick, David.

# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Это пример логической ошибки. Код имеет действительный синтаксис,
# но он не приводит к желаемому результату, не путать с синтаксической.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() +
    ".\n")

# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.

# Синтаксическая ошибка, пропущенный отступ:
#   File "magicians.py", line 3
#     print(magician)
"""       ^                                """
# IndentationError: expected an indented block

# Синтаксическая ошибка, лишний отступ:
#   File "magicians.py", line 3
#     print(magician)
"""   ^                                    """
# IndentationError: expected an indented block
