# Week 8 – Kontrolltöö 1, järeltöö - praktiline osa

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week8_kt_jareltoo`
2. Sinna kausta loo kõik selle nädala praktikumi ülesanded
3. Lae Moodlist alla kõik vajalikud `.txt` failid, need leiate Moodlist: `Nädal 8 - Vahe nädal/Kontrolltöö 1 järeltöö` -> `Kontrolltöö 1, järeltöö - Praktiline osa, failid`
4. Sinna kausta pane:
    1. Kõik allalaetud `.txt` failid
    2. Sinu loodud kood
    3. Ülesande käigus loodud `.txt` fail
5. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

**PS! Enda koode saab hakata testima alates `09:30-10:00`**

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
6. Lisa `GitLabi` ka kõik `.txt` failid
7. Oma lahendus peab olema esitatud kell 10:00

---

## PS! Alusta algusest, loo üks funktsioon ära, testi seda (kutsu `main()` funktsioonis see välja) ning liigu edasi.

## Ülesanne 1: E-spordi turniiride tulemuste analüüs ja punktiarvestus
**Failinimi:** `espordi_tulemused.py`

### Eesmärk
Sa töötad e-spordi organisatsioonis League of Legends võistluste andmeanalüütikuna. Sul on kaks faili kahe erineva turniiri tulemustega ning sa pead:
1. Töötlema ja filtreerima käesoleva turniiri tulemusi
2. Analüüsima eelmise turniiri tulemusi
3. Jagama punktid e-spordi süsteemi järgi mõlema turniiri eest
4. Koostama lõpliku edetabeli

### Ettevalmistus
1. Tutvu failiga `eelmine_turniir.txt` sisuga:
    - Fail `eelmine_turniir.txt` sisaldab juba töödeldud andmeid, kus igas reas on `tiim;punktid`
    - Iga tiimi nime taga on selle turniiri punktid
2. Tutvu failiga `kaesolev_turniir.txt` sisuga:
    - Nende andmetega pole andmetöötlust tehtud. On vaja eemaldada vigased andmed (E märgid) ning arvutada iga tiimi punktid
    - Fail `kaesolev_turniir.txt` sisaldab andmeid, kus igas reas on `tiim;mang1;mang2;mang3;mang4;mang5`
    - Mängude tulemused on kujul:
        - `W` (win), mis tähistab võitu
        - `L` (loss), mis tähistab kaotust
        - `E` (error), mis tähistab tehnilise vea tõttu toimumata jäänud mängu
    - Fail sisaldab ka vigaseid andmeid -> `E`
3. Tutvu e-spordi punktisüsteemiga:
    - Punktisüsteem on selline: `{'W': 2, 'L': 1, 'E': 0}`
        - Võit (`W`): 2 punkti
        - Kaotus (`L`): 1 punkt
        - Tehniline viga (`E`): 0 punkti
    - See süsteem on kasutusel selleks, et hoida kõik tiimid motiveeritud läbi kogu hooaja. Isegi kaotuse korral saab tiim ühe punkti, mis julgustab võistlema ja pingutama kuni lõpuni. Ainult tehnilised vead või täielik mitteosalemine tähendab null punkti.

Sinu ülesanne on:
1. Töödelda mõlemad failid automaatselt
2. Leida iga tiimi punktisumma käesolevast turniirist
3. Jagada punktid mõlema turniiri tulemuste põhjal
4. Luua uus fail, mis sisaldab koondpunktitabelit, kus on tiimi nimi koos vastavate punktidega

### Nõuded

#### Globaalne konstant

Loo globaalne konstant `ESPORDI_PUNKTID` faili algusesse ning kasuta seda seal kus vaja
```python
ESPORDI_PUNKTID = {'W': 2, 'L': 1, 'E': 0}
```

#### Abifunktsioonide loomine

1. Loo abifunktsioon `arvuta_turniiri_punktid(tiimi_mangude_tulemused)`:
    - **Parameeter:**
        - tiimi_mangude_tulemused (list[str]): List, mis sisaldab ühe tiimi/meeskonna mängude tulemusi kujul: `['W', 'L', 'E', 'W', 'L']`
    - **Tagastab:**
        - int: Turniiri punktisumma (kõigi mängude punktid kokku)
        - 0: Kui sisend puudub või vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli sisendi olemasolu
            - Kui sisend puudub kuva vastav veateade ja tagasta `0`
        - Arvuta punktid iga mängu kohta kasutades `ESPORDI_PUNKTID` sõnastikku:
            - `'W'` annab 2 punkti
            - `'L'` annab 1 punkti
            - `'E'` annab 0 punkti
        - Liida kõik mängude punktid kokku
        - Tagasta kogu turniiri  punktisumma

#### Põhifunktsioonide loomine

1. Loo funktsioon `analuusi_kaesolevat_turniiri(kaesoleva_turniiri_failinimi)`:
    - **Parameeter:**
        - kaesoleva_turniiri_failinimi (str): Faili nimi, mis sisaldab käesoleva turniiri tulemusi
    - **Tagastab:**
        - dict: {meeskonna_nimi: meeskonna_punktid} kõigi tiimide kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Rakenda sobivat veatöötlust faili leidmiseks ja lugemiseks:
            - Kasuta `try-except` plokki `FileNotFoundError` püüdmiseks
            - Vea korral kuva veateade ja tagasta tühi sõnastik
                - Faili lugemine:
        - Loe tulemused failist
            - Määra õige `encoding`
        - Faili lugemine ja töötlemine:
            - Loe faili rida rea haaval
            - Iga rea kohta:
                1. Eemalda igast reast tühikud
                2. Tühjad read jäta vahel
                3. Tükelda rida sobiva eraldajaga (vaata faili formaati)
                4. Eralda tiimi nimi ja mängude tulemused
                5. Kasuta `arvuta_turniiri_punktid(tiimi_mangude_tulemused)` funktsiooni, et arvutada tiimi punktid
                6. Salvesta tulemus sõnastikku
        - Tagasta tulemused sõnastikuna kujul:
            ```python
            {'FaZe Clan': 8, 'Team Liquid': 7, 'G2 Esports': 6, 'Cloud9': 10, ...}
            ```

2. Loo funktsioon `analuusi_eelmist_turniiri(eelmise_turniiri_failinimi)`:
    - **Parameeter:**
        - eelmise_turniiri_failinimi (str): Faili nimi, mis sisaldab eelmise turniiri tulemusi
    - **Tagastab:**
        - dict: {tiim: punktid} kõigi tiimide kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Rakenda sobivat veatöötlust faili leidmiseks ja lugemiseks:
            - Kasuta `try-except` plokki `FileNotFoundError` püüdmiseks
            - Vea korral kuva veateade ja tagasta tühi sõnastik
                - Faili lugemine:
        - Loe tulemused failist
            - Määra õige `encoding`
        - Faili lugemine ja töötlemine:
            - Loe faili rida rea haaval
            - Iga rea kohta:
                1. Eemalda igast reast tühikud
                2. Tühjad read jäta vahel
                3. Tükelda rida sobiva eraldajaga (vaata faili formaati)
                4. Eralda tiimi nimi ja punktid
                5. Konverteeri punktid `int` tüüpi:
                    - Juhul kui ei saa konverteerida, siis jäta rida vahele ning jätka järgmise reaga
                6. Salvesta tulemus sõnastikku
        - Tagasta tulemused sõnastikuna kujul:
            ```python
            {'FaZe Clan': 6, 'Team Liquid': 8, 'G2 Esports': 5, 'Cloud9': 7, ...}
            ```

3. Loo funktsioon `koosta_koondedetabel(eelmise_turniiri_punktid, kaesoleva_turniiri_punktid)`:
    - **Parameetrid:**
        - eelmise_turniiri_punktid (dict): Tiimi nimi ning selle eelmise turniiri punktid
        - kaesoleva_turniiri_punktid (dict): Tiimi nimi ning selle praeguse turniiri punktid
    - **Tagastab:**
        - dict: Koondpunktitabel sorteeritud kahanevalt kujul {nimi: punktid}
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastikud ei ole tühjad (kasuta `len` selleks):
            - Kui on, kuva veateade ja tagasta tühi sõnastik
        - Liida kokku tiimi eelmise turniiri ja käesoleva turniiri punktid
        - Arvesta kõiki tiime, ka neid, kes osalesid ainult ühes turniiris
        - Sorteeri sõnastik kogupunktide järgi kahanevalt
            - Kasutage selleks sellist lahendust, kus `koondtabel` on sõnastik, kus `key-value` paarideks on tiimi nimi ning punktid kokku kahe turniiri peale:
                ```python
                # Sorteeri sõnastik nii et kõrgeimad punktid oleksid ees
                sorteeritud_paarid = sorted(koondtabel.items(), key=lambda item: item[1], reverse=True)
                ```
            - See on valmis lahendus - kasuta seda ühe reana, lisa vaid õiged muutujanimed, kus `koondtabel` on sõnastik kujul: `{'FaZe Clan': 14, 'Team Liquid': 15, 'G2 Esports': 11, 'Cloud9': 16, ...}`
            - See koodijupp sorteerib sõnastiku nii, et esimesel kohal on kõige rohkem punkte saanud tiim
            - Peale sorteerimist näeb `sorteeritud_paarid` välja selline: `[('Cloud9', 16), ('Team Liquid', 15), ('FaZe Clan', 14), ...]`
            - Teisenda `sorteeritud_paarid` tagasi sõnastikuks
        - Tagasta lõplik sorteeritud sõnastiku edetabel, mis sisaldab tiimi nime koos vastavate punktidega

4. Loo funktsioon `salvesta_edetabel(koondpunktid, edetabeli_failinimi="koondedetabel.txt")`:
    - **Parameetrid:**
        - koondpunktid (dict): Koondpunktitabel, mis sisaldab tiimi nime koos vastavate punktidega
        - edetabeli_failinimi (str): Väljundfaili nimi (vaikeväärtus: `"koondedetabel.txt"`)
    - **Tagastab:**
        - Puudub
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastik `koondpunktid` ei ole tühi
            - Kui on, kuva vastav veateade ja välju funktsioonist
        - Rakenda sobivat veatöötlust faili kirjutamiseks:
            - Kasuta `try-except` plokki
            - Vea tekkimisel kuva veateade ja välju funktsioonist
        - Loo uus fail, kasutades parameetrit `edetabeli_failinimi`
        - Kirjuta tulemused faili kujul:
            ```python
            1. koht: {tiim} – {punktid}
            2. koht: {tiim} – {punktid}
            ...
            ```
        - Rakenda sobivat veatöötlust vea püüdmiseks
            - Vea tekkimisel kuva veateade ja välju funktsioonist
        - Kui tulemused on edukalt faili kirjutatud, kuva teade faili eduka salvestamise kohta

5. Loo funktsioon `main()`:
    - Organiseeri kõigi funktsioonide väljakutsumine, kus sa kõigepealt:
        1. Loed ja analüüsid mõlema turniiri tulemusi
        2. Koosta koondtabel
        3. Salvesta tulemused faili

6. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Programmi väljund
```python
Tulemused salvestatud faili 'koondedetabel.txt'
```

### Salvestatud faili sisu
```
1. koht: Cloud9 – 17
2. koht: Team Liquid – 16
3. koht: FaZe Clan – 15
4. koht: Fnatic – 15
5. koht: T1 – 14
6. koht: G2 Esports – 13
7. koht: TSM – 12
8. koht: NRG Esports – 11
9. koht: Evil Geniuses – 11
10. koht: 100 Thieves – 10
11. koht: Team Vitality – 9
12. koht: Gen.G – 7
```

---
