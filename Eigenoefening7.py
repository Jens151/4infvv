from random import randrange

nummer1 = randrange(20) + 1
teller = 1

gekozen_nummer = int(input("Raad een willekeurig getal tussen 1 en 20: "))

while gekozen_nummer != nummer1:
    if gekozen_nummer < 1 or gekozen_nummer > 20:
        print("Niet geldige input")

    elif gekozen_nummer > nummer1:
        print("Het getal is lager")

    else:
        print("Het getal is hoger")

    gekozen_nummer = int(input("Raad nog een getal: "))
    teller = teller + 1

print("Je hebt juist geraden")
print("Je had", teller, "pogingen nodig.")
