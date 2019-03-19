persons = ['roma', 'misha', 'sasha']

for invitation in persons:
    print("Welkome to dinner Mr.", invitation.title())

off_person = "sasha"
old_person = persons.remove(off_person)
new_person = persons.append('Igor')
print(off_person.title() + " will not come to visit.\n")

for invitation in persons:
    print("Welcome to dinner", invitation.title())

print("Three more guests will come.\n")
persons.insert(0, 'Nikolay')
persons.insert(2, 'Zhora')
persons.append('Grigoriy')

for invitation in persons:
    print("Welcome to dinner Mr.", invitation.title())

print("There will be only 2 guests.\n")
not_invited = persons.pop()
print(f"Sorry Mr.{not_invited} you are not invited.")
not_invited = persons.pop()
print(f"Sorry Mr.{not_invited} you are not invited.")
not_invited = persons.pop()
print(f"Sorry Mr.{not_invited} you are not invited.")
not_invited = persons.pop()
print("Sorry Mr.{} you are not invited.\n".format(not_invited))

for valid in persons:
    print("Mr." + valid.title() + " your invitation remains valid.")

del persons[0]
del persons[0]
print(persons)

"""
Welkome to dinner Roma
Welkome to dinner Misha
Welkome to dinner Sasha
Sasha will not come to visit.

Welcome to dinner Roma
Welcome to dinner Misha
Welcome to dinner Igor
Three more guests will come.

Welcome to dinner Nikolay
Welcome to dinner Roma
Welcome to dinner Zhora
Welcome to dinner Misha
Welcome to dinner Igor
Welcome to dinner Grigoriy
There will be only 2 guests.

Sorry Grigoriy you are not invited.
Sorry Igor you are not invited.
Sorry Misha you are not invited.
Sorry Zhora you are not invited.

Nikolay your invitation remains valid.
Roma your invitation remains valid.
[]
"""
