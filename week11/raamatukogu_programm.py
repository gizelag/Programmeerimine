from raamatukogu import Raamatukogu
from raamat import Raamat


def loe_raamatud_failist(failinimi):
    # Loeb raamatute andmed tekstifailist ja loob nende põhjal Raamat-objektid
    try:
        with open(failinimi, "r", encoding="utf-8") as f:
            fail = f.readlines()  # loeme kogu faili ridadena listi

        for rida in fail:
            rida = rida.strip()  # eemaldame reavahetused ja tühikud
            if not rida:
                continue  # jätame tühjad read vahele

            osad = [x.strip() for x in rida.split(",")]

            # Kontrollime, et reas oleks täpselt 4 välja
            if len(osad) != 4:
                print(f"Vahele jäetud vigane rida: {osad}")
                continue

            pealkiri = osad[0]
            autor = osad[1]
            lehekuljed = osad[2]
            liik = osad[3]

            # Loome Raamat-objekti ja lisame selle globaalsesse listi
            raamat = Raamat(pealkiri, autor, lehekuljed, liik)
            raamatud.append(raamat)

        return raamatud

    # Veatöötlus failiprobleemide jaoks
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []


def kasitle_juba_laenutatud(raamatukogu, pealkiri):
    # Käivitatakse siis, kui kasutaja proovib juba laenutatud raamatut võtta
    if raamatukogu.on_juba_laenutatud(pealkiri):
        print(f"\nSa oled raamatu {pealkiri} juba endale laenutanud\n")

    # Kuvame kasutaja laenutatud raamatud
    raamatukogu.kuva_laenutatud_raamatud()

    # Küsime, kas kasutaja soovib jätkata
    return kysi_kas_jatkata(raamatukogu)


def kysi_kas_jatkata(raamatukogu):
    # Tsükkel kestab seni, kuni kasutaja sisestab korrektse vastuse
    while True:
        vastus = input("Kas soovid veel raamatuid laenutada? (jah/ei/minu):")

        if vastus.lower() == "jah":
            return True
        elif vastus.lower() == "ei":
            return False
        elif vastus.lower() == "minu":
            # Kuvame kasutaja laenutatud raamatud
            raamatukogu.kuva_laenutatud_raamatud()
        else:
            print("Palun vasta kas jah/ei/minu")


def lopeta_programm(raamatukogu):
    # Programm lõpetatakse viisakalt ja kuvatakse kokkuvõte
    print("Aitäh, raamatukogu külastamast!")
    raamatukogu.kuva_laenutatud_raamatud()
    exit()


def kasitle_edukat_laenutust(raamatukogu, laenutatud_raamat):
    # Käivitatakse siis, kui raamat laenutati edukalt
    print(f"\nRaamat {laenutatud_raamat.pealkiri} edukalt laenutatud!\n")

    # Kuvame allesjäänud saadaval olevad raamatud
    raamatukogu.kuva_raamatud()

    return kysi_kas_jatkata(raamatukogu)


def initsialiseeri_raamatukogu(failinimi):
    # Loome Raamatukogu objekti ja täidame selle failist loetud raamatutega
    raamatukogu = Raamatukogu()
    raamatud = loe_raamatud_failist(failinimi)

    if not raamatud:
        print("Vigane faili lugemine")
        return None

    for raamat in raamatud:
        raamatukogu.lisa_raamat(raamat)

    if len(raamatukogu.raamatud) == 0:
        return None

    return raamatukogu


def main():
    failinimi = "raamatud.txt"

    # Initsialiseerime raamatukogu
    raamatukogu = initsialiseeri_raamatukogu(failinimi)
    if not raamatukogu:
        print("Raamatukogu laadimine ebaõnnestus või on tühi. Programm lõppeb.")
        exit()

    # Kuvame algse raamatute nimekirja
    raamatukogu.kuva_raamatud()

    # Peatsüklis küsime kasutajalt laenutamise soove
    while True:
        laenutamise_soov = input("Sisesta raamatu pealkiri, mida sa laenutada soovid:")
        vastus_raamatukogust = raamatukogu.laenuta_raamat(laenutamise_soov)

        if vastus_raamatukogust == "juba_laenutatud":
            if not kasitle_juba_laenutatud(raamatukogu, laenutamise_soov):
                lopeta_programm(raamatukogu)

        elif vastus_raamatukogust is not None:
            if not kasitle_edukat_laenutust(raamatukogu, vastus_raamatukogust):
                lopeta_programm(raamatukogu)

        else:
            print("Ei leidnud sellist raamatut, proovi uuesti!")
            if not kysi_kas_jatkata(raamatukogu):
                lopeta_programm(raamatukogu)


if __name__ == '__main__':
    # Globaalne list, kuhu loeme failist raamatud
    raamatud = []
    main()
