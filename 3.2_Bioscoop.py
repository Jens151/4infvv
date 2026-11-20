from datetime import date
huidig_jaar = date.today().year
geboorte_jaar = int(input("In welk jaar ben je geboren?: "))
leeftijd = huidig_jaar - geboorte_jaar
print("Dit jaar word je", leeftijd, "jaar.")
if leeftijd < 12:
    print("Je mag naar films voor alle leeftijden.")
elif leeftijd <= 15:
    print("Je mag naar films vanaf 12 jaar.")
elif leeftijd <= 17:
    print("Je mag naar films vanaf 16 jaar.")
else:
    print("Je mag naar alle films.")
