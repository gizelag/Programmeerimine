kiirus = float(input("sisesta auto kiirus km/h: "))
trahvi_summa = (kiirus - 80) * 5

if kiirus < 50:
    print("Lubatud kiirus")
elif kiirus > 80:
    print(f"kiirus! trahv summas: {trahvi_summa} EUR")
else:
    print("hoiatus: ole ettevaatlik")