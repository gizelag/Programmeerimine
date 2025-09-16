a = int(input("sisesta esimene arv:"))
tehe = str(input("sisesta tehe (+, -, *, /):"))
b  int(input("sisesta teine arv:"))
if tehe == "+":
    print("tulemus:", a + b)
elif tehe == "-":
    print("tulemus:", a - b)
elif tehe == "*":
    print("tulemus:", a * b)
    if b == 0:
        print("viga! nulliga jagamine pole lubatud")
elif tehe == "/":
    print("tulemus:", a / b)
else:
    print("tundmatu tehe! palun kasuta ainult +, -, *, voi /.")


