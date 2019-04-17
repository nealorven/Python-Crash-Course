
def create_files(file_name):
    with open(file_name, 'w') as file_object:
        file_object.write("I love programming.")


def read_files(file_name):
    try:
        with open(file_name) as file_object:
            each_words = file_object.readline()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} does not exist.")
    else:
        print(f"file {file_name} contains: {each_words}")


file_name_1 = 'cats.txt'
read_files(file_name_1)
# file cats.txt contains: capanno salvichi mewcarlo

file_name_2 = 'mouses.txt'
read_files(file_name_2)
# Sorry, the file mouses.txt does not exist.

list_animals = [
    'cats.txt', 'dogs.txt', 'mouses.txt'
    ]
for list_animal in list_animals:
    read_files(list_animal)

# file cats.txt contains: capanno salvichi mewcarlo
# file dogs.txt contains: bob ben beb
# Sorry, the file mouses.txt does not exist.
