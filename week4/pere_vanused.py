from operator import truediv

failinimi = "pere_vanused.txt"

def loe_pereandmed():
    try:
        with open(failinimi,"r",encoding="utf-8") as fail:
            return fail.readlines()

    except FileNotFoundError:
        return None

def arvuta_perestatistika():
    if failisisu is None:
        return None, None, None
    inimeste_arv = 0
    vanus_kokku = 0
    noorim = None
    vanim = None

    try:
        for rida in failisisu:
            if not rida:
                continue
            if ";" not in rida:
                continue
            try:
                rea_osad = rida.split(";")
                if len(rea_osad) != 2:
                    continue

                nimi = rea_osad[0].strip()
                if not nimi:
                    continue

                vanus = int(rea_osad[1].strip())
                if vanus < 0:
                    continue
                inimeste_arv += 1
                vanus_kokku += vanus
                if vanim is None or vanus > vanim:
                    vanim = vanus
                if noorim is None or vanus < noorim:
                    noorim = vanus
            except (ValueError, IndexError):
                continue

        if inimeste_arv == 0:
            return None, None, None

        keskmine = vanus_kokku / inimeste_arv
        keskmine = round(keskmine)
        return keskmine, noorim, vanim
    except Exception:
        return None, None, None

def lisa_pereliikmeid():
    while True:
        lisa_pere = input("Soovid lisada uusi pereliikmeid? (jah/ei): ")
        if lisa_pere == "jah":
            while True:
                pere_nimi = str(input("Sisesta nimi: "))
                if pere_nimi == "":
                    print("Nimi ei tohi olla tühi")
                else:
                    break

            while True:
                try:
                    pere_vanus = int(input("Sisesta vanus: "))
                    if pere_vanus < 0:
                        print("Vanus peab olema positiivne arv")
                        continue
                    else:
                        break
                except ValueError:
                    continue

            salvesta_uus_liige(pere_nimi, pere_vanus)

        elif lisa_pere == "ei":
            print("Uued liikmed lisatud!")
            break
        else:
            print("Palun vasta 'jah' või 'ei'")

def salvesta_uus_liige(nimi, vanus):
    try:
        with open(failinimi,"a",encoding="utf-8") as fail:
            fail.write(f"{nimi};{vanus}\n")

    except FileNotFoundError:
        return None

def kuva_vordlus(vana_keskmine, vana_noorim, vana_vanim, uus_keskmine, uus_noorim, uus_vanim):
    muutus_keskmine = uus_keskmine - vana_keskmine
    muutus_noorim = uus_noorim - vana_noorim
    muutus_vanim = uus_vanim - vana_vanim

    print(f"Keskmine vanus: {vana} -> {uus} (muutus: {erinevus})")
    print(f"Noorim vanus: {vana_noorim} -> {uus_noorim} (muutus: {erinevus})")
    print(f"Vanim vanus: {vana_vanim} -> {uus_vanim} (muutus: {erinevus-vana_vanim})")

def main():
    sisu = loe_pereandmed()
    vana_keskmine, vana_noorim, vana_vanim = arvuta_perestatistika(sisu)

    if None not in (vana_keskmine, vana_noorim, vana_vanim):
        print(f"Keskmine vanus: {vana_keskmine}")
        print(f"Noorim vanus: {vana_noorim}")
        print(f"Vanim vanus: {vana_vanim}")
    else:
        print("Ei suutnud leida ühtegi kehtivat vanust failist")

    lisa_pereliikmeid()

    uus_sisu = loe_pereandmed()
    uus_keskmine, uus_noorim, uus_vanim = arvuta_perestatistika()

    if None not in (vana_keskmine, vana_noorim, vana_vanim, uus_keskmine, uus_noorim, uus_vanim):
        kuva_vordlus(vana_keskmine, vana_noorim, vana_vanim, uus_keskmine, uus_noorim, uus_vanim)

if __name__ == "__main__":
    main()