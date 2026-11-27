from random import randrange
nummer1 = randrange(10) + 1
gekozen_nummer = int(input("Raad een willekeurig getal tussen 1 en 10: "))
if gekozen_nummer < 1 or gekozen_nummer > 10:
    print("Ongeldige input")
elif gekozen_nummer > nummer1:
    print("Het getal is lager")
    gekozen_nummer2 = int(input("Raad nog een getal: "))
    if gekozen_nummer2 == nummer1:
        print("Je hebt juist geraden")
    else:
        print("Fout, het nummer was " + str(nummer1) + ".")
elif gekozen_nummer < nummer1:
    print("Het getal is hoger")
    gekozen_nummer2 = int(input("Raad nog een getal: "))
    if gekozen_nummer2 == nummer1:
        print("Je hebt juist geraden")
    else:
        print("Fout, het nummer was " + str(nummer1) + ".")
elif gekozen_nummer == nummer1:
    print("Je hebt juist geraden")