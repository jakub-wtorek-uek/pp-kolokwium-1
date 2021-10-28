from random import randint


def rand(from, to):
    rando = randint(from, to)

    while rando % 2 != 0 and rando % 3 != 0:
        rando = randint(from, to)

    return rando
