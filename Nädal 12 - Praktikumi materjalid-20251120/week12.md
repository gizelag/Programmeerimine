# Week 12 – Kapseldamine ja @property

## Eesmärk

1. Õppida kasutama kapseldamist: `private` atribuudid ja `@property` dekoraatorid
2. Kasutada `@staticmethod` ja `@classmethod` rakendamist
3. Progeda, progeda ja progeda

---

## Seadistamine

1. Lae Moodlist alla kõik vajalikud `.json` ja `.csv` failid -> need on iga vastava nädala `Praktikumi materjalid` all
2. Loo kaust/directory nimega `week12`
3. Sinna kausta pane kõik vajaminevad failid ning salvesta sinna ka kõik selle nädala praktikumi ülesanded
4. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik atribuudid peavad olema kapseldatud ehk privaatsed: `_nimi`
2. Kõik vajalikud väärtused peavad kasutama `@property` gettereid ja settereid
3. Vigade käsitlus peab olema implementeeritud
4. Kood peab olema kommenteeritud ning loetav
5. Kasuta `@classmethod` ja `@staticmethod` seal, kus mõistlik
6. Kõik failid peavad käivituma ning olema testitud
7. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
8. Programmi käivitamine käib läbi:
    ```python
    if __name__ == "__main__":
        main()
    ```

**PS! Praktiline osa meelega natukene lühem, et teil oleks rohkem aega enda projekti jaoks. Te ju kasutate enda projektis ka klasse, eks?!**

---

## Ülesanne 1 – Linna planeerimine läbi kapseldamise

### Eesmärk
Võta eelmisel nädalal loodud `Maja` klass ja lisa sellele **kapseldamine** ning kasuta **`@property`**-t. Eesmärk on muuta kõik atribuudid turvaliseks ning kontrollida väärtuste õigsust setterites.

**Failinimi:** `kapseldatud_linna_planeerimine.py`

### Nõuded
1. Loo klass `Maja` ning selle klassi konstruktor:
    - **Parameetrid:**
        - `aadress` (str): Maja aadress
        - `korterite_arv` (int): Korterite arv majas
        - `ehitusaasta` (int): Aasta, mil maja ehitati
    - **Privaatsed atribuudid:**
        - `_aadress` (str): Maja aadress
        - `_korterite_arv` (int): Korterite arv majas
        - `_ehitusaasta` (int): Aasta, mil maja ehitati
        - `_elanike_arv` (int): Praegune elanike arv (algväärtus 0)
        - `_renoveeritud` (bool): Kas maja on renoveeritud (algväärtus False)
        - `_on_uus` (bool): Kas maja on uus → ehitatud pärast 2005. aastat
    - **Kirjeldus:**
        - Parameetrite tüübikontroll:
            - Kontrolli, et kõik parameetrid on õiget tüüpi:
                - `aadress` peab olema `str`
                - `korterite_arv` peab olema `int`
                - `ehitusaasta` peab olema `int`
                - Kui tüüp on vale, tekita `TypeError` koos selgitava sõnumiga
        - Väärtuste valideerimine:
            - Aadress ei tohi olla tühi → kasta `.strip()`-i
            - Korterite arv ei tohi olla negatiivne
            - Ehitusaasta peab olema kehtiv → kasuta `on_kehtiv_aasta()` staatlist meetodit
            - Kui väärtus on vale, tekita `ValueError` koos selgitava sõnumiga
        - Kui tüübid on õiged, siis loo privaatsed atribuudid

