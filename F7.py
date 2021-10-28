def bonus(years):
    if years <= 5:
        return 100 * years

    total_bonus = 500

    if years <= 8:
        return total_bonus + 200 * (years - 5)

    total_bonus += 600
    years -= 8

    while years > 0:
        total_bonus += 50
        years -= 1

    return total_bonus
