x = int(input("sisesta esimene taisarv:"))#kusib esimest taisarvu
y = int(input("sisesta teine taisarv"))#kusib teist taisarvu
summa = x + y#kahe arvu summa arvutamine
if summa > 100: summa -= 50 print("loppsumma:", summa )#kui summa suurem kui 100 siis lahutab 50
elif summa < 50: summa *= 2 print("loppsumma", summa)#kui summa alla 50-ne siis korrutab kahega
else: print("loppsumma:", summa)#kui summa on vahemikus 50-100 valjastab lihtsalt sisestatud arvu
