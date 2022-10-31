import random

frank = []
sam = []
tom = []


def input_nb(plr, plr1, plr2):
    x = 0
    number = random.randint(0, 11)
    while x < 4:
        if number in plr1 or number in plr2 or number in plr:
            number = random.randint(0, 11)
        else:
            plr.append(number)
            x += 1
    plr.sort()
    return plr


frank = input_nb(frank, sam, tom)
sam = input_nb(sam, frank, tom)
tom = input_nb(tom, sam, frank)

