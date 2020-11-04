# temps[0]: jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

import time


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
    g = e // 30
    h = e % 30
    i = g // 12
    j = g % 12
    print(i, "années", j, "mois", h, "jours")
    print(f, "heures", d, "minutes", b, "secondes")


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


def DemandeTemps(jours, heures, minutes, secondes):
    jours = int(input("rentrer un nombre de jours"))
    heures = int(input("entrer un nombre d'heures"))
    minutes = int(input("rentrer un nombre de minutes"))
    secondes = int(input("rentrer un nombre de secondes"))
    print(str(jours)+"jours")
    if heures//24 == 0:
        print(str(heures)+"heures")
    else:
        print("error")
        heures = int(input("rentrer une heure"))
        return
    if minutes//60 == 0:
        print(str(minutes)+"minutes")
    else:
        print("error")
        minutes = int(input("rentrer une minutes"))
        return
    if secondes//60 == 0:
        print(str(secondes)+"secondes")
    else:
        print("error")
        secondes = int(input("rentrer une seconde"))
        return


def SommeTemps(temps1, temps2):
    jours_1 = int(input("rentrer un nombre de jours1"))
    jours_2 = int(input("rentrer un nombre de jours2"))
    heures_1 = int(input("rentrer un nombre de heures 1"))
    heures_2 = int(input("rentrer un nombre de heures 2"))
    minutes_1 = int(input("rentrer un nombre de minutes 1"))
    minutes_2 = int(input("rentrer un nombre de minutes 2"))
    secondes_1 = int(input("rentrer un nombre de secondes 1"))
    secondes_2 = int(input("rentrer un nombre de secondes 2"))
    temps1 = tempsEnSeconde(jours_1, heures_1, minutes_1, secondes_1)
    temps2 = tempsEnSeconde(jours_2, heures_2, minutes_2, secondes_2)
    temps = temps1+temps2
    temps_final = secondeEnTemps(temps)
    return temps_final


def ProportionTemps(temps1, proportion):
    jours = int(input("rentrer un nombre de jours"))
    heures = int(input("rentrer un nombre d'heures"))
    minutes = int(input("rentrer un nombre de minutes"))
    secondes = int(input("rentrer un nombre de secondes"))
    temps1 = tempsEnSeconde(jours, heures, minutes, secondes)
    proportion = float(input("rentrer une proportion"))
    temps2 = int(temps1*proportion)
    temps_final = secondeEnTemps(temps2)
    return temps_final


a = int(time.time())


def TempsEnDate(a):
    temps1 = secondeEnTemps(a)
    return temps1


def bissextile(jours):
    a = jours // 365
    b = a // 4
    return b


print(bissextile(20000)


def NombreBissextile(années):
    a = années // 4
    return a


print(NombreBissextile(2020))


def TempsEnDateBissextile(temps):
    secondeEnTemps(temps)
    NombreBissextile(i)
    print 

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDateBisextile(temps))