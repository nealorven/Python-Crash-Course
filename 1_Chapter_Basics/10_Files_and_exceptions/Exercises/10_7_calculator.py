
while True:
    print("Press 'q' to exit.")
    num_1 = input("Enter first number: ")
    if num_1 == 'q':
        break
    num_2 = input("Enter second number: ")

    try:
        addition = int(num_1) + int(num_2)
    except ValueError:
        print("Enter numbers to add.")
    else:
        print(f"sum of addition: {addition}\n")

# Press 'q' to exit.
# Enter first number: 1
# Enter second number: 2
# sum of addition: 3
#
# Press 'q' to exit.
# Enter first number: q
