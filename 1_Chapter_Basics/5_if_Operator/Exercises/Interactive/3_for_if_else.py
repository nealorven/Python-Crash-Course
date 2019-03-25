dictionary = {
    1:'one',
    2:'two',
    3:'three'
    }
number = input("Enter number 1-3: ")

for key, value in dictionary.items():
    if key == int(number):
        print(f"Num: {value}.")
        break
    else:
        print("They are different.")
        break

# Поправить
