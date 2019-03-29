# Цикл for получает коллекцию элементов и выполняет блок кода по одному разу
# для каждого элемента в коллекции. В отличие от него, цикл while продолжает
# выполняться, пока остается истинным некоторое условие.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# Инициализация пустой строки, которая передается каждый раз в цикл
message = ""

while message != 'quit':
    message = input(prompt)
    # Оператор if что бы не выводилось сообщение quit после цикла while
    if message != 'quit':
        print(message)

# Tell me something, and I will repeat it back to you:
# Enter 'quit' to end the program.
