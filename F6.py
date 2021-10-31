from random import randint


def rand(froma, to):
    rando = randint(froma, to)

    while rando % 6 != 0:
        rando = randint(froma, to)

    return rando
