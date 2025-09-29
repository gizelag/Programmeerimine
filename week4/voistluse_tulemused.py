def loe_tulemused(failinimi):
    try:
        with open(failinimi,"r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Viga: Faili '{failinimi}' ei leitud ")
        return None

def leia_voitja(failisisu):
    if failisisu is None:
        return None, 0
    try:
        for rida in failisisu(1):
        rida.strip()
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

            punktid = int rea_osad[1].strip()

            if punktid > voitja_punktid:
                voitja_punktid = punktid
                voitja_nimi = nimi


            if not punktid:
        except (ValueError, IndexError):
            continue

        return voitja_nimi, voitja_punktid
    except Exception:
        print(f"VÕITJA: {voitja_nimi}, {voitja_punktid}")

if __name__ == "__main__":