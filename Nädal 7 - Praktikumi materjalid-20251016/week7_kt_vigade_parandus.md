
# Week 7 – Kontrolltöö vigade parandus

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week7`
2. Sinna kausta loo kõik selle nädala praktikumi ülesanded
3. Lae Moodlist alla kõik vajalikud `.txt` failid, need leiate Moodlist: `Nädal 7` -> `Nädal 7 - Praktikumi materjalid`
4. Sinna kausta pane:
    1. Kõik allalaetud `.txt` failid
    2. Sinu lood kood
    3. Ülesande käigus loodud `.txt` fail
5. Peale lõpetamist lae kõik vajalikud failid GitLabi

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
6. Lisa `GitLabi` ka kõik `.txt` failid

## PS! Alusta algusest, loo üks funktsoon ära, testi seda (kutsu `main()` funktsioonis see välja) ning liigu edasi.

---

## Ülesanne 1: F1 kiiruskatsete tulemuste analüüs ja punktiarvestus
**Failinimi:** `f1_tulemused.py`

### Eesmärk
Sa töötad Formula 1 võistlustiimis andmeanalüütikuna. Sul on kaks faili kiiruskatsete tulemustega ning sa pead:
1. Töötlema ja filtreerima käesoleva sõidu tulemusi
2. Analüüsima eelmise sõidu tulemusi
3. Jagama F1 punktisüsteemi järgi punktid mõlema sõidu eest
4. Koostama lõpliku edetabeli

### Ettevalmistus
1. Tutvu failiga `eelmised_tulemused.txt` sisuga:
    - Fail `eelmised_tulemused.txt` sisaldab juba töödelduid andmeid, kus igas reas on `nimi;aeg`
    - Iga sõitja nime taga on tema kiireim aeg
2. Tutvu failiga `kaesolevad_tulemused.txt` sisuga:
    - Nende andmetega pole andmetöötlust tehtud. On vaja eemaldada vigased ajad ning leida iga sõitja kiireim aeg
    - Fail `kaesolevad_tulemused.txt` sisaldab andmeid, kus igas reas on `nimi; t1; t2; t3; t4`
    - Fail sisaldab ka vigaseid andmeid -> `999`
3. Tutvua F1 punktisüsteemiga:
    - Punktisüsteem on selline: `[25, 18, 15, 12, 10, 8, 6, 4, 2, 1]`
    - Esimesed 10 kohta saavad punktid:
        - Sõitja, kelle aeg on kiireim saab 25 punkti
        - Teine koht saab 18 punkti
        - Kolmas koht saab 15 punkti
        - Kümnes koht saab 1 punkti
    - Koht 11 ja edasi saavad 0 punkti

Sinu ülesanne on:
1. Töödelda mõlemad failid automaatselt
2. Leida iga sõitja parim aeg käesolevast sõidust
3. Jagada punktid mõlema sõidu tulemuste põhjal
4. Luua uus fail, mis sisaldab koondpunktitabelit, kus on sõitja nimi koos vastavate punktidega


### Nõuded

#### Globaalne konstant

Loo globaalne konstant `F1_PUNKTID` faili algusesse ning kasuta seda seal kus vaja
```python
F1_PUNKTID = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
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

2. Loo funktsioon `filtreeri_kehtivad_ajad(ajad, vigane_vaartus)`:
    - **Parameetrid:**
        - ajad (list[str]): List, mis sisaldab kõiki sõitja tulemusi
        - vigane_vaartus (int): Vigane väärtus, mida eemaldada/mitte arvesse võtta
    - **Tagastab:**
        - list[float]: List kehtivate aegadega (float kujul)
        - []: Tühi list kui kõik ajad vigased või vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli sisendi olemasolu
            - Kui sisend puudub kuva vastav veateade ja tagasta tühi list
        - Filtreeri välja vigased väärtused
        - Konverteeri kehtivad ajad `float` tüüpi
            - Vea korral ignoreeri ning jätka andmete töötlemist
        - Tagasta list, mis sisaldab sõitja kehtivaid aegu

3. Loo funktsioon `leia_parim_aeg(kehtivad_ajad)`:
    - **Parameeter:**
        - kehtivad_ajad (list[float]): List kehtivate aegadega
    - **Tagastab:**
        - float: Parim (väikseim) aeg
        - None: Kui list on tühi
    - **Ülesanne:**
        - Vea kontroll: Kontrolli sisendi olemasolu
            - Kui sisend puudub kuva vastav veateade ning tagasta `None`
        - Leia sõitja kiireim/parim aeg listist
        - Tagasta sõitja kiireim/parim aeg

#### Põhifunktsioonide loomine

