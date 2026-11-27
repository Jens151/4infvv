gewicht = float(input("Hoeveel weeg je (in kg)?: "))
lengte = float(input("Hoe groot ben je (in m)?: "))
bmi = round(gewicht / (lengte * lengte), 1)
print("Je BMI is", bmi, ".")

if bmi < 18.5:
    print("Categorie: ondergewicht")
elif bmi < 25:
    print("Categorie: gezond gewicht")
elif bmi < 30:
    print("Categorie: overgewicht")
else:
    print("Categorie: zwaar overgewicht")
