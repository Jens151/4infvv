from datetime import date
huidig_jaar = date.today().year
geboorte_jaar = int(input("In welk jaar ben je geboren?: "))
leeftijd = (huidig_jaar - geboorte_jaar)
print: leeftijd
