numbers = {
    'jen': [2, 4, 6, 3],
    'sarah': [7, 2, 8, 3],
    'edward': [8, 1, 2, 4],
    'phil': [0, 2, 9, 6]
    }
for name, number in numbers.items():
    print(f"{name.title()}: ")

    for num in number:
        print(f"{num}")

# Jen:
# 2
# 4
# 6
# 3
# Sarah:
# 7
# 2
# 8
# 3
# Edward:
# 8
# 1
# 2
# 4
# Phil:
# 0
# 2
# 9
# 6
