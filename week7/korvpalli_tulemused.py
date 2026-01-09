KORVPALLI_PUNKTID = {'W': 2, 'L': 1, 'X': 0}

def loe_tulemused(failinimi):
    #kasutan oiget encodengut faili avamiseks
    try:
        with open(failinimi, 'r', encoding='utf-8') as fail:#lugemiseks
            read = fail.readlines()#tootlen igat rida

    except FileNotFoundError:#veatootlemine kui faili ei leia
        print(f'Viga, faili {failinimi} ei leitud')
        return []#tagastab tuhja listi

    except Exception as e:#veakasitlus uleuldise vea korral
        print(f'Viga: {e}')
        return []
    # Eemaldan tühjad read ja tagastame tulemuste listi
    tulemused = []
    for rida in read:#tootlemas igat rida eraldi
        rida = rida.strip()#eemaldame igast reast tuhikud
        if rida != '':#rida ei tohi olla tuhi
            tulemused.append(rida)#read mis pole tuhjad lisame listi
    return tulemused#tagastab listi

def arvuta_vooru_punktid(tulemused):
    if not tulemused:#kontrollime sisendi olemasolu
        print('Viga')#kui sisend puudub veateade
        return None#ja tagastame none

    punktid = 0#arvutame punktid iga mangu kohta
    for tulemus in tulemused:
        if tulemus in KORVPALLI_PUNKTID:
            punktid += KORVPALLI_PUNKTID[tulemus]
        else:
            print('Viga')

    return punktid


def analuusi_kaesolevat_vooru(kaesoleva_vooru_failinimi):
    read = loe_tulemused(kaesoleva_vooru_failinimi)#kasutame loodud abifunktsiooni
    if not read:
        return {}

    tulemused_dict = {}
    for rida in read:
        osad = rida.split(';')#eraldame osad,ehk tukeldame rea sobiva eraldajaga
        if len(osad) < 2:#kui alla kahe siis vigane rida
            print('Viga')
            continue
        #jatkame iga meeskonna andmete eraldamist et arvutada punktidkokku
        meeskond = osad[0].strip()
        mangud = []
        for tulemus in osad[1:]:#arvutame vooru punktid
            tulemus = tulemus.strip()#eraldame tuhikud tulemusest
            if tulemus:
                mangud.append(tulemus.upper())#valjastab tulemuse koos loppu kirjatud apendiga

        punktid = arvuta_vooru_punktid(mangud)#kasutame teist funktsiooni et arvutada puntiskoori  summa
        if punktid is not None:#kui tootab siis tagastame punktid
            tulemused_dict[meeskond] = punktid
    return tulemused_dict


def analuusi_eelmist_vooru(eelmise_vooru_failinimi):
    read = loe_tulemused(eelmise_vooru_failinimi)#kasutame loodud abifunktsiooni
    if not read:
        return {}

    tulemused_dict = {}#selleks et toodelda meeskonda ja punkte peame enne eraldama need nagu ennegi seda tegime
    for rida in read:
        osad = rida.split(';')
        if len(osad) != 2:
            print('Viga')
            continue

        meeskond = osad[0].strip()#meeskond on osa 0 ja me votame eest tagant tuhikud ara temajaoks
        try:#kasutame try except plokki et konventeerida punktid int tuupi
            punktid = int(osad[1].strip())
            tulemused_dict[meeskond] = punktid

        except ValueError:#kui ei saa konventeerida int tuupi siis jatab vahele ja jatkab
            print('Viga')
            continue
    return tulemused_dict#tagastab tulemused


def koosta_koondedetabel(eelmise_vooru_punktid, kaesoleva_vooru_punktid):
    #veakontroll,kontrollime et sonastikud poleks tyhjad
    if not eelmise_vooru_punktid or not kaesoleva_vooru_punktid:
        print('Viga')#kuvab veateate
        return {}#tagastab tuhja sonastiku
    koondtabel = {}
#liidame punktid kokku
    for meeskond in set(eelmise_turniiri_punktid.keys()) | set(kaesoleva_turniiri_punktid.keys()):
        eelmine = eelmise_turniiri_punktid.get(meeskond, 0)
        kaesolev = kaesoleva_turniiri_punktid.get(meeskond, 0)
        koondtabel[meeskond] = eelmine + kaesolev

    for meeskond in kaesoleva_vooru_punktid:
        if meeskond in meeskonna_punktid:
            meeskonna_punktid[meeskond] += kaesoleva_vooru_punktid[meeskond]
        else:
            meeskonna_punktid[meeskond] = kaesoleva_vooru_punktid[meeskond]
    #sorteerime kahanevalt kogupunktide jargi
    sorteeritud_list = sorted(meeskonna_punktid.items(), key=lambda item: item[1], reverse=True)

    koondedetabel = {}#teeme dicti
    for meeskond, punktid in sorteeritud_list:
        koondedetabel[meeskond] = punktid

    return koondedetabel


def salvesta_edetabel(koondpunktid, edetabeli_failinimi="korvpalli_koondedetabel.txt"):
    if not koondpunktid:#veakasitlus, kontrollime et psonastik koondpunktid poleks tyhi
        print('Viga')
        return None

    try:#loome uue faili ülekirjutamiseks
        with open(edetabeli_failinimi, 'w', encoding='utf-8') as fail:#avame faili ulekirjutamiseks
            koht = 1
            for meeskond in koondpunktid:#maarame kuidas edetabel valja peab nagema
                fail.write(f'{koht}. koht: {meeskond} – {koondpunktid[meeskond]}\n')
                koht += 1#iga jargnev koht uks nr suurem
        print(f"Koondpunktide tabel edukalt salvestatud faili '{edetabeli_failinimi}'")

    except Exception as e:#veakasitlus
        print(f'Viga: {e}')


def main():#kutsume main funktsiooni valja
    #paneme kirja mis funktsioon millise txt failiga sobib
    eelmise_vooru_fail = 'eelmine_voor.txt'
    kaesoleva_vooru_fail = 'kaesolev_voor.txt'

    #votame eelmise ja kaesoleva vooru punktid ja paneme vorduma nende analuusiga
    eelmise_vooru_punktid = analuusi_eelmist_vooru(eelmise_vooru_fail)
    kaesoleva_vooru_punktid = analuusi_kaesolevat_vooru(kaesoleva_vooru_fail)

    koondpunktid = koosta_koondedetabel(eelmise_vooru_punktid, kaesoleva_vooru_punktid)
    salvesta_edetabel(koondpunktid)

if __name__ == '__main__':
    main()