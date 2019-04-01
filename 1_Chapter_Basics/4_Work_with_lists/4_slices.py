# Чтобы вывести первые три элемента списка, запросите индексы
# с 0 по 3, и вы получите элементы 0, 1 и 2.
#              |          =>         |
#              0          1          2           3        4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# ['charles', 'martina', 'michael']
#                         |          =>          |
#              0          1          2           3        4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# ['martina', 'michael', 'florence']

# Если первый индекс среза не указан, то Python
# автоматически начинает срез от начала списка:
#              |                =>               |
#              0          1          2           3        4
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# ['charles', 'martina', 'michael', 'florence']

# Аналогичный синтаксис работает и для срезов,
# включающих конец списка:
#                                    |          =>        |
#              0          1          2          4         5
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# ['michael', 'florence', 'eli']

# Например, чтобы отобрать последних трех игроков,
# используйте срез players[-3:]
#                                    |          <=         |
#                        -3         -2          -1        0
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# ['michael', 'florence', 'eli']

# В следующем примере программа перебирает первых трех
# игроков и выводит их имена:
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Here are the first three players on my team:
# Charles
# Martina
# Michael
