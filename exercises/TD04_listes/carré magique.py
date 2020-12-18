carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    for i in range(len(carre)):
        print(carre[i])


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si 
        toutes les lignes ont la même somme, et -1 sinon """
    somme = []
    for i in range(len(carre)):
        a = 0
        for j in range(len(carre[i])):
            a = a + carre[i][j]
        somme.append(a)
    if somme[0] == somme[2] == somme[3] == somme[1]:
        print(somme[1])
    else:
        print(-1)


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si 
        toutes les colonnes ont la même somme, et -1 sinon """
    somme = []
    for j in range(len(carre[1])):
        a = 0
        for i in range(len(carre)):
            a = a + carre[i][j]
        somme.append(a)
    if somme[0] == somme[1] == somme[2] == somme[3]:
        print(somme[0])
    else:
        print(-1)
    return


print(testLignesEgales(carre_pas_mag))
