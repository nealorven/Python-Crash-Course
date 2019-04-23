# Page 210
# Тестирование функции

# Данный код можно протестить на правильность работы

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

# Please give me a first name: neal
# Please give me a last name: orven
# 	Neatly formatted name: Neal Orven.
#
# Please give me a first name: neal orven
# Please give me a last name:
