x = int(input("Geef een getal: "))
y = int(input("Geef nog een getal: "))
z = input("Welke bewerking wil je gebruiken, kies uit: optellen, aftrekken, vermenigvuldigen en delen: ")
if z == "optellen":
    print("Het resultaat is:", x + y)
elif z == "aftrekken":
    print("Het resultaat is:", x - y)
elif z == "vermenigvuldigen":
    print("Het resultaat is:", x * y)
elif z == "delen":
  if y != 0: 
    print("Het resultaat is:", x / y)
  else:
    print("Je kunt niet delen door 0")
else:
    print("Ongeldige info")
