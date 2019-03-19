countries = ['usa', 'netherlands', 'australia', 'germany', 'france']

print("Original list:")
print(countries)
# Original list:
# ['usa', 'netherlands', 'australia', 'germany', 'france']

print("Sorted list:")
print(sorted(countries))
# Sorted list:
# ['australia', 'france', 'germany', 'netherlands', 'usa']

print("Original list:")
print(countries)
# Original list:
# ['usa', 'netherlands', 'australia', 'germany', 'france']

print("Sorted list with reverse:")
print(sorted(countries, reverse=True))
# Sorted list with reverse:
# ['usa', 'netherlands', 'germany', 'france', 'australia']

print("Original list:")
print(countries)
# Original list:
# ['usa', 'netherlands', 'australia', 'germany', 'france']

print("First .reverse method:")
countries.reverse()
print(countries)
# First .reverse method:
# ['france', 'germany', 'australia', 'netherlands', 'usa']

print("Second .reverse method:")
countries.reverse()
print(countries)
# Second .reverse method:
# ['usa', 'netherlands', 'australia', 'germany', 'france']

print("Use method .sort():")
countries.sort()
print(countries)
# Use method .sort():
# ['australia', 'france', 'germany', 'netherlands', 'usa']

print("\nUse method .sort(reverse=True):")
countries.sort(reverse=True)
print(countries)
# Use method .sort(reverse=True):
# ['usa', 'netherlands', 'germany', 'france', 'australia']
