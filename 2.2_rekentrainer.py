from random import randrange
nummer1 = (randrange(10) + 1)
nummer2 = (randrange(10) + 1)
som = (nummer1 * nummer2)
berekening = int(input("Hoeveel is " + str(nummer1) + " x " + str(nummer2) + "?: "))
if berekening == som:
    print("Juist, het antwoord was: " + str(som) + ".")
else:
    print("Fout! Het juiste antwoord is " + str(som) + ".")
