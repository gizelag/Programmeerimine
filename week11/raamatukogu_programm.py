from raamatukogu import Raamatukogu
from raamat import Raamat


def  loe_raamatud_failist(failinimi):
    try:
        with open(failinimi , "r", encoding="utf-8") as f:
            fail = f.readlines()  # read lines into a list

        for rida in fail:
            rida = rida.strip()
            if not rida:
                continue
            osad = [x.strip() for x in rida.split(",")]


            if len(osad) != 4:  # Kui ei ole õigete andmetega rida siis jätame vahele
                print(f"Vahele jäetud vigane rida: {osad}")
                continue

            pealkiri = osad[0]
            autor = osad[1]
            lehekuljed = osad[2]
            liik = osad[3]

            # Loome objektid
            raamat = Raamat(pealkiri, autor, lehekuljed, liik)

            raamatud.append(raamat)
        return raamatud


    #veakasitlus
    except FileNotFoundError as e:
        print(e)
        return []
    except Exception as e:
        print(e)
        return []

def kasitle_juba_laenutatud(raamatukogu, pealkiri):
    if raamatukogu.on_juba_laenutatud(pealkiri) == True:
        print(f"\nSa oled raamatu {pealkiri} juba endale laenutanud\n")
    raamatukogu.kuva_laenutatud_raamatud()
    return kysi_kas_jatkata(raamatukogu)


def kysi_kas_jatkata(raamatukogu):
    while True:
        vastus = input("Kas soovid veel raamatuid laenutada? (jah/ei/minu):")
        if vastus.lower() == "jah":
            return True
        elif vastus.lower() == "ei":
            return False
        elif vastus.lower() == "minu":
            raamatukogu.kuva_laenutatud_raamatud()
        else:
            print("Palun vasta kas jah/ei/minu")

def lopeta_programm(raamatukogu):
    print(f"Aitäh, raamatukogu külastamast!")
    raamatukogu.kuva_laenutatud_raamatud()
    exit()

def kasitle_edukat_laenutust(raamatukogu, laenutatud_raamat):
    print(f"\nRaamat {laenutatud_raamat.pealkiri} edukalt laenutatud!\n")
    raamatukogu.kuva_raamatud()
    return kysi_kas_jatkata(raamatukogu)

def initsialiseeri_raamatukogu(failinimi):
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
    raamatukogu = initsialiseeri_raamatukogu(failinimi)
    if not raamatukogu:
        print("Raamatukogu laadimine ebaõnnestus või on tühi. Programm lõppeb.")
        exit()

    raamatukogu.kuva_raamatud()
    #prindime raamatukogu

    while True:
        laenutamise_soov = input("Sisesta raamatu pealkiri, mida sa laenutada soovid:")
        vastus_raamatukogust = raamatukogu.laenuta_raamat(laenutamise_soov)
        if vastus_raamatukogust == "juba_laenutatud":
            if kasitle_juba_laenutatud(raamatukogu, laenutamise_soov) is False:
                lopeta_programm(raamatukogu)
                return False

        elif vastus_raamatukogust is not None:
            if kasitle_edukat_laenutust(raamatukogu, vastus_raamatukogust) is False:
                lopeta_programm(raamatukogu)
                return False

        elif vastus_raamatukogust is None:
            print("Ei leidnud sellist raamatut, proovi uuesti!")
            if kysi_kas_jatkata(raamatukogu) is False:
                lopeta_programm(raamatukogu)
                return False

if __name__ == '__main__':
    raamatud = []
    main()