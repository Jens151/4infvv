seconden = float(input("Hoeveel seconden tel je tussen bliksem en donder?: "))
afstand = seconden * 343 / 1000
if afstand < 3:
    print("Het onweer is ongeveer " + str(round(afstand, 1)) + " km ver.")
    print("Opgelet! Het onweer is dichtbij, ga snel naar binnen.")
elif afstand >= 3:
    print("Het onweer is ongeveer " + str(round(afstand, 1)) + " km ver.")
