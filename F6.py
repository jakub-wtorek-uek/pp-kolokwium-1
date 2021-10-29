from random import randint


def rand(froma, to):
    rando = randint(froma, to)

    while rando % 2 != 0 and rando % 3 != 0:
        rando = randint(froma, to)

    return rando
