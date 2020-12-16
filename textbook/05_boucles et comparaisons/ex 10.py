N = int(input("donnez un nombre"))
i = 0

while i < N + 1:
    a = " " * (N - i)
    b = "*" * i
    print(a + b + "*" + b + a)
    i += 1