2. Loo `Property`-d ainult lugemiseks (GET):
    1. Loo meetod `aadress()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - `str`: Maja aadress: `_aadress`

    2. Loo meetod `korterite_arv()`
        - **Parameeter:**
            - Puudub
         - **Tagastab:**
            - `int`: Korterite arv: `_korterite_arv`

    3. Loo meetod `ehitusaasta()`
        - **Parameeter:**
            - Puudub
         - **Tagastab:**
            - `int`: Ehitusaasta: `_ehitusaasta`

    
    3. Loo meetod `on_uus_maja()`
        - **Parameeter:**
            - Puudub
         - **Tagastab:**
            - `bool`: True kui maja on ehitatud pärast 2005. aastat, False kui maja on ehitatud 2005 kaasaarvatud või varem: `_on_uus`

    4. Loo meetod `elanike_tihedus()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - float: Mitu elanikku on ühe korteri kohta
        - **Kirjeldus:**
            - Arvutab mitu elanikku on ühe korteri kohta:
                - Kui `korterite_arv` on 0, tagasta 0
                - Valem: `elanike_arv / korterite_arv` (ümardatud 2 komakohani)
    
    5. Loo meetod `maja_vanus()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - int: Maja vanus praeguse aasta järgi
        - **Kirjeldus:**
            - Arvutab maja vanuse praeguse aasta järgi:
                - Impordi `datetime`: `from datetime import datetime` ning otsi internetist, kuidas saada sealt aasta kätte
                - Valem: `praegune_aasta - ehitusaasta`

3. Loo `Property`-d nii lugemiseks kui ka kirjutamiseks (GET ja SET):
    1. Loo meetod `renoveeritud()`:
        - **GET meetod tagastab:**
            - Tagastab `_renoveeritud` väärtuse
        - **SET meetod:**
            - Kontrollib, kas uus väärtus on `bool` tüüpi:
                - Kui ei ole, tekitab `TypeError` koos selgitava sõnumiga
            - Muudab `_renoveeritud` väärtust
            - Kuvab sõnumi: `"Maja [aadress] on nüüd renoveeritud!"`

    2. Loo meetod `elanike_arv()`:
        - **GET meetod tagastab:**
            - Tagastab `_elanike_arv` väärtuse
        - **SET meetod:**
            - Kontrollib, kas väärtus on `int` tüüpi:
                - Tekita `TypeError` koos selgitava sõnumiga
            - Kontrollib, kas väärtus ei ole negatiivne:
                - Tekita `ValueError` koos selgitava sõnumiga
            - Muudab `_elanike_arv` väärtust

4. Loo staatiline meetod `on_kehtiv_aasta()`:
    - **Parameeter:**
        - `aasta` (int): Maja ehitusaasta
    - **Tagastab:**
        - `bool`: True kui kehtiv, False kui mitte
    - **Kirjeldus:**
        - Kontrollib, kas ehitusaasta on vahemikus **1800-2025**:
            - Kui maja ehitusaasta on vahemikus, siis tagasta True
            - Tagasta False kui maja ehitusaasta ei ole vahemikus
        - PS! See meetod ei sõltu konkreetsest maja objektist

5. Loo meetod `lisa_elanik()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Suurendab olemas olevate elanike arvu ühe võrra kasutades sobivat `setterit`
    - Käsitle võimalikke `ValueError` veateateid `try-except` plokiga:
        - Vea korral kuva selgitav sõnum
    - Kui uus elanik lisatakse edukalt kuva sõnum, näiteks: `"Majja [aadress] lisandus uus elanik. Elanikke kokku: [elanike_arv]"`

6. Loo meetod `eemalda_elanik()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Kui majas on rohkem kui 0 inimest:
        - Käsitle võimalikke `ValueError` veateateid `try-except` plokiga:
            - Vea korral kuva selgitav sõnum
        - Vähendab elanike arvu ühe võrra kasutades sobivat `setterit`
        - Kui elanik on edukalt eemaldatud kuva sõnum, näiteks: `"Majast [aadress] lahkus elanik. Elanikke kokku: [elanike_arv]"`
    - Kui majas pole ühtegi elanikku:
        - Kuvab sõnumi, näiteks: `"Majast [aadress] ei saa elanikku eemaldada, sest majas pole ühtegi elanikku!"`


7. Loo meetod `__str__()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - str: Vormindatud string maja andmetega
  - **Kirjeldus:**
    - Tagastab kõik maja andmed vormindatult stringina:
        - Renoveeritud välja tekst: `"Jah"` kui True, `"Ei"` kui False
        - Maja tüübi tekst: `"Uus maja"` kui True, `"Vana maja"` kui False
    - Tekst on kujul:
        ```
        Maja – [aadress]
        Ehitusaasta – [ehitusaasta]
        Vanus – [vanus] aastat
        Korterite arv: [korterite_arv]
        Elanike arv: [elanike_arv]
        Elanike tihedus: [tihedus] elanikku per korter
        Renoveeritud: [Jah/Ei]
        Maja tüüp: [Uus maja/Vana maja]
        ```

