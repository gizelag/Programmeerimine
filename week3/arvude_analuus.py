# Funktsioon võrdleb kahte arvu ja tagastab neist suurema
def leia_suurim(uus, senine_max):  # võrdleb kahte arvu ja tagastab suurema
    if uus > senine_max:
        return uus
    else:
        return senine_max


# Funktsioon kontrollib, kas antud arv on suurem kui 50
def kas_suurem_kui_50(arv):
    if arv > 50:
        return True
    else:
        return False


def main():
    # Kasutajale kuvatav juhis
    print("Sisesta arvud ükshaaval (1-100) lõpetamiseks kirjuta 'lõpp'")

    # Muutujad arvutuste ja statistika jaoks
    summa = 0
    suurim = 0
    yle_viiekymne = 0
    arv_kokku = 0

    # Tsükkel, mis kestab kuni kasutaja sisestab "lõpp"
    while True:
        kasutaja_sisend = input("Sisesta arv(või kirjuta 'lõpp'): ").lower()

        # Kontrollime, kas kasutaja soovib programmi lõpetada
        if kasutaja_sisend == "lõpp":
            break

        # Kontrollime, kas sisend on number
        if not kasutaja_sisend.isdigit():
            print("Viga: sisestus peab olema täisarv vahemikus 1 kuni 100.")
            continue

        arv = int(kasutaja_sisend)

        # Kontrollime, kas arv jääb lubatud vahemikku
        if arv < 1 or arv > 100:
            print("Viga: arv peab olema vahemikus 1 kuni 100.")
            continue

        # Uuendame summat ja loendurit
        summa += arv
        arv_kokku += 1

        # Leiame seni suurima arvu
        suurim = leia_suurim(arv, suurim)

        # Kontrollime, kas arv on suurem kui 50
        if kas_suurem_kui_50(arv):
            yle_viiekymne += 1

        # Kuvame vahetulemused pärast iga korrektset sisestust
        print("\n ---TULEMUSED---")
        if arv_kokku == 0:
            print("Ühtegi arvu ei sisestatud.")
        else:
            keskmine = summa / arv_kokku
            print(f"Sisestati {arv_kokku} arvu.")
            print(f"Arvude summa: {summa}")
            print(f"Suure suurim: {suurim}")
            print(f"Keskmine: {keskmine}")
            print(f"Arvud, mis olid suuremad kui 50: {yle_viiekymne}")


# Programmi käivitamise kontroll
if __name__ == "__main__":
    main()
