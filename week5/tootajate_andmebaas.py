from andmete_lugeja import loe_tekst_failist

def lae_vanused_failist(failinimi):
    sisu = loe_tekst_failist(failinimi)
    sõnastik = {}
    if sisu is None:
        print("Viga, faili sisu puudub")
        return {}
    try:
        read = sisu.strip().splitlines()
        for rida in read:
            if rida == "":
                continue
            rida = rida.split(":")
            try:
                nimi = rida[0].strip()
                if not nimi.isalpha():
                    print(f"Viga nimes {nimi}")
                    continue
                vanus = int(rida[1].strip())
                if not vanus:
                    print(f"Viga vanuses {vanus}")
                    continue
            except ValueError as e:
                print(f"ValueError {e}")
                continue
            except IndexError as e:
                print(f"IndexError1 {e}")
                continue
            sõnastik.update({nimi: vanus})
    except IndexError as e:
        print(f"IndexError {e}")
    return sõnastik


def jaga_inimesed_gruppidesse(nimede_vanuste_dict):
    lapsed = []
    taiskasvanud = []
    pensionarid = []
    if nimede_vanuste_dict == None or nimede_vanuste_dict == {}:
        print("Nimede vanuste dict")
        return [lapsed, taiskasvanud, pensionarid]

    for nimi, vanus in nimede_vanuste_dict.items():
        if vanus < 13:
            lapsed.append(nimi)
        elif vanus <= 64:
            taiskasvanud.append(nimi)
        else:
            pensionarid.append(nimi)
    grupid = [lapsed, taiskasvanud, pensionarid]
    return grupid


def main():
    nimede_vanuste_dict = lae_vanused_failist(failinimi="vanused.txt")
    grupid = jaga_inimesed_gruppidesse(nimede_vanuste_dict)
    lapsed_list = grupid[0]
    taiskasvanud_list = grupid[1]
    pensionarid_list = grupid[2]
    lapsed = ", ".join(lapsed_list)
    taiskasvanud = ", ".join(taiskasvanud_list)
    pensionarid = ", ".join(pensionarid_list)

    print(f"Lapsed (alla 13): {lapsed}\n"

          f"Täiskasvanud (13-64): {taiskasvanud}\n"
          f"Pensionärid (üle 64): {pensionarid}\n")


if __name__ == "__main__":
    main()