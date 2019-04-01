# Page 132
# Удаляет все вложенные значения 'cat' из списка

pets = [
    'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'
    ]
print(pets)

# Цикл повторяется пока в списке присутствует значение 'cat'
while 'cat' in pets:
    pets.remove('cat')

print(pets)

# ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ['dog', 'dog', 'goldfish', 'rabbit']
