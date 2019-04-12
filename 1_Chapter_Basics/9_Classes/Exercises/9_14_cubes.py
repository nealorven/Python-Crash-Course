from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, rolls=1):
        print(*[randint(1, self.sides) for _ in range(rolls)])

    # print(i for i in range(101))

    # for row in range(1,6):
    #     for col in range(row):
    #         print('*', end="")
    #     print('')


d1 = Die()  # 6-sided dice
d1.roll_dice(10)  # 10 rolls

d2 = Die(10)
d2.roll_dice(10)

d3 = Die(20)
d3.roll_dice(10)

# 2 5 1 1 2 6 3 3 2 5
# 6 5 5 5 5 5 10 3 5 8
# 9 18 2 14 19 7 5 13 6 5
