## Zadanie 1.

(F1.py) Zdefiniuj funkcję stars(n), która zwraca n znaków gwiazdek w postaci łańcucha znakowego.<br>
Przykład: stars(5) => "*****" 

    def stars(n):
        return "*" * n

<br>

## Zadanie 2.

(F2.py) Zdefiniuj funkcję in(n,from,to), która zwraca prawdę (True), jeśli podana liczba n należy do 
przedziału <from,to>.<br>
Przykład: in(3,2,5) => True

    def ina(n, froma, to):
        return froma <= n <= to

<br>

## Zadanie 3.

(F3.py) Zdefiniuj funkcję max4(n1,n2,n3,n4), która zwraca największą z czterech podanych liczb 
n1,n2,n3,n4.<br> 
Przykład: max4(5,8,2,7) => 8 

    def max4(n1, n2, n3, n4):
        return max([n1, n2, n3, n4])

<br>

## Zadanie 4.

(F4.py) Zdefiniuj funkcję coins(price), która zwraca minimalną liczbę monet 1, 2 lub 5 zł, za pomocą 
których można przedstawić price, które jest liczbą typu całkowitego.<br>
Przykład: coins(23) => 6 

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

<br>

## Zadanie 5.

(F5.py) Zdefiniuj funkcję bool(), która zwraca losowo prawdę lub fałsz (True lub False).<br>
Przykład: bool() => True 

    from random import randint


    def bool():
        rando = randint(0, 1)
        return False if rando == 1 else True

<br>

## Zadanie 6.

(F6.py) Zdefiniuj funkcję rand(from,to), która zwraca losową liczbę z podanego przedziału <from,to>, 
która jest podzielna przez 2 oraz przez 3 bez reszty.<br>
Przykład: rand(10,50) => 36

    from random import randint


    def rand(froma, to):
        rando = randint(froma, to)

        while rando % 2 != 0 and rando % 3 != 0:
            rando = randint(froma, to)

    return rando

<br>

## Zadanie 7.

(F7.py) W pierwszych pięciu latach pracy pracownik otrzymuje dodatek stażowy w wysokości 100 zł 
za każdy przepracowany rok, a w kolejnych trzech latach 200 zł za każdy przepracowany rok. W 
pozostałych latach dodatek wynosi 50 zł za każdy przepracowany rok. Zdefiniuj funkcję bonus(years), 
która dla podanych lat pracy years zwróci wielkość dodatku stażowego.<br>
Przykład: bonus(9) => 1150

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

<br>