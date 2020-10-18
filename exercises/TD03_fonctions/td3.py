# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes


def tempsEnSeconde(jours, heures, minutes, secondes):
    """ Renvoie la valeur en seconde de temps ."""
    a = jours*24
    b = (heures+a)*60
    c = (minutes+b)*60
    d = (secondes+c)
    return d


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(3, 23, 1, 34))


def secondeEnTemps(seconde):
    a = seconde // 60
    b = seconde % 60
    c = a // 60
    d = a % 60
    e = c // 24
    f = c % 24
    print(e, "jours", f, "heures", d, "minutes", b, "secondes")


temps = secondeEnTemps(100000)


def afficheTemps(temps):
    a = temps[0]
    b = temps[1]
    c = temps[2]
    d = temps[3]
    liste_1 = [a, b, c, d]
    liste_2 = ["jours", "heures", "minutes", "secondes"]
    liste_3 = ["jour", "heure", "minute", "seconde"]
    i = 0
    while i < 4:
        if liste_1[i] == 1:
            print(str(liste_1[i])+liste_3[i])
        elif liste_1[i] == 0:
            print(" ")
        else:
            print(str(liste_1[i])+liste_2[i])
        i += 1


afficheTemps((1, 8, 14, 23))


jours = int(input("rentrer un nombre de jours"))
heures = int(input("entrer un nombre d'heures"))
minutes = int(input("rentrer un nombre de minutes"))
secondes = int(input("rentrer un nombre de secondes"))


def AfficherTemps(jours, heures, minutes, secondes):
    print(str(jours)+"jours")
    if heures//24 == 0:
        print(str(heures)+"heures")
    else:
        print("error")
        return
    if minutes//60 == 0:
        print(str(minutes)+"minutes")
    else:
        print("error")
        return
    if secondes//60 == 0:
        print(str(secondes)+"secondes")
    else:
        print("error")
        return


AfficherTemps(jours, heures, minutes, secondes)
