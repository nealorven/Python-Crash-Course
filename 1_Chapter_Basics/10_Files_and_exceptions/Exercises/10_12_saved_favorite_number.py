import json


def write_num():
    user_request = input("Write best number: ")
    data_file = 'numbers.json'

    with open(data_file, 'w') as f_obj:
        json.dump(user_request, f_obj)
    return user_request


def read_num():
    file_name = 'numbers.json'
    try:
        with open(file_name) as f_obj:
            data_out = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return data_out


def control_num():
    data_out = read_num()

    if data_out:
        print("Old number: " + data_out)
    else:
        data_out = write_num()
        print(f"New number read: " + data_out)


control_num()
