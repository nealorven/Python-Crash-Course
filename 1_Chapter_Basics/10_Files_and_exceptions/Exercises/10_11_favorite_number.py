import json


def write_data():
    user_request = input("Write any data: ")
    data_file = 'data.json'

    with open(data_file, 'w') as f_obj:
        json.dump(user_request, f_obj)
    return user_request


def read_data():
    file_name = 'data.json'
    try:
        with open(file_name) as f_obj:
            data_out = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return data_out


def control_data():
    data_out = read_data()

    if data_out:
        print("Ur old data: " + data_out)
    else:
        data_out = write_data()
        print(f"New data read: " + data_out)


control_data()
