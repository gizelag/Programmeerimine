import time
import random

def küsi_kasutaja_käik(tikud_alles):
    print("Mängija 1 kord(sul on 5 sekundit)")
    start = time.time()
    kasutaja_input = int(input("Mitu tikku võtad(1-5)? "))
    end = time.time()

    aeg = end - start
    if aeg > 5:
        print("Aeg läbi! Võetakse auttomaatselt 1 tikk.")
        return 1
    if not kasutaja_input.isdigit():
        print("Vigane sisend! võetakse automaatselt 1 tikk.")
        return 1

    mitu = int(kasutaja_input)
    if mitu < 1 or mitu > 5:
        print("Vale arv! Võetakse automaatselt 1 tikk. ")
        return 1

    if mitu > tikud_alles:
        print("Pole nii palju tikke järel!Võetakse automaatselt 1 tikk.")
        return 1

    return mitu

def arvuti_käik(tikud_alles):
    max_voetav = min(5, tikud_alles)#suurim lubatud vaartus
    käik = random.randint(1, max_voetav)
    print("Mängija 2 (arvuti) kord:")
    print(f"Arvuti: {käik}")
    return käik

def main():
    print("Tikumäng algab! Viimase tiku võtja kaotab.")
    tikud = 20
    mängija = 1#1 on inimene ja 2 on arvuti


    while tikud > 0:
        print(f"Tikke järel: {tikud} \n")
        if mängija == 1:
            käik = küsi_kasutaja_käik(tikud)
            print(f"Kasutaja käik: {käik}")
        else:
            käik = arvuti_käik(tikud)

        tikud -= käik
        if tikud < 0:
            tikud = 0

        print(f"Alles: {tikud} tikku")
        if tikud == 0:
            mängija = 1
            print("\nMängija 1 (sina) võttis viimase tiku ja kaotas")
            print("Arvuti võitis!")
        else:
            print("\nArvuti võttis viimase tiku ja kaotas")
            print("Palju õnne, sa võitsid!")
        break
    print(f"Tikke järel: {tikud} \n")
    if mängija == 1:
        mängija = 2
    else:
        mängija = 1

if __name__ == "__main__":
    main()