8. Loo funktsioon `main()`
- Loo neli erinevat `Maja` objekti
- Lisa ja eemalda elanike, kasutades sobivat meetodit
- Arvuta elanike tiheduse
- Renoveeri vähemalt üks `Maja` objekt
- Kasuta staatilist meetodit erinevate aastatega
- Maja vanuse kuvamine
- Vigade käsitlemise testimine, näiteks negatiivne elanike arv, vale ehitusaasta → vaata, kas su programm teeb seda, mida peab


9. Programmi käivitamine
  - **Kirjeldus:**
    - Käivita programm läbi `main()` funktsiooni:
    ```python
    if __name__ == "__main__":
        main()
    ```

---

## Ülesanne 2 – Kasutajate registreerimine, statistika kogumine ja parooli hashimine

### Andmefailid

Tutvu kahe failiga, mis sisaldab registreeritud kasutajate andmeid:

**Failinimi:** `kasutajad.csv`
- CSV fail 5 kasutaja andmetega
- Formaat: `kasutajanimi,eesnimi,perenimi,synnikuupaev,parool`
- Esimene rida on päis
- Paroolid on tavatekstina (krüpteeritakse programmi poolt)

**Failinimi:** `kasutajad.json`
- JSON fail 5 kasutaja andmetega
- Formaat: massiiv objektidest võtmetega `kasutajanimi`, `eesnimi`, `perenimi`, `synnikuupaev`, `parool`
- Paroolid on tavatekstina (krüpteeritakse programmi poolt)

### Ülesanne 2 vol1 - Kasutajate registreerimine

**Failinimi:** `registreeri_kasutaja.py`

### Nõuded
0. Impordi vajalik moodul: `from datetime import datetime`

1. Loo klass `Kasutaja` ning selle klassi konstruktor:
    - **Parameetrid:**
        - `kasutajanimi` (str): Kasutaja unikaalne kasutajanimi
        - `eesnimi` (str): Kasutaja eesnimi
        - `perenimi` (str): Kasutaja perekonnanimi
        - `synnikuupaev` (datetime): Kasutaja sünnikuupäev
    - **Atribuudid:**
        - `kasutajanimi` (str): Kasutajanimi
    - **Privaatsed atribuudid:**
        - `_eesnimi` (str): Eesnimi
        - `_perenimi` (str): Perekonnanimi
        - `_synnikuupaev` (datetime): Sünnikuupäev
    - **Klassimuutuja:**
        - `_kasutajate_arv` (int): Kõigi loodud kasutajate arv (algväärtus 0)
    - **Kirjeldus:**
        - Konstruktor salvestab kõik parameetrid atribuutidena
        - Suurendab klassimuutujat `_kasutajate_arv` ühe võrra

2. Loo `Property`-d ainult lugemiseks (GET):
    1. Loo meetod `taisnimi()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - `str`: Kasutaja täisnimi
        - **Kirjeldus:**
            - Tagastab kasutaja täisnime formaadis `"eesnimi perenimi"`

    2. Loo meetod `vanus()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - `int`: Kasutaja vanus
        - **Kirjeldus:**
            - Arvutab vanuse sünnikuupäeva põhjal:
                - Kasuta imporditud `datetime` moodulit:
                    - Otsi internetist, kuidas saada sealt aasta kätte
                - Valem: `praegune_aasta - synnikuupaev.year`
            - Tagasta arvutatud kasutaja vanus

