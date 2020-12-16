entiers = list(range(2, 21, 2))

for i in range(len(entiers)):
    if i < len(entiers) - 1:
        print(entiers[i] * entiers[i+1])
    else:
        pass
