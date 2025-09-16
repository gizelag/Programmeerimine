temp = int(input("Sisesta temperatuur kraadides: "))
if temp < 0:
    print("Jäätumine")
elif temp <= 10:
    print("Külm")
elif  temp <= 20:
    print("Mõnus kevadilm")
elif temp <= 30:
    print("Soe suvi")
else:
    print("Liiga kuum")




