def loe_pereandmed(failinimi):
    try:
        with open(failinimi,"r", encoding="utf-8") as fail:
            return fail.readlines()
    except FileNotFoundError:#kui ei leita viga
        return None


def kuva_viis_esimest(failisisu):
    if failisisu is None:
        return None
    try:
        for rida in failisisu[:5]:
            if not rida:
                continue

            if not ";" in rida:
                continue

            try:
                rea_osad = rida.split(";")#tukeldan rea osad sobiva eraldajaga
                if len(rea_osad) != 2:#kontollin et tukeldamise tulemusena on tapselt kaks rida
                    continue

                nimi = rea_osad[0].strip()#leiame nime
                if not nimi:
                    continue#kontrollime et peale tuhikute eemaldamist nimi ei oleks tuhi

                vanus = int(rea_osad[1].strip())
                if not vanus:
                    continue
                print(f"{nimi} on {vanus} aastat vana")

            except (ValueError, IndexError):
                continue

    except Exception:
        return None


def arvuta_perestatistika(failisisu):
    if failisisu is None:
        return None,None,None
    inimeste_arv = 0
    vanus_kokku = 0
    noorim = None
    vanim = None

    try:
        for rida in failisisu:
            if not rida:
                continue

            if (";") not in rida:
                continue

            try:
                rea_osad = rida.split(";")  # tukeldan rea osad sobiva eraldajaga

                if len(rea_osad) != 2:  # kontollin et tukeldamise tulemusena on tapselt kaks rida
                    continue
                nimi = rea_osad[0].strip()
                if not nimi:
                    continue

                vanus = int(rea_osad[1].strip())  # leiame vanuse
                if vanus < 0:
                    continue
                inimeste_arv += 1
                vanus_kokku += vanus
                if vanim is None or vanus > vanim:
                    vanim = vanus
                if noorim is None or vanus < noorim:
                    noorim = vanus
            except (ValueError, IndexError):
                vanus = 0
        if inimeste_arv == 0:
            return None, None,None

        keskmine = vanus_kokku / inimeste_arv
        keskmine = round(keskmine)
        return keskmine, noorim, vanim

    except Exception:
        return None

def main():
    sisu = loe_pereandmed(failinimi='vanused.txt')
    kuva_viis_esimest(failisisu=sisu)
    statistika = arvuta_perestatistika(failisisu=sisu)
    if statistika is not None:
        keskmine_vanus, noorim_vanus, vanim_vanus = statistika
        print(f"Keskmine vanus:{keskmine_vanus}")
        print(f"Noorim vanus:{noorim_vanus}")
        print(f"Vanim vanus:{vanim_vanus}")
    else:
        print("Ei suutnud leida ühtegi kehtivat vanust failist")

if __name__ == "__main__":
    main()











