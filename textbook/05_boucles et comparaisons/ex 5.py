notes = [14, 9, 6, 8, 12]

a = 0

for i in notes:
    a = a+i

b = a / len(notes)

print("{:.2f}".format(b))
