behaald_punt = float(input("Hoeveel punten heb je behaald?: "))
punten_toets = float(input("Op hoeveel punten ging de toets?: "))
punt = behaald_punt / punten_toets * 100
if punt >= 50:
    print("Je hebt " + str(round(punt,1)) + "%")
    print("Proficiat, je bent geslaagd!")
elif punt < 50:
    print("Je hebt " + str(round(punt,1)) + "%")
    print("Jammer, je bent niet geslaagd.")
