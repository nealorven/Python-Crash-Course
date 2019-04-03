# Page 150
# Запрет изменения списка в функции

# Синтаксис среза [:] создает копию списка для передачи функции. Если удаление
# элементов из списка unprinted_designs в print_models.py нежелательно, функцию
# print_models() можно вызвать так:
# имя_функции(имя_списка[:]) или
# print_models(unprinted_designs[:], completed_models)

# Передаем два списка в функцию с прямым обращением аргумента:
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        # В цикле перемещаются объекы из списка в список
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # Выводит имена объектов из списка completed_models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Объявляем списки
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Синтаксис среза [:] создает копию списка для передачи функции
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case

# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case

print(unprinted_designs)
# Список unprinted_designs сохранился
# ['iphone case', 'robot pendant', 'dodecahedron']