3. Loo klassimeetodid:
    1. Loo meetod `loo_csv_reast()`:
        - **Parameeter:**
            - `csv_string` (str): CSV string formaadis `"kasutajanimi,eesnimi,perenimi,YYYY-MM-DD"`
        - **Tagastab:**
            - `Kasutaja`: Uus kasutaja objekt
        - **Kirjeldus:**
            - Parsi CSV string osadeks kasutades sobivat eraldajat
            - Konverteerb kuupäeva stringi `datetime` objektiks kasutades `synnikuupaev_obj = datetime.strptime(synnikuupaev, '%Y-%m-%d')`, kus synnikuupaev on failist loetud kasutaja sünnikuupäev
            - Loo ja tagasta uue kasutaja objekt kasutades `cls()`

    2. Loo meetod `loo_json_objektist()`:
        - **Parameeter:**
            - `registreeritud_kasutajad_dict` (dict): Sõnastik võtmetega `'kasutajanimi', 'eesnimi', 'perenimi', 'synnikuupaev'`
        - **Tagastab:**
            - `Kasutaja`: Uus kasutaja objekt
        - **Kirjeldus:**
            - Loeb andmed sõnastikust
            - Konverteeri kuupäeva kasutades `datetime.fromisoformat(registreeritud_kasutajad_dict['synnikuupaev'])`
            - Loob ja tagastab uue kasutaja objekti kasutades `cls()`

    3. Loo meetod `kasutajate_statistika()`:
        - **Parameeter:**
            - Puudub
        - **Tagastab:**
            - `str`: Teade kujul "Süsteemis on X kasutajat"
        - **Kirjeldus:**
            - Tagastab loodud kasutajate koguarvu klassimuutujast
            - Tagasta tekst näiteks kujul: `"Süsteemis on X kasutajat"`, kus X on kasutajate koguarv

4. Loo staatilised meetodid:
    1. Loo meetod `valideeri_kasutajanimi()`:
        - **Parameeter:**
            - `kasutajanimi` (str): Kontrollitav kasutajanimi
        - **Tagastab:**
            - `tuple`: (bool, str) → Kas on korrektne ja teade
        - **Kirjeldus:**
            - Kontrollib, et kasutajanimi on vähemalt 3 tähemärki pikk:
                - Vea korral tagasta False ja vastav veateade, näiteks: `Kasutajanimi peab olema vähemalt 3 tähemärki`
            - Kontrollib, et kasutajanimi sisaldab ainult tähti ja numbreid, kasuta `isalnum()`:
                - Vea korral tagasta False ja vastav veateade, näiteks: `Kasutajanimi võib sisaldada ainult tähti ja numbreid`
            - Kui kasutajanimi on sobiv:
            - Tagastab True ja tekst `OK`

5. Testi oma klassi:
    - ```python
        if __name__ == "__main__":
            ...
        ```
    - Pane `if __name__ == "__main__":` ploki all enda kood:
        - Testi kas klassimeetodid ja property'd töötavad

---

### Ülesanne 2 vol2 - Paroolihaldur

**Failinimi:** `paroolihaldur.py`

### Nõuded
0. Impordi vajalikud moodulid:
    ```python
    import hashlib
    import json
    ```

1. Loo klass `ParooliHaldur`:
    - **Klassimuutuja:**
        - `_paroolid` (dict): Kõik registreeritud paroolid kujul `{kasutajanimi: parool_hash}`
    - **Konstruktor parameetrid:**
        - `kasutajanimi` (str): Kasutaja, kelle parooli hallatakse
    - **Privaatsed atribuudid:**
        - `_kasutajanimi` (str): Kasutajanimi
        - `_parool_hash` (str): Krüpteeritud parool (algväärtus None)

2. Loo `@property` getter ja setter `parool_hash`:
    - **Getter tagastab:**
        - `str`: Krüpteeritud parooli räsi või None
    - **Setter:**
        - **Parameeter:**
            - `parool` (str): Kasutaja parool
        - **Kirjeldus:**
        - Seab parooli ehk valideerib ja krüpteerib:
            - Võtab vastu parooli tavatekstina
            - Valideerib parooli kasutades `valideeri_parool()` meetodit
            - Kui parool on nõrk, kuvab veateate, näiteks kujul: `Viga kasutajal {kasutaja_nimi} : {teade}`
        - Kui parool on tugev, krüpteerib selle ja salvestab `_parool_hash` atribuuti
        - Lisab parooli ka klassimuutujasse `_paroolid` kujul `{kasutajanimi: parool_hash}`

