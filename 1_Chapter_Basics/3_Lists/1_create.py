# Рекомендуется присваивать спискам имена во множественном числе:
# letters, digits, names
# Заносить элементы в список в простой форме, пример: 'trek' а не 'Trek'
# что бы было удобно выводить данные
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# ['trek', 'cannondale', 'redline', 'specialized']

# Вызов из списка первого элемента:
print(bicycles[0])

# trek

# Также можно использовать строковые методы:
print(bicycles[0].title())

# Trek

# В Python также существует специальный синтаксис для обращения к последнему
# элементу списка. Если запросить элемент с индексом –1:
print(bicycles[-1])

# specialized

# Использование отдельных элементов из списка
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# My first bicycle was a Trek.
