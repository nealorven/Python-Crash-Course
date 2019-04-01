# Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
# хотели провести отпуск. Включите блок кода для вывода результатов опроса.

# 1. Объявление словаря куда будут записываться данные.
# 2. Объявить флаг и цикл while.
# 3.    Написать запросы от пользователя.
# 4.    Написать условие записи запросов пользователя в кортеж
# 5.    Написать условие if для опроса пользователя о продолжении опроса или нет
# 6. Написать цикл for для переборки кортежа и вывода данных в консоль

responses = {}
dream_active = True
while dream_active:
	name = input("\nWhats your name?: ")
	place = input("Where do you want to go to rest?: ")
	responses[name] = place
	repeat = input("continue vacation planning? (yes/no): ")
	if repeat == 'yes': dream_active = True
	elif repeat == 'no': dream_active = False
	else: print("You entered an incorrect answer.")
	break
print("\nPlaces for rest:")
for name, place in responses.item():
	print("{} plans to go to {}"
		.format(name.capitalize(), place.title()))
