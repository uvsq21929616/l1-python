carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    for i in range(len(carre)):
        print(carre[i])


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    for i in range(len(carre)):
        a = 0
        for j in range(len(carre[i])):
            a = a + carre[i][j]