3. Loo staatilised meetodid:
    1. Loo meetod `valideeri_parool()`:
        - **Parameeter:**
            - `parool` (str): Kontrollitav parool
        - **Tagastab:**
            - `tuple`: (bool, str) → Kas on tugev ja teade
        - **Kirjeldus:**
            - Kontrollib parooli tugevust:
                - Vähemalt 8 tähemärki:
                    - Vea korral tagasta False ja vastav veateade, näiteks: `Parool peab olema vähemalt 8 tähemärki`
                - Sisaldab vähemalt ühte suurtähte:
                    - Vea korral tagasta False ja vastav veateade, näiteks: `Parool peab sisaldama suurtähte`
                - Sisaldab vähemalt ühte numbrit:
                    - Vea korral tagasta False ja vastav veateade, näiteks: `Parool peab sisaldama numbrit`
            - Kui parool on tugev, tagaasta True ja vastav teade, näiteks: `Parool on tugev`  

    2. Loo meetod `krüpteeri_parool()`:
        - **Parameeter:**
            - `parool` (str): Krüpteeritav parool
        - **Tagastab:**
            - `str`: SHA-256 räsiväärtus
        - **Kirjeldus:**
            - Krüpteerib parooli kasutades SHA-256 algoritmi, kasuta selleks: `hashlib.sha256(parool.encode()).hexdigest()`, kus `parool` on krüpteeritav parool
            - Tagasta krüpteeritud parooli

4. Loo klassimeetodid:
    1. Loo meetod `salvesta_paroolid_faili()`:
        - **Parameeter:**
            - `failinimi=paroolid.json` (str): Faili nimi, kuhu paroolid salvestatakse (vaikeväärtus: `paroolid.json`)
        - **Kirjeldus:**
            - Salvestab klassimuutuja `_paroolid` JSON faili
            - Kasuta `try-except` plokki vea püüdmiseks:
                - Vea korral kuva veateade
            - Kui salvestamine õnnestus:
                - Kuvab teate salvestamise õnnestumisest, näiteks: `Paroolid salvestatud faili: {failinimi}`
            - Täpsustus failinimi: `paroolid.json`:
                - JSON fail räsitud paroolidega
                - Formaat: sõnastik kujul `{"kasutajanimi": "räsitud_parool"}`

    2. Loo meetod `paroolide_arv()`:
        - **Tagastab:**
            - `int`: Registreeritud paroolide arv
        - **Kirjeldus:**
            - Tagastab registreeritud paroolide arvu

5. Testi oma klasi:
    - ```python
        if __name__ == "__main__":
            ...
        ```
    - Kutsu `if __name__ == "__main__":` ploki all meetodid välja:
        - Testi parooli seadmist kasutades `@property` setterit
        - Testi nõrga parooli käitumist
        - Kuva ühe kasutaja räsi kasutades getterit
        - Kuva statistika kasutades `paroolide_arv()`
        - Salvesta paroolid faili kasutades `salvesta_paroolid_faili()`

#### Faili `paroolid.json` sisu:

```json
{
    "anna123": "40358877c4787c69fb9938af7b64cb8bf93392c9ec9d23f31e1006c06c01bb7e",
    "liisa88": "1ebb7fc10ec7872b5241783674648e4a7ba73338b0885feb6ed6ce7f8f727c67",
    "marten2000": "e630d15bf8e02d69d1a448844eaf0e48e319f7608ee8470e0a2cb04da6d7c984",
    "kertu95": "4abffaa1ef96b06e307c3cc66b8d540246d3c816cf0a961acb370bcc6370a3be",
    "lottebiceps": "8d35b5262a40c2c214945f2da661c6c4472bca617c76a6aef66da628318a45fd",
    "karl420": "fd084535a40b0e49e712111f8c95faa11620a3292ac5e27f6c14a561e50fa7f7",
    "raul1234": "5d23a89b37a799ff4aedfafb5ae9fa5f55310acb6b29317f28ab6b8c3ae55c61",
    "jaana111": "86414ba56b122c7e6a4530056a9899fb188281aeae2df97fdd6c4184f12ca758"
}
```

---

### Ülesanne 2 vol3 - Failide lugemine eraldi moodulis

**Failinimi:** `faili_lugemine.py`

### Nõuded
0. Impordi vajalik moodul:
    ```python
    import json
    ```

1. Loo klass `FailiLugeja`:
    - **Kirjeldus:**
        - Universaalne klass failidest andmete lugemiseks
        - Ei sõltu teistest klassidest - tagastab toored andmed sõnastikena

