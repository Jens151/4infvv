uur_loon = 8.5
werkuren = float(input("Hoeveel uur heb je gewerkt deze maand: "))
maandloon = uur_loon * werkuren
if werkuren > 20:
  print("Proficiat, je krijgt een premie van 25 euro!")
  maandloon = maandloon + 25
print("Je verdient deze maand", maandloon, "euro.")
