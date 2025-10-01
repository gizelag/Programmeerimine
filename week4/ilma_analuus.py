def loe_ilmaandmed(failinimi):
    try:
        with open(failinimi, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None


def tootle_ilmaandmed(ilmastik_list):
    if ilmastik_list is None:
        return None, None, None, None
    try:
        keskmine_max = 0
        keskmine_min = 0
        sademete_summa = 0
        vihamseid_paevi = 0
        statistika_kogus = 0
        for rida in ilmastik_list:
            if not rida:
                continue
            if not ";" in rida:
                continue
            try:
                rea_osad = rida.split(";")
                if len(rea_osad) != 4:
                    continue
                max_temp = float(rea_osad[1].strip())
                # if not max_temp:
                #     continue
                min_temp = float(rea_osad[2].strip())
                # if not min_temp:
                #     continue
                sademed = float(rea_osad[3].strip())
                # if not sademed:
                #     continue
                keskmine_max += max_temp
                keskmine_min += min_temp
                sademete_summa += sademed
                if sademed > 1.0:
                    vihamseid_paevi += 1
                statistika_kogus += 1
            except (ValueError, IndexError):
                continue
        if statistika_kogus == 0:
            return None, None, None, None
        keskmine_max = round(keskmine_max / statistika_kogus, 1)
        keskmine_min = round(keskmine_min / statistika_kogus, 1)
        sademete_summa = round(sademete_summa, 1)

    except Exception as e:
        print(e)

    return keskmine_max, keskmine_min, sademete_summa, vihamseid_paevi


def kuva_statistika(keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi):
    if any(x is None for x in (keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi)):
        print("Viga: statistika puudub")
        return None, None, None, None
    print(f"Keskmine max temperatuur: {keskmine_max}°C")
    print(f"Keskmine min temperatuur: {keskmine_min}°C")
    print(f"Sademete kogusumma: {sademete_summa} mm")
    print(f"Vihmaseid päevi (>1mm): {vihmaseid_paevi}")


def salvesta_statistika(keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi):
    if any(x is None for x in (keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi)):
        return None, None, None, None
    try:
        with open("ilm_statistika.txt", "w", encoding="utf-8") as file:
            tekst = (f"Keskmine max temperatuur: {keskmine_max}°C\n"
                     f"Keskmine min temperatuur: {keskmine_min}°C\n"
                     f"Sademete kogusumma: {sademete_summa} mm\n"
                     f"Vihmaseid päevi (>1mm): {vihmaseid_paevi}"
                     )

            file.write(tekst)
            fail_kuhu_kirjutan = "ilm_statistika.txt"
            print(f"Statistika salvestatud faili '{fail_kuhu_kirjutan}'")
    except Exception as e:
        print(f"Viga faili kirjutamisel: {e}")


def main():
    ilmastik_list = loe_ilmaandmed(failinimi="ilmastiku_andmed.txt")
    keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi = tootle_ilmaandmed(ilmastik_list)
    kuva_statistika(keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi)
    salvesta_statistika(keskmine_max, keskmine_min, sademete_summa, vihmaseid_paevi)


if __name__ == '__main__':
    main()
