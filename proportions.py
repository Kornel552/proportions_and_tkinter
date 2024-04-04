minuty = float(input("Podaj minuty: "))
sekundy = float(input("Podaj sekundy: "))
kilo = float(input("Podaj wydajność(kg): "))

a = ((minuty * 60) + sekundy)
b = kilo * 3600
c = b / a
print(round(c, 2), "kg")

l = str(input("chcesz porównać wydanjość?: "))
if l == str("tak"):
    wydajnosc = float(input("podaj przypisaną wydajność: "))
    q = float((c / wydajnosc) * 100)
    z = float((wydajnosc / c) * 100)
    if wydajnosc < c:
        print(round(q, 2), "%")
    else:
        print(round(q, 2), "%")

else:
    0
