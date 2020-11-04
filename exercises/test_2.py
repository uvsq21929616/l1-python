for i in range(1, 11):
    a = "*"*(10-i)
    print("{:>s}".format(a))


def NombreBissextile(années):
    a = années // 4
    return a


print(NombreBissextile(2020))


def TempsEnDateBissextile(temps):
    pass
