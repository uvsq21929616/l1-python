jours=int(input("rentrer un nombre de jours"))
heures=int(input("rentrer un nombre d'heures"))
minutes=int(input("rentrer un nombre de minutes"))
secondes=int(input("rentrer un nombre de secondes"))
temps1=tempsEnSeconde(jours,heures,minutes,secondes)
proportion=float(input("rentrer une proportion"))


def ProportionTemps(temps1,proportion):
    temps2=temps1*proportion
    temps_final=secondeEnTemps(temps2)
    return temps_final

ProportionTemps(temps1,proportion)

