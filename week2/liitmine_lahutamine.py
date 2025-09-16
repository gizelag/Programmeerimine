x = int(input("sisesta esimene taisarv:"))#kusib esimest taisarvu

y = int(input("sisesta teine taisarv"))#kusib teist taisarvu
summa = x + y#kahe arvu summa arvutamine
if summa > 100:
    print("loppsumma:", summa - 50)#kui summa suurem kui 100 siis lahutab 50
elif summa < 50:
    print("loppsumma", summa * 2)#kui summa alla 50-ne siis korrutab kahega
else:
    print("loppsumma:", summa)#kui summa on vahemikus 50-100 valjastab lihtsalt sisestatud arvu
