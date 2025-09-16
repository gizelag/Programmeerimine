kiirus = float(input("sisesta auto kiirus km/h:"))
if kiirus < 50: print("lubatud kiirus")
elif kiirus >= 80: print("kiirus! trahv summas: {trahvi_summa} EUR")
else: print("hoiatus: ole ettevaatlik")
uletatud_kiirus = - 80
trahvi_summa = (uletatud_kiirus - 80) * 5