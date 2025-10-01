def loe_tulemused(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Viga: Faili `{failinimi}` ei leitud")
        return None


def leia_voitja(failisisu):
    # Kontrollin, ega funktsiooni sisend pole None
    if failisisu == None:
        return None, 0
    voitja_nimi = ""
    voitja_punktid = 0

    try:
        for rida in failisisu:
            rida.strip()


            # Kui tuhi rida siis jatame rea vahele
            if not rida:
                continue

            # Kas eraldaja mark on, kui ei ole siis jatame vahele
            if ";" not in rida:
                continue

            try:
                rea_osad = rida.split(";")
                # print(rea_osad)

                # Kontrollin, et tükeldamise tulemusena on täpselt 2 osa sest voib tekkida ValueError
                if len(rea_osad) != 2:
                    continue

                # Leiame nime
                nimi = rea_osad[0].strip()

                # Kontrolli, et nimi ei ole tühi, kui on jäta vahele
                if not nimi:
                    # print(nimi)
                    continue

                # Teisendame punktid integeriks, praegu on see str -> siin voib tekkida ValueError
                punktid = int(rea_osad[1].strip())

                # Leia kõrgeima punktisummaga osaleja nimi ja tema punktid
                if punktid > voitja_punktid:
                    voitja_punktid = punktid
                    voitja_nimi = nimi

            # Jäta vigased read vahele ja jätka järgmise real
            except (ValueError, IndexError):
                continue

        return voitja_nimi, voitja_punktid

    except Exception:
        print("Error tekkis funktsioonis leia_voitja(failisisu)")
        return None, 0


def main():
    sisu = loe_tulemused(failinimi="tulemused.txt")

    nimi_voitjal, punktid_voitjal = leia_voitja(failisisu=sisu)

    print(f"VÕITJA: {nimi_voitjal} ({punktid_voitjal} punkti)")



if __name__ == "__main__":
    main()
