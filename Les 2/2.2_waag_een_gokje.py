from random import randrange
nummer = (randrange(10) + 1)
geraden_nummer = int(input("Raad een getal tussen 1 en 10: "))
if geraden_nummer == nummer:
    print("Gewonnen! Het getal was " + str(nummer) + ".")
else:
    print("Helaas het getal was " + str(nummer) + ".")
