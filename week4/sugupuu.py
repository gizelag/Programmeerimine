def loe_pereandmed(failinimi):

    try:
        with open(failinimi,"r", encoding="utf-8") as fail:
            return fail.readlines()
    except FileNotFoundError:
        #print(f"Viga: '{failinimi}' ei leitud")
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
            if not nimi:#kontrollime et nimi ei ole tuhi peale tuhikute eemaldamist
                continue

            vanus = int(round(rea_osad[1].strip()))
            print(f"{nimi} on {vanus} aastat vana")


        except (ValueError, IndexError):
            continue


def arvuta_perestatistika(failisisu):
    if failisisu is None:
        return None
    inimeste_arv = 0
    vanim= None
    vanus_kokku = 0
    noorim = None

    try:
        for rida in failisisu:
            rida = rida.strip()
            if not rida:continue

            if not (";") in rida:
                continue

        try:
            rea_osad = rida.split(";")  # tukeldan rea osad sobiva eraldajaga

            if len(rea_osad) != 2:  # kontollin et tukeldamise tulemusena on tapselt kaks rida
                continue

            vanus = int(rea_osad[1].strip())  # leiame vanuse

            if not vanus:  # kontrollime et vanus ei ole tuhi peale tuhikute eemaldamist
                continue
            inimeste_arv += 1
            vanus_kokku += vanus
            if vanim is None or vanus > vanim:
                vanim = vanus
            if noorim is None or vanus < noorim:
                noorim = vanus

        except (ValueError, IndexError):
            continue

        keskmine = vanus_kokku / inimeste_arv
        keskmine = round(keskmine)
        return keskmine, noorim, vanim
    except Exception:
        return None

def main():
    sisu = loe_pereandmed(failinimi="vanused.txt")
    kuva_viis_esimest(failisisu=sisu)
    tulemus = arvuta_perestatistika(failisisu=sisu)
    if tulemus is not None:
        keskmine_vanus, noorim_vanus, vanim_vanus = tulemus
        print(f"Keskmine vanus:{int(keskmine_vanus)}")
    if noorim_vanus is not None:
        print(f"Noorim vanus:{noorim_vanus}")
    if vanim_vanus is not None:
        print(f"Vanim vanus:{vanim_vanus}")
    else:
        print("Ei suutnud leida ühtegi kehtivat vanust failist")

if __name__ == "__main__":
    main()