1. Loo funktsioon `analuusi_praegusi_tulemusi(failnimi):`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, mis sisaldab käesoleva sõidu tulemusi
    - **Tagastab:**
        - dict: {nimi: parim_aeg} kõigi sõitjate kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Kasuta loodud abifunktsiooni `loe_tulemused(failinimi)`, et tulemused failist sisse lugeda
            - Kontrolli ega tulemuste list tühi pole
                - Kui on, siis kuva teade ja tagasta tühi sõnastik
        - Töötle iga sõitja andmeid eraldi:
            - Eralda nimed ning ajad:
                - Tükelda rida sobiva eraldajaga (vaata faili formaati)
            - Kasuta `filtreeri_kehtivad_ajad(ajad, vigane_vaartus)` funktsiooni, et filtreerida välja kehtivad aja selle sõitja jaoks
            - Kasuta `leia_parim_aeg(kehtivad_ajad)` funktsiooni, et leida sõitja filtreeritud tulemustest tema kiireim tulemus
        - Tagasta tulemused sõnastikuna kujul:
            ```python
            {'Hamilton': 70.8, 'Leclerc': 71.8, ..., 'Sargeant': 81.7, 'Schumacher': 81.9}
            ```

2. Loo funktsioon `analuusi_eelmised_tulemused(failnimi):`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, mis sisaldab eelmise sõidu tulemusi
    - **Tagastab:**
        - dict: {nimi: parim_aeg} kõigi sõitjate kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Kasuta loodud abifunktsiooni `loe_tulemused(failinimi)`, et tulemused failist sisse lugeda
            - Kontrolli ega tulemuste list tühi pole
                - Kui on, siis kuva teade ja tagasta tühi sõnastik
        - Töötle lihtsamat andmeformaati (nimi;aeg)
            - Eralda nimed ja aeg
            - Teisenda aeg `float` tüübiks
        - Tagasta tulemused sõnastikuna kujul:
            ```python
            {'Hamilton': 72.1, 'Verstappen': 71.3, ..., 'Sargeant': 80.6, 'Schumacher': 81.2}
            ```

3. Loo funktsioon `jaga_punktid(soitjate_ajad)`:
    - **Parameeter:**
        - soitjate_ajad (dict): Sõnastik, mis sisaldab sõitjate nime ja tema parimat aega
    - **Tagastab:**
        - dict: {nimi: punktid} kõigi sõitjate kohta
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastik ei ole tühi
            - Kui on, kuva veateade ja tagasta tühi sõnastik
        - Sorteeri sõnastik nii, et kiiremad ajad oleksid ees
            - Kasutage selleks sellist lahendust:
                ```python
                # Sorteeri sõnastik nii et kiireimaid ajad oleksid ees
                sorteeritud_tulemused = sorted(soitjate_ajad.items(), key=lambda item: item[1])
                ```
                - See on valmis lahendus - kasuta seda ühe reana, lisa vaid õiged muutujanimed, kus:
                    - `soitjate_ajad` on sõnastik kujul: `{'Hamilton': 70.8, 'Leclerc': 71.8, 'Verstappen': 71.9, ....., 'Schumacher': 81.9}`
            - See koodijupp muudab sõnastiku `soitjate_ajad` sorteeritud listiks tuple'idega kujul `[(nimi, aeg)]`
            - Pärast sorteerimist on esimesel kohal kiireim sõitja, teisel kohal teine kiireim aeg jne:
                - Peale sorteerimist näeb `sorteeritud_tulemused` välja selline: `[('Verstappen', 71.2), ('Hamilton', 71.8), ('Leclerc', 73.5), ..., ('Schumacher', 81.9)]`
        - Jaga sõitjatele vastavad punktid F1 süsteemi järgi
            - Kasuta selleks globaalset muutujat `F1_PUNKTID`
        - Tagasta punktitabel

4. Loo funktsioon `koosta_koondedetabel(eelmised_punktid, praegused_punktid)`:
    - **Parameetrid:**
        - eelmised_punktid (dict): Sõitja nimi ning tema eelmise sõidu eest saadud punktid
        - praegused_punktid (dict): Sõitja nimi ning tema praeguse sõidu eest saadud punktid
    - **Tagastab:**
        - dict: Koonpunktitabel sorteeritud kahanevalt kujul {nimi: punktid}
        - {}: Tühi sõnastik vea korral
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastikud ei ole tühjad (kasuta `len` selleks):
            - Kui on, kuva veateade ja tagasta tühi sõnastik
        - Liida kokku mõlema sõidu punktid
        - Arvesta kõiki sõitjaid, ka neid, kes osalesid ainult ühes sõidus
        - Sorteeri sõnastik kogupunktide järgi kahanevalt
            - Kasutage selleks sellist lahendust, kus `soitate_punktid` on sõnastik, kus `key-value` paarideks on sõitja nimi ning punktid kokku kahe sõidu peale kokku:
                ```python
                # Sorteeri sõnastik nii et kõrgeimad punktid oleksid ees
                sorteeritud_tulemused = sorted(soitate_punktid.items(), key=lambda item: item[1], reverse=True)
                ```
            - See on valmis lahendus - kasuta seda ühe reana, lisa vaid õiged muutujanimed, kus `soitate_punktid` on sõnastik kujul: `{'Verstappen': 40, 'Hamilton': 43, 'Leclerc': 33, ..., 'Schumacher': 0}`
            - See koodijupp sorteerib sõnastiku nii, et esimesel kohal on kõige rohkem punkte saanud sõitja
            - Peale sorteerimist näeb `sorteeritud_tulemused` välja selline: `[('Verstappen', 43), ('Hamilton', 43), ('Leclerc', 30)...]`
            - Teisenda `sorteeritud_paarid` tagasi sõnastikuks
        - Tagasta lõplik sorteeritud sõitjate sõnastiku edetabel, mis sisaldab sõitja nime koos vastavate punktidega

