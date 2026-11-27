resultaat = int(input("Geef je toetsresultaat op 100: "))
if resultaat < 0 or resultaat > 100:
    print("Ongeldig Cijfer")
elif resultaat >= 50:
    print("Je bent geslaagd")
else:
    print("Je bent niet door")
