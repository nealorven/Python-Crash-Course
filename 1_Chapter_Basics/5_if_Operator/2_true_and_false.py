### Использование and для проверки нескольких условий:
true = 0<1 and 1>0
false = 0>1 and 1<0
print(true)
print(false)

# True
# False

true_0 = (0<1)
true_1 = (1>0)
false_0 = [0>1]
false_1 = [1<0]
print(true_0 and true_1)
print(false_0 and false_1)

# True
# False

print(0>1)

# False

print(0<1 and true_1)

# True

trues = [
    (0==0), (0<1), (0<=1), (1>0), (1>=0)
    ]
lyings = [
    (0==1), (1<0), (1<=0), (0>1), (0>=1)
    ]

for true in trues:
    pass

print("All this tuple list have a 'True': ")

for lying in lyings:
    pass

print("All this tuple list have a 'False': ")

# ...