2. Loo staatiline meetod `loe_csv_failist()`:
    - **Parameeter:**
        - `failinimi` (str): CSV faili nimi
    - **Tagastab:**
        - `list`: Nimekiri sõnastikest (toored andmed)
    - **Kirjeldus:**
        - Ava faili lugemiseks
        - Määra sobiv `encoding`
        - Loe päiserida ja tee sellest võtmete nimekiri kasutades sobivat erladajat
        - Loeb iga rea ja loob sõnastiku päise võtmete ja rea väärtuste põhjal
        - Tagastab kõik andmed nimekirjana sõnastikest

3. Loo staatiline meetod `loe_json_failist()`:
    - **Parameeter:**
        - `failinimi` (str): JSON faili nimi
    - **Tagastab:**
        - `list`: Nimekiri sõnastikest (toored andmed)
    - **Kirjeldus:**
        - Ava faili lugemiseks
        - Määra sobiv `encoding`
        - Laeb JSON andmed kasutades `json.load()`
        - Tagastab andmed otse (JSON massiiv ongi nimekiri sõnastikest)

4. Testi oma klassi:
    - ```python
        if __name__ == "__main__":
            ...
        ```
    - Pane `if __name__ == "__main__":` ploki all enda kood:
        - Testi kas mõlemad meetodid töötavad

---

### Ülesanne 2 vol3 - Main programm

**Failinimi:** `main.py`

1. Impordi vajalikest failidest vajalikud klassid

2. Loo funktsioon `main()`
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - Puudub
    - **Kirjeldus:**
        - Loe kasutajate andmed CSV failist:
            - Loe toored andmed kasutades sobiva klassi meetodit
            - Loo `Kasutaja` objektid kasutades sobivat meetodit
            - Valideeri kasutaja kasutajanimi kasutades sobivat meetodit:
                - Kui kasutajanimi pole kehtiv kuva teade ja jätka
            - Loo `ParooliHaldur` objekt iga kasutaja jaoks
            - Valideeri paarol ja loo hashitud parool kasutades `@property` setterit
            - Kuva kasutaja info:
                - Kuva kasutajate täisnimed ja vanused
                - NB! Parooli valideerimise veateade kuvatakse automaatselt `@property` setteri poolt
        - Loe kasutajad JSON failist:
            - Loe toored andmed kasutades sobiva klassi meetodit
            - Loo `Kasutaja` objektid kasutades sobivat meetodit
            - Valideeri kasutaja kasutajanimi kasutades sobivat meetodit:
                - Kui kasutajanimi pole kehtiv kuva teade ja jätka
            - Loo `ParooliHaldur` objekt iga kasutaja jaoks
            - Valideeri paarol ja loo hashitud parool kasutades `@property` setterit
            - Kuva kasutaja info:
                - Kuva kasutajate täisnimed ja vanused
                - NB! Parooli valideerimise veateade kuvatakse automaatselt `@property` setteri poolt
        - Salvesta räsitud/hashitud paroolid faili:
            - Kasuta sobiva klassi meetodit
        - Kuva lõplik statistika:
            - Kuva loodud kasutajate arv kasutades sobiva klassi meetodit
            - Kuva registreeritud paroolide arv kasutades sobiva klassi meetodit

3. Programmi käivitamine
    - **Kirjeldus:**
        - Käivita programm läbi `main()` funktsiooni:
        ```python
        if __name__ == "__main__":
            main()
        ```

#### Põhiprogrammi väljund:

```bash
--- Kasutajad CSV failist ---
Anna Tamm, vanus: 30
Peeter Kask, vanus: 26
Viga kasutajal peeter99: Parool peab olema vähemalt 8 tähemärki
Liisa Mets, vanus: 37
Märten Sepp, vanus: 25
Kertu Rebane, vanus: 30

--- Kasutajad JSON failist ---
Lotte Muskel, vanus: 25
Karl Kask, vanus: 26
Toomas Kuusk, vanus: 17
Viga kasutajal mesikapp: Parool peab olema vähemalt 8 tähemärki
Raul Kapp, vanus: 20
Jaana Kask, vanus: 26

--- Salvestame paroolid ---
Paroolid salvestatud faili: paroolid.json

Süsteemis on 10 kasutajat
Registreeritud paroole: 8
```

---
