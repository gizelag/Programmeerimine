from andmete_lugeja import loe_tekst_failist
import random


# Funktsioon, mis loeb nimed tekstifailist
# Tagastab nimede listi või tühja listi, kui tekib viga
def lae_nimed_failist(failinimi='klassinimed.txt'):
    try:
        # Kasutame eraldi moodulit faili lugemiseks
        sisu = loe_tekst_failist(failinimi)

        # Kui fail puudub või lugemine ebaõnnestus
        if sisu is None:
            print("Viga, faili ei leitud")
            return []

        # Teeme igast reast nime ja eemaldame tühjad read
        sisu = [rida.strip() for rida in sisu.splitlines() if rida.strip()]
        return sisu

    except Exception as e:
        # Üldine veapüüdmine – programm ei kuku kokku
        return []


# Kuvab kasutajale tekstimenüü
def kuva_menuu():
    print(
        "1. Näita kõiki nimesid\n"
        "2. Lisa nimi\n"
        "3. Eemalda nimi\n"
        "4. Näita esimesed n nime\n"
        "5. Vali suvaline õpilane\n"
        "6. Sulge programm\n"
    )


# Küsub kasutajalt menüü valikut
# Kasutab tsüklit ja erindite käsitlemist
def kusi_kasutaja_valik():
    while True:
        try:
            kasutaja_valik = int(input("Sisesta arv 1-6: "))

            # Kontrollime, kas valik on lubatud vahemikus
            if 1 <= kasutaja_valik <= 6:
                return kasutaja_valik
            else:
                print("Viga, arv peab olema 1-6")

        except ValueError:
            # Kui sisend ei ole arv
            print("Viga, arv peab olema 1-6")


# Kuvab kõik nimed koos järjekorranumbritega
def kuva_koik_nimed(nimed):
    if not nimed:
        print("Viga, nimed puuduvad")
        return None

    for i, nimi in enumerate(nimed, start=1):
        print(f"{i}. {nimi}")


# Lisab nime nimekirja
# Kontrollib, et nimi ei oleks tühi ega juba olemas
def lisa_nimi(nimed):
    uus_nimi = input("Sisesta uus nimi: ")

    # Tühja sisendi kontroll
    if not uus_nimi.strip():
        print("Viga, nimi puudub")
        return None

    # Duplikaadi kontroll (tõstutundetu)
    for nimi in nimed:
        if nimi.lower() == uus_nimi.lower():
            print(f"Viga, {uus_nimi} on juba olemas")
            return None

    nimed.append(uus_nimi)
    print(f"Nimi '{uus_nimi}' lisati nimekirja!")
    kuva_koik_nimed(nimed)


# Eemaldab nime kasutaja valitud järjekorranumbri alusel
def eemalda_nimi(nimed):
    if not nimed:
        print("Viga: nimed puuduvad")
        return None

    # Kuvame nimed koos numbritega
    for i, nimi in enumerate(nimed, start=1):
        print(f"{i}. {nimi}")

    try:
        eemalda = int(input("Sisesta eemaldatava õpilase number: "))
    except ValueError:
        print("Viga: sisend pole number")
        return None

    # Kontrollime, kas number on listi piires
    if not 1 <= eemalda <= len(nimed):
        print("Viga: sisend peab olema listis olev number")
        return None

    eemaldatud = nimed.pop(eemalda - 1)
    print(f"Nimi '{eemaldatud}' eemaldati nimekirjast!")

    kuva_koik_nimed(nimed)


# Kuvab esimesed n nime nimekirjast
def naita_esimesed_n(nimed):
    if not nimed:
        print("Viga: nimed puuduvad")
        return None

    try:
        mitu_nime = int(input("Mitu nime soovid näha: "))
    except ValueError:
        print("Viga: sisend pole number")
        return None

    if mitu_nime <= 0:
        print("Arv peab olema suurem kui 0")
        return None

    # Kui küsitakse rohkem kui olemas, näitame kõik
    if mitu_nime > len(nimed):
        mitu_nime = len(nimed)

    for i, nimi in enumerate(nimed[:mitu_nime], start=1):
        print(f"{i}. {nimi}")


# Valib nimekirjast ühe suvalise õpilase
def vali_suvaline_opilane(nimed):
    if not nimed:
        print("Viga: nimed puuduvad")
        return None

    suvaline_opilane = random.choice(nimed)
    print(f"Suvaline valik: {suvaline_opilane}")


# Programmi käivituspunkt
def main():
    # Laeme nimed failist programmi alguses
    nimed = lae_nimed_failist('klassinimed.txt')

    # Põhitsükkel – töötab kuni kasutaja valib väljumise
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

    # Programmi lõpus kuvame lõpliku nimekirja
    print("Lõplik nimekiri oli:")
    kuva_koik_nimed(nimed)


# Tagab, et main() käivitub ainult otse faili käivitamisel
if __name__ == "__main__":
    main()
