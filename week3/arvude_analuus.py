def leia_suurim(uus, senine_max):#vordleb kahte arvu ja tagastab suurema
    if uus > senine_max:
        return uus
    else:
        return senine_max

def kas_suurem_kui_50(arv):
    return arv > 50

def main ():
    print("Sisesta arvud ükshaaval (1-100) lõpetamiseks kirjuta 'lõpp'")
    summa = 0
    suurim = 0
    yle_viiekymne = 0
    arv_kokku = 0

    while True:
        kasutaja_sisend = input("Sisesta arv(või kirjuta 'lõpp'): ").lower()
        if kasutaja_sisend == "lõpp":
            break
        if not kasutaja_sisend.isdigit():
            print("Viga: sisestus peab olema täisarv vahemikus 1 kuni 100.")
            continue
        arv = int(kasutaja_sisend)
        if arv <1 or arv > 100:
            print("Viga: arv peab olema vahemikus 1 kuni 100.")
            continue

        summa += arv
        suurim = leia_suurim(arv, suurim)
        arv_kokku += 1
        if kas_suurem_kui_50(arv):
            yle_viiekymne += 1

            print("\n ---TULEMUSED---")
        if arv_kokku == 0:
            print("Ühtegi arvu ei sisestatud.")
        else:
            keskmine = summa / arv_kokku
            print(f"Ssestati {arv_kokku} arvu.")
            print(f"Arvude summa: {summa}")
            print(f"Suure suurim: {suurim}")
            print(f"Keskmine: {keskmine}")
            print(f"Arvud, mis olid suuremad kui 50: {yle_viiekymne}")

if __name__ == "__main__":
    main()


