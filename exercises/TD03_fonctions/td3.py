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
    a=temps[0]
    b=temps[1]
    c=temps[2]
    d=temps[3]
    if 


afficheTemps((1, 0, 14, 23))