5. Loo funktsioon `salvesta_edetabel(koondpunktid, failinimi="f1_koondedetabel.txt")`:
    - **Parameetrid:**
        - koondpunktid (dict): Koondpunktitabel, mis sisaldab sõitja nime koos vastavate punktidega
        - failinimi (str): Väljundfaili nimi (vaikeväärtus: `"f1_koondedetabel.txt"`)
    - **Tagastab:** Puudub
    - **Ülesanne:**
        - Vea kontroll: Kontrolli, et sõnastik `koondpunktid` ei ole tühi
            - Kui on, kuva vastav veateade ja välju funktsioonist
        - Loo uus fail, kasutades parameetrit `failinimi`
        - Kirjuta tulemused faili kujul:
            ```python
             1. koht: {nimi} – {punktid}
             2. koht: {nimi} – {punktid}
             ...
             11. koht: {nimi} – {punktid}
             ```
        - Rakenda sobivat veatöötlust vea püüdmiseks
            - Vea tekkimisel kuva veateade ja välju funktsioonist
        - Kui tulemused on edukalt faili kirjutatud, kuva teade faili eduka salvestamise kohta

6. Loo funktsioon `main()`:
    - Organiseeri kõigi funktsioonide väljakutsumine, kus sa kõigepealt:
        1. Loed ja analüüsid mõlema sõidu tulemused
        2. Konverteeri ajad punktideks
        3. Koosta koondtabel
        4. Salvesta tulemused faili

7. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Programmi väljund
```python
Tulemused salvestatud faili 'f1_koondedetabel.txt'
```

### Salvestatud faili sisu
```
1. koht: Hamilton – 43
2. koht: Verstappen – 40
3. koht: Leclerc – 33
4. koht: Räikkönen – 22
5. koht: Russell – 22
6. koht: Sainz – 16
7. koht: Norris – 12
8. koht: Albon – 6
9. koht: Gasly – 6
10. koht: Ocon – 2
11. koht: Schumacher – 0
```

---

## Ülesanne 2: Eesti-Läti liiga korvpallitulemuste analüüs ja punktiarvestus
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
            - Kasutage selleks sellist lahendust, kus `meeskonna_punktid` on sõnastik, kus `key-value` paarideks on meeskonna nimi ning punktid kokku kahe vooru peale
            - See koodijupp sorteerib sõnastiku nii, et esimesel kohal on kõige rohkem punkte saanud sõitja:
                ```python
                # Sorteeri sõnastik nii et kõrgeimad punktid oleksid ees
                sorteeritud_meeskondade_tulemused = sorted(meeskonna_punktid.items(), key=lambda item: item[1], reverse=True)
                ```
            - See on valmis lahendus - kasuta seda ühe reana, lisa vaid õiged muutujanimed, kus `meeskonna_punktid` on sõnastik kujul: `{'Kalev/Cramo': 11, 'Tartu Ülikool': 10, 'Valmiera Glass': 8, ..., 'Keila KK': 5}`
            - Peale sorteerimist näeb `sorteeritud_meeskondade_tulemused` välja selline: `[('Rigas Zelli', 13), ('Kalev/Cramo', 11), ..., ('Keila KK', 5)]`
            - Teisenda `sorteeritud_meeskondade_tulemused` tagasi sõnastikuks
        - Tagasta lõplik sorteeritud sõnastiku edetabel, mis sisaldab meeskonna koos mõlema vooru punktidega kujul: `{'Rigas Zelli': 13, 'Kalev/Cramo': 11, 'Tartu Ülikool': 10, ..., 'Keila KK': 5}`

4. Loo funktsioon `salvesta_edetabel(koondpunktid, edetabeli_failinimi="korvpalli_koondedetabel.txt")`:
    - **Parameetrid:**
        - koondpunktid (dict): Koondpunktitabel, mis sisaldab meeskonna nime koos vastavate punktidega
        - edetabeli_failinimi (str): Väljundfaili nimi (vaikeväärtus: `"korvpalli_koondedetabel.txt"`)
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
Tulemused salvestatud faili 'korvpalli_koondedetabel.txt'
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
