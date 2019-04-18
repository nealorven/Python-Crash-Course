
def read_file(file_name):
    """reading files."""
    try:
        with open(file_name) as file_object:
            each_words = file_object.readline()
    except FileNotFoundError:
        pass
    else:
        print(f"file {file_name} contains: {each_words}")


file_name_0 = 'mouses.txt'
read_file(file_name_0)
