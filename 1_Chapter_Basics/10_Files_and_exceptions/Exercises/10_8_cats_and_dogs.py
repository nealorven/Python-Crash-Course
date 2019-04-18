class File:
    """Create, read, edit file."""
    def __init__(self, file_name):
        self.file_name = file_name

    def create_files(self):
        """File creation."""
        with open(self.file_name, 'w') as file_object:
            file_object.write("I love programming.")

    def read_file(self):
        """Reading files."""
        try:
            with open(self.file_name) as file_object:
                each_words = file_object.readline()
        except FileNotFoundError:
            print(f"Sorry, the file {self.file_name} does not exist.")
        else:
            print(f"file {self.file_name} contains: {each_words}")

    def read_files(self):
        """Reading files from the list."""
        with open(self.file_name) as f_obj:
            contents = f_obj.readline()
        for content in contents:
            print(f"{content.rstrip()}")

    def count_words(self):
        """Counting letters."""
        try:
            with open(self.file_name) as f_obj:
                contents = f_obj.read()
        except FileNotFoundError:
            pass
        else:
            words = contents.split()
            num_words = len(words)
            msg = f"The file {self.file_name} has about {str(num_words)} words."
            print(msg)


file_name_0 = 'cats.txt'
new_file_0 = File(file_name_0)
new_file_0.read_file()
# file cats.txt contains: capanno salvichi mewcarlo

file_name_1 = 'mouses.txt'
new_file_1 = File(file_name_1)
new_file_1.read_file()
# Sorry, the file mouses.txt does not exist.

animals = [
    'cats.txt', 'dogs.txt'
    ]
