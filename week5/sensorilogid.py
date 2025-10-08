from andmete_lugeja import loe_tekst_failist
def lae_temp_failist(failinimi):
    try:
        temp = loe_tekst_failist(failinimi)
        if temp is None or temp.strip() == "":
            print("Viga, failist ei saa andmeid lugeda")
            return[]
        temp = [rida.strip() for rida in temp.splitlines() if rida.strip()]
        return temp
    except Exception as e:
        print(f"Tekkis viga faili lugemisel: {e}")
        return[]

def puhasta_andmed(failinimi):
    temp = lae_temp_failist(failinimi)#kutsusin valja funktsiooni
    if not temp:#veakontroll tagastab tuhja listi kui viga
        return[]
    puhastatud = []
    for temperatuur in temp:
        try:
            temperatuur = float(temperatuur.strip())
            if temperatuur == "":
                continue
            if -999.0 < temperatuur < 9999.0:
                puhastatud.append(temperatuur)
        except ValueError as e:
            continue
    puhtad_mootmised = puhastatud
    return puhtad_mootmised

def sorteeri_mootmised(puhtad_mootmised):
    if not puhtad_mootmised:
        print("Viga: sorteeri_mootmised.")
        return []
    sorteeritud_mootmised = sorted(puhtad_mootmised)
    return sorteeritud_mootmised

def arvuta_statistika(sorteeritud_mootmised):
    if not sorteeritud_mootmised:
        print("Viga: arvuta_statistika.")
        return {}, 0

    kokku_temp = sum(sorteeritud_mootmised)
    mootmiste_koguarv = len(sorteeritud_mootmised)

    vaikseim_mootmine = sorteeritud_mootmised[0]
    suurim_mootmine =  sorteeritud_mootmised[-1]
    alla_keskmise = 0

    if mootmiste_koguarv > 0:
        keskmine = round(kokku_temp / mootmiste_koguarv, 1)

    sõnastik = {
        "min": vaikseim_mootmine,
        "max": suurim_mootmine,
        "kokku": mootmiste_koguarv,
        "keskmine": keskmine
    }
    for temp in sorteeritud_mootmised:
        if temp < keskmine:
            alla_keskmise += 1

    return sõnastik, alla_keskmise


def main():
    failinimi = "logid_sensor.txt"
    sõnastik = {}
    puhtad_mootmised = puhasta_andmed(failinimi)
    sorteeritud_mootmised = sorteeri_mootmised(puhtad_mootmised)
    sõnastik , alla_keskmise = arvuta_statistika(sorteeritud_mootmised)

    print(f"Puhastatud ja sorteeritud mõõtmised: {sorteeritud_mootmised}\n"
        f"Mõõtmisi kokku: {sõnastik.get('kokku', 'Pole arvutatud')}\n"
        f"Keskmine temperatuur: {sõnastik.get('keskmine', 'Pole arvutatud')} °C\n"
        f"Alla keskmise mõõtmised kokku: {alla_keskmise}")


if __name__ == "__main__":
    main()



