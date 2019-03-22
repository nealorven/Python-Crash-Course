dictionary = {
    1:'one',
    2:'two',
    3:'three'
    }
print("dictionary.items():")
number = input("Enter number 1..3: ")
for key, value in dictionary.items():
    #if dictionary[key] is value: print("They are the same object.")
    if dictionary[key] == number:
        print(f"Num: {value}.")
    else:
        print("They are different.")
