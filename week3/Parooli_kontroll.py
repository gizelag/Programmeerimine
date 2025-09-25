def on_piisavalt_pikk(parool):
    return len(parool) >= 8

def sisaldab_tahti_ja_numbreid(parool):
    sisaldab_tahti = False
    sisaldab_numbreid = False

    for mark in parool:
        if mark.isalpha():
            sisaldab_tahti = True
        if mark.isdigit():
            sisaldab_numbreid = True
            print("See on number")
    return sisaldab_tahti and sisaldab_numbreid

def ei_sisalda_tuhikuid(parool):
    for mark in parool:
        if mark == " ":
            return False
        else:
            return True


def main():
    katsed = 5

    while katsed > 0:
        parool = input("Sisesta parool: ")

        if (ei_sisalda_tuhikuid(parool) and sisaldab_tahti_ja_numbreid(parool) and on_piisavalt_pikk(parool)):
            print("Parool aktsepteeritud.")
            return
        else:
            katsed -= 1
            if katsed > 0:
                print(f"Parool ei sobi. Alles on: {katsed} katset.")
            else:
                print("Liiga palju katseid. Ligipääs keelatud.")

if __name__ == "__main__":
    main()
