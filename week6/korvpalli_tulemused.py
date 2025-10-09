KORVPALLI_PUNKTID = {'W': 2, 'L': 1, 'X': 0}
def loe_tulemused(failinimi):

    try:
        with open(failinimi, 'a', encoding='utf-8') as fail:
            tekst = fail.append().strip()#eemaldame tuhikud
            return tekst

    except Exception as e:#veakasitlus tundmatu vea korral, tagastab tuhja listi
        print("Tundmatu viga")
        return []

def arvuta_vooru_punktid(tulemused):
    mangude_tulemused = ['W', 'L', 'X']
    KORVPALLI_PUNKTID = {'W': 2, 'L': 1, 'X': 0}

    try:
        with open(tulemused, 'r', encoding='utf-8') as tulemused:
            return mangude_tulemused.index(tulemused.read().strip())
        if arvuta_vooru_punktid(tulemused) == None or == []:
            print("Viga")
            return None


def analuusi_eelmist_vooru(eelmise_vooru_failinimi):
    nimi = rea_osad[0].strip
    punktid = int(rea_osad[1].strip())
    with open loe_tulemused(failinimi) as 'r':
        try:



def koosta_koondetabel(eelmise_vooru_punktid, kaesoleva_vooru_punktid):
    koond = {}
    for nimi, pts in (eelmise_vooru_punktid or items{}):
        koond[nimi] = koond.get(nimi, 0)













