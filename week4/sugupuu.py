def loe_pereandmeid(vanused):

    try:
        with open(vanused,"r", encoding="utf-8") as f:
            for rida in f:
                print(rida)
    except FileNotFoundError:
        print(f"Viga: '{vanused}' ei leitud")
        return None


def kuva_viis_esimest(failisisu):
    if failisisu is None:
        return None
    try:
        for rida in failisisu:
            if not rida:
                continue

            if ";" not in rida:
                continue

        try:
            rea_osad = rida.split(";")#tukeldan rea osad sobiva eraldajaga
            if len(rea_osad) != 2:#kontollin et tukeldamise tulemusena on tapselt kaks rida
                continue

            nimi = rea_osad[0].strip()#leiame nime

            if not nimi:#kontrollime et nimi ei ole tuhi peale tuhikute eemaldamist
                continue

            vanus = int(round(rea_osad[1].strip()))#teisendame vanuse taisarvuks



        except (ValueError, IndexError):
            continue

    for i in vanused.readlines()[:5]:
        nimi, vanus = rida.strip().split(";")
        print(f"{nimi} on {vanus} aastat vana")



def arvuta_perestatistika(failisisu):

    if not failisisu:
        return None, None, None

    vanused = []

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

            vanused = rea_osad[1].strip()  # leiame vanuse

            if not nimi:  # kontrollime et nimi ei ole tuhi peale tuhikute eemaldamist
                continue

        except (ValueError, IndexError):
            continue

    keskmine_vanus = int(round(sum(vanused) / len(vanused)))
    noorim_vanus = min(vanused)
    vanim_vanus = max(vanused)

    return keskmine_vanus, noorim_vanus, vanim_vanus

def main():
    failinimi = "vanused.txt"
    failisisu = loe_pereandmeid(failinimi)
    kuva_viis_esimest(failisisu)
    arvuta_perestatistika(failisisu)
    if keskmine_vanus is not None:
        print(f"Keskmine vanus:{keskmine_vanus}")
    if noorim_vanus is not None:
        print(f"Noorim vanus:{noorim_vanus}")
    if vanim_vanus is not None:
        print(f"Vanim vanus:{vanim_vanus}")
    else:
        print("Ei suutnud leida ühtegi kehtivat vanust failist")

if __name__ == "__main__":
    main()











