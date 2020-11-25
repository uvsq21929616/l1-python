heure = 0
année = 2020
def date(heure, jour, année):
    minutes=int(input("rentrer un nombre"))
    if minutes//60>1:
        a=minutes//60
        b=minutes%60
        minute=b
        heure= heure+a
    else
    print("année:", année, "jour:", jour, "minutes:" minutes)
