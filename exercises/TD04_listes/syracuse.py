def syracuse(n):
    valeurs_1 = []
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        valeurs_1.append(n)
    return valeurs_1


print(syracuse(6))

valeurs_2 = []


def testeConjecture(n_max):
    while n_max > 1:
        if n_max % 2 == 0:
            n_max = n_max // 2
        else:
            n_max = n_max * 3 + 1
        valeurs_2.append(n_max)
    a = (valeurs_2[-1] == 1)
    return a


valeurs_3 = []


def tempsVol(n):
    vol = 0
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        valeurs_3.append(n)
        vol = vol+1
    return vol


def tempsVolListe(n_max):
    temps = []
    while n_max >= 1:
        b = tempsVol(n_max)
        temps += [b]
        n_max = n_max - 1
    return temps


i = 1
while i < 10000:
    tempsVol(i)
    if tempsVol(i) == 261:
        print(i)
    i = i+1


def altitudeMax(n):
    valeurs_4 = []
    while n > 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        valeurs_4.append(n)
    valeurs_4.sort()
    return valeurs_4[-1]


valeurs_5 = []


def altitudeMaxList(n_max):
    altitude = []
    for n_max in range(n_max, 1, -1):
        n = n_max
        liste = []
        liste.append(n)
        while n > 1:
            if n % 2 == 0:
                n = n//2
            else:
                n = n*3+1
            liste.append(n)
        liste.sort()
        altitude.append(liste[-1])
    return altitude


print(altitudeMaxList(3))
