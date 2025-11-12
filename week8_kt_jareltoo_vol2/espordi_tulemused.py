ESPORDI_PUNKTID = {'W': 2, 'L': 1, 'E': 0} #globaalne konstant

def arvuta_turniiri_punktid(tiimi_mangude_tulemused):
    if not tiimi_mangude_tulemused:#veakontroll
        print("Viga, mängude nimekiri on tühi.")
        return None
    try:#arvutame punktid iga mangu kohta
        return sum(ESPORDI_PUNKTID.get(tulemus.strip(), 0) for tulemus in tiimi_mangude_tulemused)
    except Exception as e:#uldine veakontroll
        print(f"Viga punktide arvutamisel: {e}")
        return None

def loeme_tulemused(failinimi):#tegin abifunktsiooni tulemuste lugemiseks
    try:
        with open (failinimi,'r', encoding = 'utf-18') as file:#avame faili lugemiseks
            read = [rida.strip() for rida in file if rida.strip()]#eraldame
        return read
    except FileNotFoundError:#veakasitlus
        print(f"Viga: faili '{failinimi}' ei leitud.")
        return []
    except Exception as e:
        print(f"Viga faili '{failinimi}' lugemisel: {e}")
        return []


def analuusi_kaesolevat_turniiri(kaesoleva_turniiri_failinimi):

    read = loeme_tulemused(kaesoleva_turniiri_failinimi)  # kasuatme abifunktsiooni faili lugemiseks
    if not read:#veakasitlus
        print("Viga: käesoleva vooru fail on tühi või puudub.")
        return {}
    # Eraldame vastavalt, vaatab kas väärtused on korrektsed ja loeb punkte
    tulemused = {}
    for rida in read:
        osad = rida.split(";")
        if len(osad) < 2:
            continue

    #jatkame eraldamist tiimidest ja punktidest
    meeskond = osad[0].strip()
    mangud = [t.strip() for t in osad[1:] if t.strip() in ESPORDI_PUNKTID.keys()]
    punktid = arvuta_turniiri_punktid(mangud)  # kasutame arvuta vooru punktid funktsiooni et arvutada vooru summa
    if punktid is not None:
        tulemused[meeskond] = punktid

def analuusi_eelmist_turniiri(eelmise_turniiri_failinimi):

    read = loeme_tulemused(eelmise_turniiri_failinimi)#kasutame loodud abifunktsiooni
    if not read:#veakasitlus
        print("Viga, eelmise vooru fail on tühi või puudub.")
        return {}

# muudame punktid int tüübiks ja koostame sõnastiku

    tulemused = {}
    for rida in read:
        try:#kasutame try except plokki et konventeerida punktid int tuupi
            meeskond, punktid = rida.split(";")
            tulemused[meeskond.strip()] = int(punktid.strip())
        except ValueError:#kui ei saa konventeerida int tuupi siis jatab vahele ja jatkab
            print(f"Viga andmereas: '{rida}' - ei saanud punkte teisendada.")
            continue
        except Exception as e:#uldine veakasitlus
            print(f"Viga eelmise vooru andmete töötlemisel: {e}")
            continue

    return tulemused#tagastab tulemused

def koosta_koondedetabel(eelmise_turniiri_punktid, kaesoleva_turniiri_punktid):
    if not eelmise_turniiri_punktid or not kaesoleva_turniiri_punktid:
        print("Viga, mõlema turniiri andmed puuduvad.")
        return {}

#liidame kokku
    koondtabel = {}
    for meeskond in set(eelmise_turniiri_punktid.keys()) | set(kaesoleva_turniiri_punktid.keys()):
        eelmine = eelmise_turniiri_punktid.get(meeskond, 0)
        kaesolev = kaesoleva_turniiri_punktid.get(meeskond, 0)
        koondtabel[meeskond] = eelmine + kaesolev

    #sorteerime kahanevalt kogupunktide jargi
    sorteeritud = sorted(koondtabel.items(), key=lambda item: item[1], reverse=True)
    return dict(sorteeritud)

    '''koondedetabel = {}#teeme dicti
    for meeskond, punktid in sorteeritud_list:
        koondedetabel[meeskond] = punktid'''

    return koondedetabel
def salvesta_edetabel(koondpunktid, edetabeli_failinimi="koondedetabel.txt"):

    if not koondpunktid:
        print('Viga, koondpunktid puuduvad')
        return
# määrame kuidas peab välja nägema koondtabel
    try:
        with open(edetabeli_failinimi, 'w', encoding='utf-8') as fail:
            koht = 1

            for meeskond, punktid in koondpunktid.items():
                rida = f'{koht}. koht: {meeskond} – {punktid}\n'
                fail.write(rida)
                koht = koht + 1

    except Exception as e:
        print(f"Viga, fail {e}")

    print(f"Fail{edetabeli_failinimi} on salvestatud")

def main():
    eelmise_turniiri_failinimi = "eelmine_turniir.txt"
    kaesoleva_turniiri_failinimi = "kaesolev_turniir.txt"

    eelmise_turniiri_punktid = analuusi_eelmist_turniiri(eelmise_turniiri_failinimi)
    kaesoleva_turniiri_punktid = analuusi_kaesolevat_turniiri(kaesoleva_turniiri_failinimi)

    koondtabel = koosta_koondedetabel(eelmise_turniiri_punktid, kaesoleva_turniiri_punktid)
    salvesta_edetabel(koondtabel)

if __name__ == "__main__":
    main()

