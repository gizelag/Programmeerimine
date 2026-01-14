def on_piisavalt_pikk(parool):
    # Kontrollib, kas parool on vähemalt 8 tähemärki pikk
    return len(parool) >= 8


def sisaldab_tahti_ja_numbreid(parool):
    # Abimuutujad, mis jälgivad kas paroolis leidub tähti ja numbreid
    sisaldab_tahti = False
    sisaldab_numbreid = False

    # Käime parooli märgid ükshaaval läbi
    for mark in parool:
        # Kontrollime, kas märk on täht
        if mark.isalpha():
            sisaldab_tahti = True
            print("See on täht")
        # Kontrollime, kas märk on number
        elif mark.isdigit():
            sisaldab_numbreid = True
            print("See on number")

    # Kui parool sisaldab nii tähti kui ka numbreid, on tingimus täidetud
    if sisaldab_numbreid == True and sisaldab_tahti == True:
        return True
    else:
        return False


def ei_sisalda_tuhikuid(parool):
    # Kontrollib, et parool ei sisaldaks tühikuid
    for mark in parool:
        if mark == " ":
            return False
    return True


def main():
    # Maksimaalne lubatud katsete arv
    katsed = 5

    # Tsükkel töötab seni, kuni katseid on alles
    while katsed > 0:
        # Kasutajalt küsitakse parooli
        parool = input("Sisesta parool: ")

        # Kontrollitakse kõiki parooli tingimusi korraga
        if ei_sisalda_tuhikuid(parool) and sisaldab_tahti_ja_numbreid(parool) and on_piisavalt_pikk(parool):
            print("Parool aktsepteeritud.")
            return
        else:
            # Kui parool ei sobi, vähendatakse katsete arvu
            katsed -= 1
            if katsed > 0:
                print(f"Parool ei sobi. Alles on: {katsed} katset.")
            else:
                print("Liiga palju katseid. Ligipääs keelatud.")


# Kontroll, et programm käivitub ainult siis,
# kui faili käivitatakse otse (mitte ei impordita)
if __name__ == "__main__":
    main()
