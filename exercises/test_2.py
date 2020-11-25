for i in range(1, 11):
    a = "*"*(10-i)
    print("{:>s}".format(a))


def NombreBissextile(années):
    a = années // 4
    return a


print(NombreBissextile(2020))


def TempsEnDateBissextile(temps):
    pass


n = int(input("rentrer un entier"))
if n >= 12 and n < 1000:
    print("Gagné")

n = 6

i = 0

while i < n:

    a = n-i

    print("w" * a)

    i += 1

n, a = 10 ** 10, 5
b = 1
c = a*b*3
while c =< n:
    b += 1
print(b)
