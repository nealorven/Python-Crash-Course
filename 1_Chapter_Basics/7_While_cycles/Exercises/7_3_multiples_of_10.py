number = input("Enter a multiple of 10: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {str(number)} is multiple.")
else:
    print(f"\nThe number {str(number)} not multiple.")

# Enter a multiple of 10: 101
# The number 101 not multiple.

# Enter a multiple of 10: 110
# The number 110 is multiple.
