# Page 148
# Изменение списка в функции

# Первое представление программы:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    # В цикле перемещаются объекы из списка в список
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Выводит имена объектов из списка completed_models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# Программа выводит тот же результат, что и версия без функций, но структура
# кода значительно улучшилась. Код, выполняющий бульшую часть работы, разнесен
# по двум разным функциям; это упрощает чтение основной части программы.

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

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Printing model: dodecahedron
# Printing model: robot pendant
# Printing model: iphone case

# The following models have been printed:
# dodecahedron
# robot pendant
# iphone case

# ПРИМЕЧАНИЕ
# Если вы пишете функцию и видите, что она решает слишком много разных задач,
# попробуйте разделить ее код на две функции. Помните, что функции всегда можно
# вызывать из других функций. Эта возможность может пригодиться для разбиения
# сложных задач на серию составляющих
