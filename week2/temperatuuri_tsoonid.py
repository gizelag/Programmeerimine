temp = int(input("Sisesta temperatuur kraadides: "))
if temp < 0:
    print("Jaatumine")
elif temp <= 10:
    print("Kulm")
elif  temp <= 20:
    print("Monus kevadilm")
elif temp <= 30:
    print("Soe suvi")
else:
    print("Liiga kuum")