# Week 6 – Kontrolltöö 1, praktiline osa 2

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week6_kt2`
2. Sinna kausta loo kõik selle nädala praktikumi ülesanded
3. Lae Moodlist alla kõik vajalikud `.txt` failid, need leiate Moodlist: `Nädal 6 - Kontrolltöö 1` -> `Kontrolltöö 1, grupp 2 - Praktiline osa, failid`
4. Sinna kausta pane:
    1. Kõik allalaetud `.txt` failid
    2. Sinu lood kood
    3. Ülesande käigus loodud `.txt` fail
5. Peale lõpetamist lae kõik vajalikud failid GitLabi

**PS! Enda koode saab hakata testima alates `9:30-10:00`**

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

## PS! Alusta algusest, loo üks funktsoon ära, testi seda (kutsu `main()` funktsioonis see välja) ning liigu edasi.

## Ülesanne 1: Eesti-Läti liiga korvpallitulemuste analüüs ja punktiarvestus
**Failinimi:** `korvpalli_tulemused.py`

### Eesmärk
Sa töötad korvpalli võistlustiimis andmeanalüütikuna. Sul on kaks faili turniirimängude tulemustega ning sa pead:
1. Töötlema ja filtreerima käesoleva vooru tulemusi
2. Analüüsima eelmise eelmise vooru tulemusi
3. Jagama punktid korvpalli süsteemi järgi mõlema vooru eest
4. Koostama lõpliku edetabeli

### Ettevalmistus
1. Tutvu failiga `eelmine_voor.txt` sisuga:
    - Fail `eelmine_voor.txt` sisaldab juba töödelduid andmeid, kus igas reas on `meeskond;punktid`
    - Iga meeskonna nime taga on selle vooru punktid
2. Tutvu failiga `kaesolev_voor.txt` sisuga:
    - Nende andmetega pole andmetöötlust tehtud. On vaja eemaldada vigased andmed (X märgid) ning arvutada iga meeskonna punktid
    - Fail `kaesolev_voor.txt` sisaldab andmeid, kus igas reas on `meeskond;mang1;mang2;mang3;mang4`
    - Mängude tulemused on kujul:
        - `W`, mis tähistab võitu
        - `L`, mis tähistab kaotust
        - `X`, mis tähistab kaotust, et mäng ei toimunud
    - Fail sisaldab ka vigaseid andmeid -> `X`
3. Tutvu korvpalli punktisüsteemiga:
    - Punktisüsteem on selline: `{'W': 2, 'L': 1,'X': 0}`
        - Võit (`W`)`: 2 punkti
        - Kaotus (`L`): 1 punkt
        - Mäng jäi ära (`X`): 0 punkti
    - See süsteem on kasutusel selleks, et hoida kõik meeskonnad motiveeritud läbi kogu hooaja - isegi kaotuse korral saab meeskond ühe punkti, mis julgustab võistlema ja pingutama kuni lõpuni. Ainult täielik loobumine või mitteosalemine tähendab null punkti.

Sinu ülesanne on:
1. Töödelda mõlemad failid automaatselt
2. Leida iga meeskonna punktisumma käesolevast voorust
3. Jagada punktid mõlema vooru tulemuste põhjal
4. Luua uus fail, mis sisaldab koondpunktitabelit, kus on meeskonna nimi koos vastavate punktidega

### Nõuded

#### Globaalne konstant

Loo globaalne konstant `KORVPALLI_PUNKTID` faili algusesse ning kasuta seda seal kus vaja
```python
KORVPALLI_PUNKTID = {'W': 2, 'L': 1, 'X': 0}
```

#### Abifunktsioonide loomine

1. Loo funktsioon `loe_tulemused(failinimi)`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, mida soovid lugeda
    - **Tagastab:**
        - List[str]: List kõigi mittetühjade ridadega failist
        - []: Tühi list vea korral
    - **Ülesanne:**
        - Rakenda sobivat veatöötlust faili leidmiseks:
            - Vea korral kuva veateade ja tagasta tühi list
        - Faili lugemine:
            - Loe tulemused failist
            - Määra õige `encoding`
        - Töötle igat rida:
            - Eemalda igast reast tühikud
            - Read, mis pole tühjad lisa listi
        - Tagastus: List failisisuga

2. Loo funktsioon `arvuta_vooru_punktid(tulemused)`:
    - **Parameetrid:**
        - mangude_tulemused (list[str]): List, mis sisaldab kõiki meeskonna mängude tulemusi kujul: `['W', 'L', 'X']`
    - **Tagastab:**
        - int: Vooru punktisumma (kõigi mängude punktid kokku)
        - None: Kui sisend puudub või vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli sisendi olemasolu
            - Kui sisend puudub kuva vastav veateade ja tagasta `None`
        - Arvuta punktid iga mängu kohta kasutades `KORVPALLI_PUNKTID` sõnastikku:
            - `'W'` annab 2 punkti
            - `'L'` annab 1 punkti
            - `'X'` annab 0 punkti
        - Liida kõik mängude punktid kokku
        - Tagasta vooru kogu punktisumma

#### Põhifunktsioonide loomine

