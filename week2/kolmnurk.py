y = int(input("sisesta esimese kulje pikkus:"))#kusib kasutajalt esimest arvu
z = int(input("sisesta teise kulje pikkus:"))#kusib kasutajalt teist arvu
c = int(input("sisesta kolmanda kulje pikkus:"))#kusib kasutajalt kolmandat arvu
kolmnurga_umbermoot = c + y + z
if y + z > c and c + z > y and c + y > z:
    print(f"sellest saab moodustada kolmnurga, kolmnurga umbermoot on: {kolmnurga_umbermoot} ")
#kui kaks kulje pikkust on suuremad kui kolmas siis kehtib ja arvutab kolmnurga umbermoodu
else:
    print("sellest ei saa moodustada kolmnurka")#kui ulaltoodu ei kehti valjastab selle sonumi
