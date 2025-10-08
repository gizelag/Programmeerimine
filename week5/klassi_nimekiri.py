from andmete_lugeja import loe_tekst_failist
import random
def lae_nimed_failist(failinimi = 'klassinimed.txt'):
    try:
        sisu = loe_tekst_failist(failinimi)
        if sisu is None:
            print("Viga, faili ei leitud")
            return []
        sisu = [rida.strip() for rida in sisu.splitlines()if rida.strip()]
        return sisu
    except Exception as e:
        return []

def kuva_menuu():
    print("1. Näita kõiki nimesid\n"
          "2. Lisa nimi\n"
          "3. Eemalda nimi\n"
          "4. Näita esimesed n nime\n"
          "5. Vali suvaline õpilane\n"
          "6. Sulge programm\n")

def kusi_kasutaja_valik():
    while True:
        try:
            kasutaja_valik = int(input("Sisesta arv 1-6"))
            if 1 <= kasutaja_valik <= 6:
                return kasutaja_valik
            else:
                print("Viga, arv peab olema 1-6")
        except ValueError:
            print("Viga, arv peab olema 1-6")

def kuva_koik_nimed(nimed):
    if not nimed:
        print("Viga, nimed puuduvad")
        return None
    for i, nimi in enumerate(nimed, start = 1):
        print(f'{i}. {nimi}')

def lisa_nimi(nimed):
    uus_nimi = input("Sisesta uus nimi:")
    if not uus_nimi.strip():
        print("Viga, nimi puudub")
        return None

    for nimi in nimed:
        if nimi.lower() == uus_nimi.lower():
            print(f"Viga, {uus_nimi} on juba olemas")
            return None

    nimed.append(uus_nimi)
    print(f"Nimi '{uus_nimi}' lisati nimekirja!")
    kuva_koik_nimed(nimed) #kuvab koik nimed uuendatud kujul

def eemalda_nimi(nimed):
    if not nimed:
        print('Viga: nimed puuduvad')
        return None

    for i, nimi in enumerate(nimed, start = 1):
        print(f'{i}. {nimi}')

    try:
        eemalda = int(input('Sisesta eemaldatava õpilase number: '))
    except ValueError:
        print('Viga: Sisend pole number')
        return None

    if not 1 <= eemalda <= len(nimed):
        print('Viga: Sisend peab olema listis olev number')
        return None
    eemaldatud = nimed.pop(eemalda - 1)
    print(f'Nimi: {eemaldatud} eemaldati nimekirjast!')

    kuva_koik_nimed(nimed)

def naita_esimesed_n(nimed):
    if not nimed:
        print('Viga: nimed puuduvad')
        return None

    try:
        mitu_nime = int(input("Mitu nime soovid näha: "))

    except ValueError:
        print('Viga: Sisend pole number')
        return None

    if mitu_nime <= 0:
        print('Arv peab olema suurem kui 0')
        return None

    if mitu_nime > len(nimed):
        mitu_nime = len(nimed)

    n = mitu_nime
    for i, nimi in enumerate(nimed[:n], start=1):
        print(f'{i}. {nimi}')


def vali_suvaline_opilane(nimed):
    if not nimed:
        print('Viga: nimed puuduvad')
        return None

    suvaline_opilane = random.choice(nimed)
    print(f'Suvaline valik: {suvaline_opilane}')


def main():
    nimed = lae_nimed_failist('klassinimed.txt')
    while True:
        kuva_menuu()
        valik = kusi_kasutaja_valik()

        if valik == 1:
            kuva_koik_nimed(nimed)
        elif valik == 2:
            lisa_nimi(nimed)
        elif valik == 3:
            eemalda_nimi(nimed)
        elif valik == 4:
            naita_esimesed_n(nimed)
        elif valik == 5:
            vali_suvaline_opilane(nimed)
        else:
            break

    print('Lõplik nimekiri oli:')
    kuva_koik_nimed(nimed)


if __name__ == "__main__":
    main()