1. Loo funktsioon `analuusi_kaesolevat_vooru(kaesoleva_vooru_failinimi):`:
    - **Parameeter:**
        - kaesoleva_vooru_failinimi (str): Faili nimi, mis sisaldab käesoleva vooru tulemusi
    - **Tagastab:**
        - dict: {meeskond: punktid} kõigi meeskondade kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Kasuta loodud abifunktsiooni `loe_tulemused(failinimi)` faili lugemiseks
        - Töötle iga meeskonna andmeid eraldi:
            - Eralda meeskonnad ning tulemused:
                - Tükelda rida sobiva eraldajaga (vaata faili formaati)
            - Kasuta` arvuta_vooru_punktid(mangude_tulemused)` funktsiooni, et arvutada vooru punktisumma
        - Tagasta tulemused sõnastikuna kujul: `{'Kalev/Cramo': 7, 'Tartu Ülikool': 6, 'Valmiera Glass': 6, ..., 'Keila Coolbet': 5, 'Keila KK': 5}`

2. Loo funktsioon `analuusi_eelmist_vooru(eelmise_vooru_failinimi):`:
    - **Parameeter:**
        - eelmise_vooru_failinimi (str): Faili nimi, mis sisaldab eelmise vooru tulemusi
    - **Tagastab:**
        - dict: {meeskond: punktid} kõigi meeskondade kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Kasuta loodud abifunktsiooni `loe_tulemused(failinimi)` faili lugemiseks
        - Töötle lihtsamat andmeformaati (meeskond;punktid)
            - Eralda meeskonnad ja punktid
            - Kasuta `try-except` plokki:
                - Konverteeri punktid int tüüpi
                - Kui ei saa konverteerida, jäta vahele ja jätka
        - Tagasta tulemused sõnastikuna kujul: `{'Kalev/Cramo': 4, 'Tartu Ülikool': 4, 'Valmiera Glass': 2, ..., 'Keila Coolbet': 2, 'Keila KK': 0}`

3. Loo funktsioon `koosta_koondedetabel(eelmise_vooru_punktid, kaesoleva_vooru_punktid)`:
    - **Parameetrid:**
        - eelmise_vooru_punktid (dict): Meeskonna nimi ning selle eelmise vooru punktid
        - kaesoleva_vooru_punktid (dict): Meeskonna nimi ning selle praeguse vooru punktid
    - **Tagastab:**
        - dict: Koonpunktitabel sorteeritud kahanevalt kujul {nimi: punktid}
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastikud ei ole tühjad:
            - Kui on, kuva veateade ja tagasta tühi sõnastik
        - Liida kokku meeskonna eelmise vooru ja käesoleva vooru punktid
        - Sorteeri sõnastik kogupunktide järgi kahanevalt
            - Kasutage selleks sellist lahendust, kus `koondtabel` on sõnastik, kus `key-value` paarideks on meeskonna nimi ning punktid kokku kahe vooru peale
            - See koodijupp sorteerib sõnastiku nii, et esimesel kohal on kõige rohkem punkte saanud sõitja:
                ```python
                # Sorteeri sõnastik nii et kõrgeimad punktid oleksid ees
                sorteeritud_tulemused = sorted(koondtabel.items(), key=lambda item: item[1], reverse=True)
                ```
            - See on valmis lahendus - kasuta seda ühe reana, lisa vaid õiged muutujanimed, kus `koondtabel` on sõnastik kujul: `{'Kalev/Cramo': 11, 'Tartu Ülikool': 10, 'Valmiera Glass': 8, ..., 'Keila KK': 5}`
            - Peale sorteerimist näeb `sorteeritud_paarid` välja selline: `[('Rigas Zelli', 13), ('Kalev/Cramo', 11), ..., ('Keila KK', 5)]`
            - Teisenda `sorteeritud_paarid` tagasi sõnastikuks
        - Tagasta lõplik sorteeritud sõnastiku edetabel, mis sisaldab meeskonna koos mõlema vooru punktidega kujul: `{'Rigas Zelli': 13, 'Kalev/Cramo': 11, 'Tartu Ülikool': 10, ..., 'Keila KK': 5}`

4. Loo funktsioon `salvesta_edetabel(koondpunktid, edetabeli_failinimi="koondedetabel.txt")`:
    - **Parameetrid:**
        - koondpunktid (dict): Koondpunktitabel, mis sisaldab meeskonna nime koos vastavate punktidega
        - edetabeli_failinimi (str): Väljundfaili nimi (vaikeväärtus: `"koondedetabel.txt"`)
    - **Tagastab:**
        - Puudub
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastik `koondpunktid` ei ole tühi
            - Kui on, kuva vastav veateade ja välju funktsioonist
        - Loo uus fail, kasutades parameetrit `edetabeli_failinimi`
        - Kirjuta tulemused faili kujul:
            ```python
            1. koht: {meeskond} – {punktid}
            2. koht: {meeskond} – {punktid}
            ...
            ```
        - Rakenda sobivat veatöötlust vea püüdmiseks
            - Vea tekkimisel kuva veateade ja välju funktsioonist
        - Kui tulemused on edukalt faili kirjutatud, kuva teade faili eduka salvestamise kohta

5. Loo funktsioon `main()`:
    - Organiseeri kõigi funktsioonide väljakutsumine, kus sa kõigepealt:
        1. Loed ja analüüsid mõlema vooru tulemusi
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
1. koht: Rigas Zelli - 13
2. koht: Kalev/Cramo - 11
3. koht: Tartu Ülikool - 10
4. koht: VEF Riga - 9
5. koht: Valmiera Glass - 8
6. koht: TalTech/Alexela - 8
7. koht: Transcom Pärnu - 8
8. koht: BK Ogre - 8
9. koht: Keila Coolbet - 7
10. koht: Viimsi - 6
11. koht: Latvia University - 5
12. koht: Keila KK - 5
```

---
