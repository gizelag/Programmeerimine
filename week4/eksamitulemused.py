# Loeb eksamitulemused tekstifailist
# Tagastab faili read listina
def loe_tulemused(failinimi):
    try:
        # Avame faili lugemiseks UTF-8 kodeeringuga
        with open(failinimi, 'r', encoding='utf-8') as fail:
            return fail.readlines()

    # Kui faili ei leita, anname veateate ja lõpetame lugemise
    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None


# Töötleb eksamitulemuste read ja teeb kokkuvõtte
def tootle_tulemusi(failisisu):
    # Loendur korrektsete tulemuste jaoks
    ok_tulemused_counter = 0

    # Loendur vigaste ridade jaoks
    vigaste_read_counter = 0

    # List punktide salvestamiseks statistika arvutamiseks
    punktid_list = []

    try:
        # Kui failisisu puudub, ei ole midagi töödelda
        if failisisu is None:
            return None

        # Töötleme iga faili rida eraldi
        for rida in failisisu:
            rida = rida.strip()

            try:
                # Tühi rida on vigane
                if not rida:
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                # Kontrollime, et eraldajaks oleks semikoolon
                if ';' not in rida:
                    vigaste_read_counter += 1
                    print(f"Viga: punktid ei ole number või puudub semikoolon – '{rida}'")
                    continue

                # Jagame rea nimeks ja punktideks
                rea_osad = rida.split(';')
                if len(rea_osad) != 2:
                    vigaste_read_counter += 1
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                # Kontrollime, et nimi ei oleks tühi
                nimi = rea_osad[0].strip()
                if not nimi:
                    vigaste_read_counter += 1
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                # Teisendame punktid täisarvuks
                punktid = int(rea_osad[1].strip())

                # Kui kõik kontrollid läbitud, loeme tulemuse korrektseks
                ok_tulemused_counter += 1
                punktid_list.append(punktid)

                # Kuvame ühe õpilase tulemuse
                print(f'{nimi} sai eksamil {punktid} punkti')

            # Kui punktid ei ole number või indeks puudub
            except (ValueError, IndexError):
                vigaste_read_counter += 1
                print(f"Viga: puudulik rida – '{rida}'")
                continue

        # Kui vähemalt üks korrektne tulemus olemas, arvutame statistika
        if ok_tulemused_counter > 0:
            min_punktid = min(punktid_list)
            max_punktid = max(punktid_list)
            avg_punktid = round(sum(punktid_list) / len(punktid_list))

            print(f'Korrektseid tulemusi: {ok_tulemused_counter}')
            print(f'Vigaseid ridu kokku: {vigaste_read_counter}')
            print(f'Keskmine punktiskoor: {avg_punktid}')
            print(f'Miinimum punktid: {min_punktid}')
            print(f'Maksimum punktid: {max_punktid}')
        else:
            # Kui ühtegi korrektset tulemust ei leitud
            print('Ühtegi kehtivat eksamitulemust ei leitud')
            print(f'Vigaseid ridu kokku: {vigaste_read_counter}')

    # Üldine kaitse ootamatute vigade vastu
    except Exception as e:
        print("Töötlemisel tekkis viga:", e)
        return None


# Programmi käivituspunkt
def main():
    # Määrame faili nime
    failinimi = 'eksam_tulemused.txt'

    # Loeme faili sisu
    sisu = loe_tulemused(failinimi)

    # Töötleme tulemusi
    tootle_tulemusi(sisu)


# Tagab, et main() käivitub ainult otse faili käivitamisel
if __name__ == '__main__':
    main()
