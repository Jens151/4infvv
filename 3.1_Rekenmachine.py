getal1 = round(float(input("Geef getal 1: ")),2)
bewerking_naar_keuze = input("Welke bewerking wil je gebruiken, kies uit: optellen, aftrekken, vermenigvuldigen, delen of machten: ")
getal2 = round(float(input("Geef getal 2: ")),2)
if getal2 == 0 and bewerking_naar_keuze == "delen":
    print("Delen door nul gaat niet.")
if bewerking_naar_keuze == "optellen":
    resultaat = getal1 + getal2
    print(str(getal1)+ " + " + str(getal2) + " = " + str(round(resultaat,2)))
elif bewerking_naar_keuze == "aftrekken":
    resultaat = getal1 - getal2
    print(str(getal1)+ " - " + str(getal2) + " = " + str(round(resultaat,2)))
elif bewerking_naar_keuze == "vermenigvuldigen":
    resultaat = getal1 * getal2
    print(str(getal1)+ " * " + str(getal2) + " = " + str(round(resultaat,2)))
elif bewerking_naar_keuze == "delen":
    resultaat = getal1 / getal2
    print(str(getal1)+ " / " + str(getal2) + " = " + str(round(resultaat,2)))
elif bewerking_naar_keuze == "machten":
    resultaat = getal1 ** getal2
    print(str(getal1)+ " ** " + str(getal2) + " = " + str(round(resultaat,2)))
else:
    print("Deze bewerking ken ik niet.")
