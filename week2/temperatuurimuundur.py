temperatuur = float(input("Sisesta temperatuur: "))
mootuhik = input("Kas temperratuur on C (Celcius) või  F (Fahrenheit)?")
if mootuhik == "C":
    teisendatud = temperatuur * 9/5 + 32
    print(f"{temperatuur}F on {round(teisendatud, 1)} F. ")
    elif mootuhik == "F":
        teisendatud = (temperatuur - 32) * 5/9
    print(f"{temperatuur}F on {round(teisendatud, 1)} C. ")
else:
    print("Tundmatu mõõtühik!")
