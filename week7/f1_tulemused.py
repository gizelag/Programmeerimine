#GLOBAALNE KONSTANT
F1_PUNKTID = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

"""Loeb tulemused failist ja tagastab kõik mittetühjad read listina.

Parameetrid:
failinimi (str): failinimi, mida soovitakse lugeda.

Tagastab:
list[str]: list mittetühjade ridadega
[]: tühi list, kui faili ei leitud või viga tekkis"""

def loe_tulemused(failinimi):

    """Loeb tulemused failist ja tagastab mittetühjad read listina."""
    try:
        with open(failinimi, 'r', encoding = 'utf-8') as f: #avame faili oiges kodeeringus
            read = f.readlines()
    except FileNotFoundError:
        print(f'Viga: faili {failinimi} ei leitud')
        return []

    tulemused = []
    for rida in read:
        rida = rida.strip()#eemaldame tuhikud ja reavahetused
        if rida:
            tulemused.append(rida)#lisame ainult mitteuhjad read

    return tulemused

def filtreeri_kehtivad_ajad(ajad, vigane_vaartus):
    """
       Filtreerib välja vigased ajad ja teisendab kehtivad ajad floatiks.

       Parameetrid:
           ajad (list[str]): ajad tekstina
           vigane_vaartus (int): väärtus, mida peetakse vigaseks (nt 999)

       Tagastab:
           list[float]: ainult kehtivad ajad
           []: kui kõik ajad olid vigased või sisend puudus
       """

    if not ajad:
        print("Viga, ajad puuduvad")
        return []

    kehtivad = []
    for a in ajad:
        try: # Teisendame aja arvuks ja kontrollime, et see ei oleks vigane
            if float(a) != vigane_vaartus:
                kehtivad.append(float(a))

        except ValueError: # Kui mõni aeg ei ole arv, jätame selle lihtsalt vahele
            continue
    return kehtivad

def leia_paim_aeg(kehtivad_ajad):
    """
       Leiab väikseima aja (parim aeg) sõitja ajaloendist.

       Parameetrid:
           kehtivad_ajad (list[float]): sõitja ajad

       Tagastab:
           float: kiireim aeg
           None: kui list on tühi
       """
    if not kehtivad_ajad:
        print("Viga, puuduvad kehtivad ajad")
        return None

    return min(kehtivad_ajad)   # parimad ajad ehk vaikseimad tagastab

def analuusi_praegusi_tulemusi(failinimi):
    """
    Parameeter:
    failinimi (str): Faili nimi, mis sisaldab käesoleva sõidu tulemusi
    Tagastab:
    dict: {nimi: parim_aeg} kõigi sõitjate kohta
    {}: Tühi sõnastik vea korral
    """
    # Kutsu valja func loe_tulemused
    # Kontrolli ega teksti list pole tuhi

    # FOr loop
        # Tootled iga rida eraldi
        # Tukelda
        # Eralda soitja nimi listist -> [Hamilton, 1, 2, 999, 5]
            # nimi = Hamilton
            # koik_ajad = [1, 2, 999, 5]
            # kutsu func filtreeri_kehtivad_ajad -> selle parameeter ajad = [1, 2, 999, 5]
                # See tagastab [1, 2, 5]
            # Leia min -> parameeter = [1, 2, 5] -> tagastab 1
              # Loo sonastik -> {Hamilton: 1}
    read = loe_tulemused(failinimi)
    if FileNotFoundError:
        print(f'Viga: faili {failinimi} ei leitud')
        return {}
    tulemused = {}
    for rida in read:
        osad = rida.split(";")
        nimi = osad[0].strip()
        ajad = osad[1].strip()
        kehtivad = filtreeri_kehtivad_ajad(ajad)
        parim = leia_parim_aeg(kehtivad)
        if parim is not None:
            tulemused[nimi] = parim
    return tulemused



def main():
    faili_sisu = loe_tulemused(failinimi="kaesolev_voor.txt")

    print(faili_sisu)

if __name__ == "__main__":
     main()
