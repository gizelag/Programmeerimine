def loe_tulemused(failinimi):
    try:
        with open(failinimi, "r", encoding="utf-8") as fail:
            return fail.readlines()
    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None

def arvuta_hinne(tudengite_punktid):
    if 90 <= tudengite_punktid <= 100:
        return 5
    elif 75 <= tudengite_punktid <= 89:
        return 4
    elif 50 <= tudengite_punktid <= 74:
        return 3
    elif 0 <= tudengite_punktid <= 49:
        return 2
    else:
        return None

def tootle_tulemusi(failisisu):
    if failisisu is None:
        return None

    kehtivad_tulemused = ''
    try:
        for rida in failisisu:
            rida = rida.strip()

            if not rida:
                continue

            try:
                if ';' not in rida:
                    print(f"Viga: punktid ei ole number või puudub semikoolon – '{rida}'")
                    continue

                osad = rida.split(';')
                if len(osad) != 2:
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                nimi = osad[0].strip()
                punktid_str = osad[1].strip()

                if not nimi:
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                punktid = int(punktid_str)

                if not (0 <= punktid <= 100):
                    print(f"Viga: punktid väljaspool vahemikku 0-100 – '{rida}'")
                    continue

                hinne = arvuta_hinne(punktid)
                print(f"{nimi} sai eksamil {punktid} punkti (hinne: {hinne})")

                kehtivad_tulemused += f'{nimi};{punktid};{hinne}\n'

            except (ValueError, IndexError) as e:
                print(f"Viga: punktid ei ole number või puudub semikoolon – '{rida}'")
                continue

        if kehtivad_tulemused:
            kirjuta_tulemused_faili(kehtivad_tulemused)
        else:
            print('Ühtegi kehtivat tulemust ei leitud')

    except Exception as e:
        print(f'Töötlemisel tekkis viga: {e}')
        return


def kirjuta_tulemused_faili(kehtivad_tulemused):
    txt_fail = 'toodeldud_eksamitulemused.txt'
    try:
        with open(txt_fail, "w", encoding="utf-8") as fail:
            fail.write(kehtivad_tulemused)
        print(f"Tulemused salvestatud faili '{txt_fail}'")
    except Exception as e:
        print(f'Viga faili kirjutamisel: {e}')


def main():
    failinimi = 'eksam_tulemused.txt'
    sisu = loe_tulemused(failinimi)
    tootle_tulemusi(sisu)

if __name__ == '__main__':
    main()