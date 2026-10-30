getal1 = float(input("Geef getal 1: "))
getal1 = float(input("Geef getal 2: "))
bewerking_naar_keuze = input("Welke bewerking wil je gebruiken, kies uit: optellen, aftrekken, vermenigvuldigen, delen of machten: ")
if bewerking_naar_keuze == "optellen":
    print("Het resultaat is: ", getal1 + getal2)
if bewerking_naar_keuze == "aftrekken":
    print("Het resultaat is: ", getal1 - getal2)
if bewerking_naar_keuze == "vermenigvuldigen":
    print("Het resultaat is: ", getal1 * getal2)
if bewerking_naar_keuze == "delen":
    print("Het resultaat is: ", getal1 / getal2)
if bewerking_naar_keuze == "machten":
    print("Het resultaat is: ", getal1 ** getal2)
else:
    print("Ongeldig teken") 
