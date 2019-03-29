order = "How many places do you need to book?: "
place = int(input(order))

if place <= 8:
    print("Your table is ready.")
else:
    print("We don't have so many places.")

# How many places do you need to book?: 8
# Your table is ready.
