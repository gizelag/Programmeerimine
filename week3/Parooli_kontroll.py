def on_piisavalt_pikk(parool):
    return len(parool) >= 8
    count = 0
    for sisaldab_tahti_ja_numbreid in parool:
        count += 1

def sisaldab_tahti_ja_numbreid(parool):
    sisaldab_tahti = False
    sisaldab_numbreid = False
    for sisaldab_tahti_ja_numbreid in parool:
        char = 'a'
        if char.isalpha():
            sisaldab_tahti = True
            elif char.isdigit():
            sisaldab_numbreid = True
            print("See on number")
            return sisaldab_tahti and sisaldab_numbreid

def ei_sisalda_tuhikuid(parool):
    for tuhik in parool:
        if tuhik == " "
            return False
        return True

 def main ():
    katsed = 5
    while katsed > 0:
        parool = input("Sisesta parool: ")
        if ei_sisalda_tuhikuid(parool):
            and sisaldab_tahti_ja_numbreid(parool):
            print("Parool aktsepteeritud.")
            return
        katsed -= 1
        if katsed > 0:
            print("Parool ei vasta nõuetele. Katseid jäänud: {katsed}")
        else:
            print("Liiga palju katseid. Ligipääs keelatud.")
if __name__ == "__main__":

