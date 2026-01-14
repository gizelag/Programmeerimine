from andmete_lugeja import loe_tekst_failist


# Loeb tekstifailist nimed ja vanused ning salvestab need sõnastikku
# Eeldab formaati: Nimi:vanus
def lae_vanused_failist(failinimi):
    sisu = loe_tekst_failist(failinimi)
    sõnastik = {}

    # Kui faili sisu ei õnnestunud lugeda
    if sisu is None:
        print("Viga, faili sisu puudub")
        return {}

    try:
        # Jagame faili sisu ridadeks
        read = sisu.strip().splitlines()

        for rida in read:
            # Jätame tühjad read vahele
            if rida == "":
                continue

            # Jagame rea nimeks ja vanuseks
            rida = rida.split(":")

            try:
                nimi = rida[0].strip()

                # Kontrollime, et nimi koosneb ainult tähtedest
                if not nimi.isalpha():
                    print(f"Viga nimes {nimi}")
                    continue

                # Teisendame vanuse täisarvuks
                vanus = int(rida[1].strip())

                # Kontroll, et vanus oleks olemas ja kehtiv
                if not vanus:
                    print(f"Viga vanuses {vanus}")
                    continue

            except ValueError as e:
                # Tekib siis, kui vanust ei saa int-iks muuta
                print(f"ValueError {e}")
                continue

            except IndexError as e:
                # Tekib siis, kui real puudub nimi või vanus
                print(f"IndexError1 {e}")
                continue

            # Lisame nime ja vanuse sõnastikku
            sõnastik.update({nimi: vanus})

    except IndexError as e:
        # Kaitse ootamatu indeksivea vastu
        print(f"IndexError {e}")

    return sõnastik


# Jagab inimesed vanuse järgi gruppidesse
# Tagastab kolm listi: lapsed, täiskasvanud ja pensionärid
def jaga_inimesed_gruppidesse(nimede_vanuste_dict):
    lapsed = []
    taiskasvanud = []
    pensionarid = []

    # Kontrollime, et sisend ei oleks tühi
    if nimede_vanuste_dict == None or nimede_vanuste_dict == {}:
        print("Nimede vanuste dict")
        return [lapsed, taiskasvanud, pensionarid]

    # Läbime kõik nime ja vanuse paarid
    for nimi, vanus in nimede_vanuste_dict.items():
        if vanus < 13:
            lapsed.append(nimi)
        elif vanus <= 64:
            taiskasvanud.append(nimi)
        else:
            pensionarid.append(nimi)

    grupid = [lapsed, taiskasvanud, pensionarid]
    return grupid


# Programmi käivituspunkt
def main():
    # Loeme failist nimed ja vanused
    nimede_vanuste_dict = lae_vanused_failist(failinimi="vanused.txt")

    # Jagame inimesed vanusegruppidesse
    grupid = jaga_inimesed_gruppidesse(nimede_vanuste_dict)

    # Võtame grupid eraldi muutujatesse
    lapsed_list = grupid[0]
    taiskasvanud_list = grupid[1]
    pensionarid_list = grupid[2]

    # Muudame listid tekstiks, et neid oleks lihtne kuvada
    lapsed = ", ".join(lapsed_list)
    taiskasvanud = ", ".join(taiskasvanud_list)
    pensionarid = ", ".join(pensionarid_list)

    # Kuvame tulemuse kasutajale
    print(f"Lapsed (alla 13): {lapsed}\n"
          f"Täiskasvanud (13-64): {taiskasvanud}\n"
          f"Pensionärid (üle 64): {pensionarid}\n")


# Tagab, et main() käivitub ainult otse faili käivitamisel
if __name__ == "__main__":
    main()
