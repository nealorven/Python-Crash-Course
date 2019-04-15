
answers_list = 'answers_list.txt'

while True:
    prompt = "Why do you like programming?: "
    with open(answers_list, 'a') as list_object:
        message = input(prompt)
        format_text = f"{message}\n"
        list_object.write(format_text)
    if message == 'exit':
        break

with open(answers_list, 'r') as read_object:
    each_rows = read_object.readlines()

for each_row in each_rows:
    print(each_row.rstrip())

# Why do you like programming?: i like to write clear code
# Why do you like programming?: i want to write clean and useful code
# Why do you like programming?: exit
# i like to write clear code
# i want to write clean and useful code
# exit
