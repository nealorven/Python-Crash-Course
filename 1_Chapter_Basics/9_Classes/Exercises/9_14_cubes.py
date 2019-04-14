from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    #def roll_die(self, sides):
    #    rolls = randint(1, sides)
    #    x = print(rolls)

    def roll_dice(self, rolls=1):
        print(*[randint(1, self.sides) for _ in range(rolls)])


d1 = Die()  # 6-sided dice
d1.roll_dice(10)  # 10 rolls
# 2 5 1 1 2 6 3 3 2 5

d2 = Die(10)
d2.roll_dice(10)
# 6 5 5 5 5 5 10 3 5 8

d3 = Die(20)
d3.roll_dice(10)
# 9 18 2 14 19 7 5 13 6 5
