
num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

try:
    addition = int(num_1) + int(num_2)
except ValueError:
    print("Enter numbers to add.")
else:
    print(f"sum of addition: {addition}")

# Enter first number: a
# Enter second number: 2
# Enter numbers to add.
