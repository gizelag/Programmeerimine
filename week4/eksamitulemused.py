def loe_tulemused(failinimi):
    try:
        with open(failinimi, 'r', encoding='utf-8') as fail:
            return fail.readlines()

    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None

def tootle_tulemusi(failisisu):
    ok_tulemused_counter = 0
    vigaste_read_counter = 0
    punktid_list = []

    try:
        if failisisu is None:
            return None

        for rida in failisisu:
            rida = rida.strip()

            try:
                if not rida:
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                if ';' not in rida:
                    vigaste_read_counter += 1
                    print(f"Viga: punktid ei ole number või puudub semikoolon – '{rida}'")
                    continue

                rea_osad = rida.split(';')
                if len(rea_osad) != 2:
                    vigaste_read_counter += 1
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                nimi = rea_osad[0].strip()
                if not nimi:
                    vigaste_read_counter += 1
                    print(f"Viga: puudulik rida – '{rida}'")
                    continue

                punktid = int(rea_osad[1].strip())

                ok_tulemused_counter += 1
                punktid_list.append(punktid)
                print(f'{nimi} sai eksamil {punktid} punkti')


            except (ValueError, IndexError):
                vigaste_read_counter += 1
                print(f"Viga: puudulik rida – '{rida}'")
                continue


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
            print('Ühtegi kehtivat eksamitulemust ei leitud')
            print(f'Vigaseid ridu kokku: {vigaste_read_counter}')


    except Exception as e:
        print("Töötlemisel tekkis viga:", e)
        return None

def main():
    failinimi = 'eksam_tulemused.txt'
    sisu = loe_tulemused(failinimi)
    tootle_tulemusi(sisu)

if __name__ == '__main__':
    main()
