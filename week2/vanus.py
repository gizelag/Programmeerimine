vanus = int(input("Sisesta oma vanus: "))#küsib kasutajalt vanust, muudab sisendi täisarvuks
if vanus <= 0:
    print("Vigane vanus")#kui vanus on negatiivne on vigane vanus
elif vanus < 18:
    print("Oled veel liiga noor")#kui vanus on väiksem kui 18, siis oled veel liiga noor
elif vanus >= 18 and vanus <= 65:
    print("Oled tööeas")#kui vanus on 18 kuni 65 kaasa arvatud, siis oled tööeas
else:
    print("Oled pensionieas")#kõikidel muudel juhtudel oled pensionieas
