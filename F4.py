def coins(price):
    sum_of_coins = 0

    while price - 5 >= 0:
        price -= 5
        sum_of_coins += 1

    while price - 2 >= 0:
        price -= 2
        sum_of_coins += 1

    while price - 1 >= 0:
        price -= 1
        sum_of_coins += 1

    return sum_of_coins
