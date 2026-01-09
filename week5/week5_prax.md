# Week 5 – Andmestruktuurid (listid ja sõnastikud)

## Eesmärk
1. Selle praktikumi eesmärk on õppida kasutama andmestruktuure
2. Listide loomine ja nende opereerimine
3. List listis
4. Võti-väärtus paarid ehk sõnastik ja selle opereerimine

---

## Ülesanded

### Seadistamine

1. Lae Moodlist alla kõik vajalikud `.txt` failid -> need on iga vastava nädala `Praktikumi materjalid` all
2. Loo kaust/directory nimega `week5`
3. Sinna kausta pane kõik vajaminevad `.txt` failid ning salvesta sinna ka kõik selle nädala praktikumi ülesanded
4. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
6. Lisa `GitLabi` ka kõik `.txt` failid

---

## Ülesanne 1 – Nimekirja haldamine
**Failinimi:** `andmete_lugeja.py`

### Eesmärk
Eelmisel nädalal märkasite, et kopeerite palju sarnast koodi erinevates ülesannetes - eriti faili lugemise osa. See on vastuolus DRY (Don't Repeat Yourself) printsiibiga, millest lugesite lisalugemises.
Selle ülesande eesmärk on luua korduvkasutatav moodul, mida saate importida ja kasutada kõigis järgmistes ülesannetes. See säästab aega, vähendab vigu ja teeb koodi palju puhtamaks!

### Nõuded
1. Loo funktsioon `loe_tekst_failist(failinimi)`:
    - **Parameetrid:** failinimi (str): Faili nimi, mida soovid lugeda
    - **Tagastab:**
        - str: Kogu faili sisu stringina (ilma lõpu tühikuteta)
        - None: Kui faili ei leitud või tekkis viga
    - **Kirjeldus:**
        - Faili lugemine:
            - Määra õige `encoding`
            - Loe kogu faili sisu korraga
            - Eemalda faili lõpust tühikud
            - Tagasta kogu faili sisu stringina
        - Veakäsitlus:
            - Kasuta `try-except` blokki  `FileNotFoundError` ja üldise `Exception` püüdmiseks
            - `FileNotFoundError` korral veateade
            - `Exception` korral veateade
            - Tagasta `None` vea korral

2. Lisa testimise osa` if __name__ == "__main__":` blokki:
    - Kutsu välja funktsioon `loe_tekst_failist(failinimi)`
        - Kasuta selleks faili `klassinimed.txt`
    - Salvesta tulemus muutujasse ja kontrolli, kas loodud funktsioon töötab
    - Prindi välja tulemus, et näha kas funktsioon töötab

### Miks see on kasulik?
1. `if __name__ == "__main__":` blokk käivitub ainult siis, kui käivitad selle faili otse
2. Kui impordid selle mooduli teises programmis, siis see testimise osa ei käivitu automaatselt
3. Nii saad kohe testida, kas funktsioon töötab, kuid hiljem ei sega see importimist
4. Järgmistes ülesannetes selle asemel, et kirjutada iga kord samasugune funktsioon saate te importida seda funktsiooni

### Kuidas seda järgmistes ülesannetes kasutada?
**Eeldus:** Fail `andmete_lugega.py` asub samas kaustas, kus on ka see fail, mis seda impordib ning meil see ka nii on.

**Import (faili alguses)**
```python
from andmete_lugeja import loe_tekst_failist
```

**Kasutamine:**
```python
# Kutsume funktsiooni välja samamoodi nagu tavalist funktsiooni
faili_sisu = loe_tekst_failist(failinimi="mingi_fail.txt")

# Kuna me teame, et funktsioon tagastab kas str või None, 
# siis kasutame tagastatud väärtust edasi:
if faili_sisu is not None:
    for rida in read:
        print(rida)
else:
    print("Faili lugemisel tekkis viga")
```

---

## Ülesanne 2 – Nimekirja haldamine
**Failinimi:** `klassi_nimekiri.py`

### Eesmärk
Kirjuta programm, mis haldab klassi laste nimekirja. Programm peab võimaldama nimesid vaadata, lisada, eemaldada ja teha muid toiminguid menüü kaudu.

### Ettevalmistus
1. Veendu, et `andmete_lugeja.py` on loodud ja toimib
2. Tutvu faili `klassinimed.txt` sisuga

### Nõuded
1. Loo funktsioon `lae_nimed_failist(failinimi)`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, kust nimesid lugeda
    - **Tagastab:**
        - list[str]: Nimede list
        - []: Tühi list vea korral
    - **Kirjeldus:**
        - Import: Impordi failist `andmete_lugeja.py` funktsioon `loe_tekst_failist(failinimi)`
        - Faili lugemine: Kasuta importitud funktsiooni faili sisu lugemiseks
        - Vea kontroll: Kui loetud faili sisu on None, tagasta tühi list ja väljasta veateade
        - Teksti töötlemine:
            - Jaga tekst ridadeks
            - Eemalda igast reast tühikud
            - Jäta välja tühjad read
        - Tagastus: Tagasta nimede list

2. Loo funktsioon `kuva_menuu()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - None
    - **Kirjeldus:** Prindib programmi peamenüü valikud, kujul:
        ```python
        1. Näita kõiki nimesid
        2. Lisa nimi
        3. Eemalda nimi
        4. Näita esimesed n nime
        5. Vali suvaline õpilane
        6. Sulge programm
        ```
3. Loo funktsioon `kusi_kasutaja_valik()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - `int`: Kehtiv menüüvaliku number, vahemikus 1-6
    - **Kirjeldus:**
        - Kasutab tsüklit, kasutajalt sisend saamiseks
        - Teisenda kasutaja sisend täisarvuks
        - Kasuta `try-except` blokki `ValueError` püüdmiseks
            - Vea korral kuva veateade ja küsi uuesti
        - Kontrolli, et sisestatud number on vahemikus 1-6
            - Kui pole, kuva veateade ja küsi uuesti
        - Korda küsimist, kuni saad kehtiva sisendi
        - Tagasta menüüvaliku numbri

4. Loo funktsioon `kuva_koik_nimed(nimed)`:
    - **Parameeter:**
        - `nimed (list[str])`: Nimede list (funktsioon lae_nimed_failist(failinimi) tagastab seda)
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Kontrolli ega parameeter pole tühi:
            - Kui on tühi, väljasta veateade ja välju funktsioonist
        - Kuvab kõik õpilaste nimed nummerdatud listina:
            - Prindi iga nime koos järjekorranumbriga, kujul: `f"{i}. {nimi}"`

5. Loo funktsioon `lisa_nimi(nimed)`, mis lisab uue nime nimekirja ja kuvab uuendatud nimekirja:
    - **Parameeter:**
        - `nimed (list[str])`: Nimede list
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Küsib kasutajalt uut nime, kujul: `"Sisesta uus nimi: "`
        - Kontrollib, et kasutaja poolt sisestatud nimi pole tühi string:
            - Kui on tühi, väljasta veateade ja välju funktsioonist
        - Võrdleb uut nime olemasolevate nimedega (võrdlus peab olema case-insensitive):
            - Teisenda nii uus nimi kui ka olemasolevad nimed väiketähtedeks võrdlemiseks
            - Kui nimi on juba olemas (näiteks "mari" == "Mari"), väljasta veateade ja välju funktsioonist
            - Kui nimi pole olemas, lisa originaalnimi (säilitades suurtähed) listi lõppu
            - Kuvab kinnitava sõnumi, kujul: `"Nimi '{uus_nimi}' lisati nimekirja!"`
        - Kuvab uuendatud nimekirja kasutades funktsiooni `kuva_koik_nimed(nimed)`

6. Loo funktsioon `eemalda_nimi(nimed)`, mis eemaldab kasutaja valitud nime nimekirjast:
    - **Parameeter:**
        - - `nimed (list[str])`: Nimede list
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Kontrollib, kas nimekiri pole tühi
            - Kui on tühi, väljasta veateade ja välju funktsioonist
        - Kuvab praegused nimed nummerdatud kujul: `"{i}. {nimi}"`
        - Küsib kasutajalt eemaldatava nime järjekorranumbrit kujul: `"Sisesta eemaldatava õpilase number: "`
        - Kasutab `try-except` blokke `ValueError` ja `IndexError` jaoks:
            - Vea korral kuva veateade
        - Kontrollib numbri kehtivust (1 kuni nimekirja pikkus)
            - Kui number pole kehtiv, kuva veateade
        - Eemaldab valitud nime nimede listist
            - Kuvab kinnitava sõnumi kujul: `"Nimi '{eemaldatud_nimi}' eemaldati nimekirjast!"`
        - Kuvab uuendatud nimekirja kasutades funktsiooni `kuva_koik_nimed(nimed)` või tühja nimekirja puhul teate

7. Loo funktsioon `naita_esimesed_n(nimed)`, mis kuvab kasutaja määratud arvu esimesi nimesid:
    - **Parameeter:**
        - `nimed (list[str])`: Nimede list
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Kontrollib, kas nimekiri pole tühi
            - Kui on tühi, väljasta veateade ja välju funktsioonist
        - Küsib kasutajalt, mitu nime näha soovitakse -> `"Mitu nime soovid näha: "`
        - Kasutab `try-except` blokki `ValueError` jaoks
            - Vea korral kuva veateade
        - Kontrollib, et number on positiivne (suurem kui 0)
            - Kui pole, kuva veateade ja välju funktsioonist
        - Kui `n` (nimede arv, mida kasutaja soovib näha) on suurem kui nimekirja pikkus, kasuta nimekirja pikkust
        - Kuvab esimesed n nime nummerdatud kujul: `"{i}. {nimi}"`

8. Loo funktsioon `vali_suvaline_opilane(nimed)`, mis valib ja kuvab juhusliku õpilase nimekirjast
    - **Parameeter:**
        - `nimed (list[str])`: Nimede list
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Impordi `random` moodul
        - Kontrollib, kas nimekiri pole tühi
            - Kui on tühi, väljasta veateade ja välju funktsioonist
        - Kasutab `random.choice(nimed)` juhusliku valiku jaoks
        - Kuvab valitud nime: `Suvaline valik: {valitud_opilane}`

9. Loo funktsioon `main()`, mis on programmi peamine funktsioon
    - Kutsu välja `lae_nimed_failist(failinimi)`
    - Jooksutab lõputut tsükli
    - Iga iteratsioon:
        1. Kuvab menüüd (funktsioon `kuva_menuu()`)
        2. Küsib kasutaja valikut (funktsioon `kusi_kasutaja_valik()`)
        3. Suuna kasutaja valiku põhjal õigesse funktsiooni:
            - 1 → Funktsioon `kuva_koik_nimed(nimed)`
            - 2 → Funktsioon `lisa_nimi(nimed)`
            - 3 → Funktsioon `eemalda_nimi(nimed)`
            - 4 → Funktsioon `naita_esimesed_n(nimed)`
            - 5 → Funktsioon `vali_suvaline_opilane(nimed)`
            - 6 → Väljub tsüklist kui kasutaja valib 6
    - Programmi lõpetamisel:
        - Kuva tekst kujul: `Lõplik nimekiri oli:`
        - Kva lõplik nimekiri, kasutades funktsiooni `kuva_koik_nimed(nimed)`

10. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

### Programmi kasutus ja väljund:**
```python
Laaditud 12 nime failist 'klassinimed.txt'
Alustan programmi!

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 1
1. Mari
2. Kati
3. Jüri
4. Toomas
5. Anneli
6. Karl
7. Liis
8. Mart
9. Sandra
10. Kristjan
11. Helen
12. Rasmus

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 2
Sisesta uus nimi: Gregor
Nimi 'Gregor' lisati nimekirja!
1. Mari
2. Kati
3. Jüri
4. Toomas
5. Anneli
6. Karl
7. Liis
8. Mart
9. Sandra
10. Kristjan
11. Helen
12. Rasmus
13. Gregor

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 3
1. Mari
2. Kati
3. Jüri
4. Toomas
5. Anneli
6. Karl
7. Liis
8. Mart
9. Sandra
10. Kristjan
11. Helen
12. Rasmus
13. Gregor
Vali eemaldatava õpilase number: 1

Nimi 'Mari' eemaldati nimekirjast!
1. Kati
2. Jüri
3. Toomas
4. Anneli
5. Karl
6. Liis
7. Mart
8. Sandra
9. Kristjan
10. Helen
11. Rasmus
12. Gregor

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 4
Mitu nime soovid näha: 2

1. Kati
2. Jüri

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 5
Suvaline valik: Rasmus

1. Näita kõiki nimesid
2. Lisa nimi
3. Eemalda nimi
4. Näita esimesed n nime
5. Vali suvaline õpilane
6. Sulge programm

Vali tegevus (1-6): 6
Lõplik nimekiri oli:
1. Kati
2. Jüri
3. Toomas
4. Anneli
5. Karl
6. Liis
7. Mart
8. Sandra
9. Kristjan
10. Helen
11. Rasmus
12. Gregor
```

---

## Ülesanne 3 – Andmesisestusviga
**Failinimi:** `sensorilogid.py`

### Eesmärk
Sa töötad keskkonnaseire keskuses, kus loetakse iga tunni tagant temperatuuriandmeid automaatselt. Kahjuks sattus logisse valed väärtused: -999 ja 9999, mis tähistavad vigaseid või katkestatud mõõtmisi.
Sinu ülesanne on puhastada andmed, sorteerida need ning teha lihtne statistiline analüüs.

### Ettevalmistus
1. Veendu, et `andmete_lugeja.py` on loodud ja toimib
2. Tutvu faili `logid_sensor.txt` sisuga

### Nõuded
1. Loo funktsioon `lae_temp_failist(failinimi)`:
    - **Parameeter:** 
        - failinimi (str): Faili nimi, kust temperatuuri andmeid lugeda
    - **Tagastab:**
        - list[str]: Temperatuuride list
        - []: Tühi list vea korral
    - **Kirjeldus:**
        - Import: Impordi failist `andmete_lugeja.py` funktsioon `loe_tekst_failist(failinimi)`
        - Faili lugemine: Kasuta importitud funktsiooni faili sisu lugemiseks
        - Vea kontroll: Kui loetud faili sisu on None, tagasta tühi list ja kuva veateade
        - Teksti töötlemine:
            - Jaga tekst ridadeks
            - Eemalda igast reast tühikud
            - Jäta välja tühjad read
        - Tagastus: Tagasta temperatuuride list (kõik elemendid on stringid)

2. Loo funktsioon `puhasta_andmed(failinimi)`, mis eemaldab vigased mõõtmised
    - **Parameetrid:**
        - failinimi (str): Faili nimi, kust temperatuuri andmeid lugeda
    - **Tagastab:**
        - list[float]: Puhastatud temperatuuride list (float tüübis)
        - []: Tühi list vea korral
    - **Kirjeldus:**
        - Andmete laadimine: Kutsu välja funktsioon `lae_temp_failist(failinimi)`
        - Vea kontroll: Kui laetud andmete list on tühi, tagasta tühi list
        - Andmete filtreerimine:
            - Kasuta `try-except` blokki `ValueError` püüdmiseks
            - Teisenda temperatuuri string float tüübiks
            - Eemalda vigased andmed: `-999`, `9999`, `99999`
            - Jäta vigased read vahele
        - Tagastus: Tagasta puhastatud temperatuuride list (float tüübis)

3. Loo funktsioon `sorteeri_mootmised(puhtad_mootmised)`, mis sorteerib mõõtmised kasvavalt
    - **Parameeter:**
        - puhtad_mootmised (list[float]): List, mis sisaldab korrektseid temperatuure
    - **Tagastab:** 
        - list[float]: Sorteeritud temperatuuride list kasvavas järjekorras
        - []: Tühi list kui sisend on tühi
    - **Kirjeldus:**
        - Kontrolli, ega funktsiooni parameeter pole tühi
            - Kui on tühi, kuva veateade ja tagasta tühi list
        - Sorteeri list kasvavasse järjekorda
        - Tagasta sorteeritud list

4. Loo funktsioon `arvuta_statistika(sorteeritud_mootmised)`, arvutab põhilise statistika mõõtmistele
    - **Parameeter:**
        - sorteeritud_mootmised (list[float]): Puhastatud ja sorteeritud temperatuurid kasvavas järjekorras
    - **Tagastab:**
        - dict, int: Statistika sõnastik ja mõõtmiste arv, mis on väiksemad kui keskmine temperatuur
        - {}, 0: Tühi sõnastik ja 0 vea korral
    - **Kirjeldus:**
        - Kontrolli, ega funktsiooni parameeter pole tühi
            - Kui on tühi, kuva veateade ja tagasta tühja sõnastik ning 0
        - Statistika arvutamine:
            - Leia väikseim mõõtmine
            - Leia suurim mõõtmine
            - Leia mõõtmiste koguarv
            - Arvuta keskmine temperatuur
            - Ümarda keskmine ühe komakohani
        - Dictionary loomine: Loo dictionary järgmiste võtmetega:
            - `min`: väikseim mõõtmine, float
            - `max`: suurim mõõtmine, float
            - `kokku`: mõõtmiste koguarv, int
            - `keskmine`: keskmine (ühe komakohaga), float
        - Alla keskmise loendamine: Loe, mitu mõõtmist on väiksemad kui arvutatud keskmine
        - Tagastus: Tagasta nii dictionary kui ka alla keskmise mõõtmiste arv

5. Loo funktsioon `main()`, mis kutsub välja kõik funktsioonid ning prindib tulemused:
    - Kutsu välja funktsioon `puhasta_andmed(failinimi)`
    - Kutsu välja funktsioon `sorteeri_mootmised(puhtad_mootmised)`
    - Kutsu välja funktsioon `arvuta_statistika(sorteeritud_mootmised)`
    - Prindi välja tulemused kujul:
        - `Puhastatud ja sorteeritud mõõtmised: {sorteeritud}`
        - `Mõõtmisi kokku: {kokku_mootmisi}`
        - `Keskmine temperatuur: {avg_temp} °C`
        - `Alla keskmise mõõtmised kokku: {alla_keskmise}`

6. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

### Väljund

```python
Laaditud 44 nime failist 'logid_sensor.txt'
Puhastatud ja sorteeritud mõõtmised: [11.4, 12.3, 12.7, 13.2, 13.7, 13.8, 14.2, 14.3, 14.7, 14.9, 15.2, 15.5, 15.8, 15.9, 16.1, 16.4, 16.7, 16.9, 17.0, 17.8, 18.3, 18.7, 19.2, 19.5, 20.1]
Mõõtmisi kokku: 25
Keskmine temperatuur: 15.8 °C
Alla keskmise mõõtmised kokku: 12
```

---

## Ülesanne 4 – Nädala temperatuurid
**Failinimi:** `nadala_temperatuurid.py`

### Eesmärk
See programm analüüsib nädala temperatuure, arvutab iga päeva keskmise temperatuuri ja leiab kõige soojema ning külmema päeva.

### Kirjeldus
Sul on antud nädal (E–P), mille iga päeva kohta on salvestatud 5 mõõdetud temperatuuri. Programm:
1. Arvutab iga päeva kohta keskmise temperatuuri
2. Loob sõnastiku, kus võtmed on nädalapäevad ja väärtused vastavad keskmised temperatuurid
3. Kuvab iga päeva nime ja selle keskmise temperatuuri (ühe komakohaga)
4. Leiab ja kuvab kõige soojema ja külmema päeva

### Nõuded
1. Loo funktsioon `leia_paeva_keskmine(paevad, paevade_temp)`:
    - **Parameetrid:**
        - list[string]: Nädalapäevade list `["E", "T", "K", "N", "R", "L", "P"]`
        - list[list[int]]: Listide list - iga alamlist sisaldab ühe päeva 5 temperatuurimõõtmist
    - **Tagastab:**
        - dict: Sõnastik, kus võtmed on nädalapäevad (str) ja väärtused keskmised temperatuurid (float, 1 komakohaga)
        - {}: Tühi sõnastik vea korra
    - **Kirjeldus:**
        - Sisendi kontrollimine:
            - Kontrolli, et mõlemad parameetrid ei ole tühjad
            - Kontrolli, et parameetrid `paevad` ja `paevade_temp` on sama pikkusega
            - Kui mõni kontroll ebaõnnestub, kuva sobilik veateade ja tagasta tühi sõnastik
        - Kasuta `try-except` blokki võimalike vigade püüdmiseks
            - Vea korral kuva veateade
        - Keskmiste arvutamine:
            - Iga päeva kohta:
            - Kui alamlist on tühi või tekib viga arvutamisel, jäta see päev vahele ja jätka järgmise päevaga
            - Arvuta iga päeva jaoks keskmine temperatuur
            - Ümarda tulemus 1 komakohani
            - Lisa sõnastikku: `{päeva_nimi: keskmine_temp}`
        - Tagastamine:
            - Tagasta sõnastik kujul `{"E": 3.5, "T": 1.9, ...}`
            - Vea korral tagasta tühi sõnastik `{}`

2. Loo funktsioon `leia_ekstreemsed(paevade_keskmised)`
    - **Parameeter:**
        - paevade_keskmised (dict): Sõnastik päevade keskmiste temperatuuridega
    - **Tagastab:**
        - tuple: Kaks elementi kujul (soojem_paev, kulmem_paev), näiteks `("T", "R:)`
        - `(None, None)`: Kui sisend on tühi
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi
            - Kui on tühi, kuva veateade ja tagasta (None, None)
        - Leia kõige kõrgema keskmise temperatuuriga päev
        - Leia kõige madalama keskmise temperatuuriga päev
        - Tagasta tuple

3. Loo funktsioon `main()` funktsioon:
    - Määra muutujad `paevad` ja `paevade_temp` (andmed on allpool)
    - Kutsu välja `leia_paeva_keskmine(paevad, paevade_temp)`
    - Kuva päevade keskmised temperatuurid koos päeva nimedega kujul `"Päevade keskmised: {paevade_avg_dict}"`
    - Kutsu välja `leia_ekstreemsed(paevade_avg_dict)`
    - Kutsub välja kõik funktsioonid
    - Kuva soojema päeva info kujul: `"Soojem keskmine: {soojem_paev} ({soojem_paeva_temp})"`
    - Kuva külmema päeva info kujul: `"Külmem keskmine: {kulmem_paev} ({kulmem_paev_temp})"`

4. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

## Andmed:
``` python
paevad = ["E", "T", "K", "N", "R", "L", "P"]

paevade_temp = [
    [3.2, 4.1, 5.0, 2.9, 2.4],      # E
    [1.0, 2.3, 3.3, 2.0, 0.9],      # T
    [0.5, 1.1, 2.0, 1.6, 0.7],      # K
    [2.2, 3.0, 4.4, 3.5, 2.9],      # N
    [1.9, 1.5, 2.2, 1.7, 1.3],      # R
    [0.0, -0.5, -0.8, -1.0, -1.3],  # L
    [1.2, 1.9, 2.0, 2.5, 1.8]       # P
]
```

### Programmi väljund

```python
Päevade keskmised: {'E': 3.5, 'T': 1.9, 'K': 1.2, 'N': 3.2, 'R': 1.7, 'L': -0.7, 'P': 1.9}
Soojem keskmine: E (3.5)
Külmem keskmine: L (-0.7)
```

---

## Ülesanne 5 – Inimesed vanusegruppidesse
**Failinimi:** `vanusegrupid.py`

### Eesmärk
Sul on sõnastik, kus iga võtmena on inimese nimi ja väärtusena tema vanus. Loome listi, kus sees on väiksemad listid ehk vanusegupid.

### Ettevalmistus
1. Veendu, et `andmete_lugeja.py` on loodud ja toimib
2. Tutvu faili `vanused.txt` sisuga

### Nõuded
1. Loo funktsioon `lae_vanused_failist(failinimi)`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, kust inimeste andmeid lugeda
    - **Tagastab:**
        - dict: Sõnastik, kus võtmed on nimed (str) ja väärtused vanused (int)
        - {}: Tühi sõnastik vea korral
    - **Kirjeldus:**
        - Import: Impordi failist `andmete_lugeja.py` funktsioon `loe_tekst_failist(failinimi)`
        - Faili lugemine: Kasuta importitud funktsiooni faili sisu lugemiseks
        - Vea kontroll: Kui loetud faili sisu on None, tagasta tühi sõnastik ja kuva veateade
        - Kasutab `try-except` blokki `IndexError` jaoks
        - Teksti töötlemine:
            - Jaga tekst ridadeks
            - Iga rea kohta:
                - Eemalda igast reast tühikud
                - Jäta välja tühjad read
                - Tükelda rida sobiva eraldajaga -> vaata faili formaati
                - Kasuta `try-except` blokki `ValueError` ja `IndexError` püüdmiseks
                    - Kontrolli, et tükeldamise tulemusena on täpselt 2 osa (nimi ja vanus)
                    - Teisenda vanus int tüübiks
                    - Vea korral kuva veateade ja jätka
                - Lisa sõnastikku: {nimi: vanus}
        - Tagasta sõnastik kujul {"Mari": 8, "Jüri": 25, ...}

2. Loo funktsioon `jaga_inimesed_gruppidesse(nimede_vanuste_dict)`:
    - **Parameeter:**
        - dict: Sõnastik, kus võtmed on nimed (str) ja väärtused vanused (int)
    - **Tagastab:**
        - list[list[str]]: 2D list, kus on kolm alamlisti:
            - `[0]`: Laste nimed (list[str])
            - `[1]`: Täiskasvanute nimed (list[str])
            - `[2]`: Pensionäride nimed (list[str])
        - `[[], [], []]`: Kolm tühja listi vea korral
    - **Kirjeldus:**
        - Vea kontroll: Kui sõnastik on tühi või None, kuva veateade ja tagasta `[[], [], []]`
        - Loo kolm tühja listi:
            - `lapsed = []` - vanus alla 13
            - `taiskasvanud = []` - vanus vahemikus 13–64 (kaasa arvatud)
            - `pensionarid = []` - vanus 65 ja üle
        - Käi läbi kõik inimesed sõnastikus:
            - Kui vanus < 13 → lisa nimi lapsed listi
            - Kui 13 ≤ vanus ≤ 64 → lisa nimi taiskasvanud listi
            - Kui vanus ≥ 65 → lisa nimi pensionarid listi
        - Tagastus: Tagasta 2D list kujul [lapsed, taiskasvanud, pensionarid]

3. Loo funktsioon `main()` funktsioon:
    - Kutsu välja funktsioon `lae_vanused_failist(failinimi)`
    - Kutsu välja funktsioon `jaga_inimesed_gruppidesse(nimede_vanuste_dict)`
    - Prindi välja tulemused -> nimed komadega eraldatult, mitte listi formaadis:
        - `Lapsed (alla 13): {nimed_lapsed}`
        - `Täiskasvanud (13-64): {nimed_täiskasvanud}`
        - `Pensionärid (üle 64): {nimed_pensionärid}`

4. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

### Programmi väljund
```
Lapsed (alla 13): Mari, Karl, Liis
Täiskasvanud (13-64): Jüri, Kati, Anneli, Sandra, Rasmus
Pensionärid (üle 64): Toomas
```

---

## Ülesanne 6 – Töötajate andmebaas
**Failinimi:** `tootajate_andmebaas.py`

### Eesmärk
Sul on ettevõtte töötajate andmebaas, mis on salvestatud tekstifailis. Loome programmi, mis suudab andmeid lugeda, töödelda ja kuvada erinevaid statistikaid ning teha muudatusi andmebaasis.

### Ettevalmistus
1. Veendu, et `andmete_lugeja.py` on loodud ja toimib
2. Tutvu faili `tootajad.txt` sisuga

### Nõuded
1. Loo funktsioon `lae_tootajad_failist(failinimi)`:
    - **Parameeter:**
        - failinimi (str): Faili nimi, kust inimeste andmeid lugeda
    - **Tagastab:**
        - dict: Sõnastik, kus võtmed on töötaja ID-d ja väärtused on töötajate andmed
        - {}: Tühi sõnastik vea korral
    - **Kirjeldus:**
        - Import: Impordi failist `andmete_lugeja.py` funktsioon `loe_tekst_failist(failinimi)`
        - Faili lugemine: Kasuta importitud funktsiooni faili sisu lugemiseks
        - Vea kontroll: Kui loetud faili sisu on `None`, kuva veateade ja tagasta tühi sõnastik
        - Teksti töötlemine:
            - Jaga tekst ridadeks
            - Eemalda igast reast tühikud
            - Jäta välja tühjad read
            - Tükelda rida sobiva eraldajaga -> vaata faili formaati
            - Kontrolli, et tükeldamise tulemusena on vähemalt kõik vajalikud väljad alles
            - Kasuta ainult vajalikke välju, ignoreeri võimalikke lisaväljasid
            - Jäta read, kus on vähem kui 4 välja vahele
        - Tagastus: Tagastus: Tagasta sõnastik kujul:
            ```python
            {
                "001": {"nimi": "Mari", "amet": "Arendaja", "palk": 3200},
                "002": {"nimi": "Jüri", "amet": "Disainer", "palk": 2900}
            }
            ```

2. Loo funktsioon `kuva_koik_tootajad(tootajad)`:
    - **Parameeter:**
        - dict: Töötajate andmete sõnastik
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi ega None -> kui on kuva veateade ja välju funktsioonist (tühi `return`)
        - Kuva kõik töötajad formaadis:
            ```python
            ID: 001, Nimi: Mari, Amet: Arendaja, Palk: 3200
            ID: 002, Nimi: Jüri, Amet: Disainer, Palk: 2900
            ```

3. Loo funktsioon `kuva_tootajad_ameti_jargi(tootajad)`:
    - **Parameeter:** 
        - dict: Töötajate andmete sõnastik
    - **Tagastab:**
        - `None`
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi ega None -> kui on kuva veateade ja välju funktsioonist
        - Küsi kasutajalt ameti nimetus
        - Kasutaja sisestamise puhul ignoreeri suurtähti
        - Kuva kõik selle ameti töötajad
        - Kuva teade, kui ameti töötajaid ei leitud

4. Loo funktsioon `arvuta_keskmine_palk(tootajad)`:
    - **Parameeter:**
        - dict: Töötajate andmete sõnastik
    - **Tagastab:**
        - float: Ettevõtte keskmine palk
        - None: Vea korral
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi:
            - Kui on kuva veateade ja tagasta None
        - Leia ettevõtte keskmine palk
        - Tagasta ettevõtte keskmine palk (float)

5. Loo funktsioon `leia_korgeima_palgaga_tootaja(tootajad)`:
    - **Parameeter:** tootajad (dict): Töötajate andmete sõnastik
    - **Tagastab:**
        - str: Kõrgeima palgaga töötaja ID
        - None: Vea korral -> kui sõnastik on tühi või None
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi -> kui on kuva veateade ja tagasta None
        - Leia kõrgeima palgaga töötaja ID
        - Tagasta ettevõtte kõrgeima palgaga töötaja ID (string)

6. Loo funktsioon `tee_arendajatele_palgatous(tootajad)`:
    - **Parameeter:** tootajad (dict): Töötajate andmete sõnastik
    - **Tagastab:**
        - dict: Töötajate andmete sõnastik, mis sisaldab muudetud palka
        - {}: Tühi sõnastik ainult siis, kui sisend oli tühi või None
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole tühi -> kui on kuva veateade
        - Leia kõik arendajad
        - Suurenda nende palka 5% võrra
        - Kuva iga arendaja vana ja uus palk
        - Kontrolli, kas leiti arendajad
            - Kui arendajaid ei leitud, kuva teade ja tagasta algne sõnastik
        - Tagasta sõnastik, mis sisaldab muudetud palka

7. Loo funktsioon `lisa_uus_tootaja(tootajad)`:
    - **Parameeter:** tootajad (dict): Töötajate andmete sõnastik
    - **Tagastab:**
        - dict: Töötajate andmete sõnastik, mis sisaldab uue töötaja infot
        - {}: Tühi sõnastik ainult siis, kui sisend oli tühi või None
    - **Kirjeldus:**
        - Kontrolli, et sõnastik ei ole None ega tühi -> kui on, kuva veateade ja tagasta {}
        - Küsi kasutajalt uue töötaja ID-d
        - Kontrolli, et ID pole juba kasutusel:
            - Kui ID on juba kasutuses, määra uuele töötajale ise ID
            - Töötajate ID-d lähevad loogilises järjestuses (vaata faili `tootajad.txt` formaati)
        - Küsi kasutajalt uue töötaja nime, ametit ja palka
        - Palk jääb stringiks nagu failist loetud
        - Kasuta `try-except` blokki palga sisestamisel -> `ValueError` püüdmiseks
        - Lisa töötaja sõnastikku
        - Kuva kinnituse teade, et uus töötaja on lisatud
        - Tagasta sõnastik, mis sisaldab uue töötaja infot

8. Loo funktsioon `main()` funktsioon:
    - Lae töötajate andmed failist
    - Kutsu välja kõik vajalikud funktsioonid õiges järjekorras:
        1. Kuva kõikide töötajate andmed
        2. Küsi ja kuva töötajad ameti järgi
        3. Arvuta keskmine palk
            - Kuva ettevõtte keskmine palk ning ümarda see ühe komakohani
        4. Leia kõrgeima palgaga töötaja
            - Kuva kõrgeima palga töötaja andmed: ID, nimi, amet ja palk
        5. Tee arendajatele palgatõus
        6. Lisa uus töötaja
        7. Kuva kõikide töötajate andmed

9. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

### Programmi väljund
```python
ID: 001, Nimi: Mari, Amet: Arendaja, Palk: 3200
ID: 002, Nimi: Jüri, Amet: Disainer, Palk: 2900
ID: 003, Nimi: Kati, Amet: Arendaja, Palk: 3500
ID: 004, Nimi: Toomas, Amet: Juht, Palk: 5000
ID: 005, Nimi: Liis, Amet: Disainer, Palk: 2800
ID: 006, Nimi: Andres, Amet: Müügimees, Palk: 2700
ID: 007, Nimi: Kristiina, Amet: Arendaja, Palk: 3800
ID: 008, Nimi: Peeter, Amet: Juht, Palk: 4500
ID: 009, Nimi: Maarika, Amet: Raamatupidaja, Palk: 2500
ID: 010, Nimi: Risto, Amet: Disainer, Palk: 3100
ID: 011, Nimi: Laura, Amet: Arendaja, Palk: 3400
ID: 012, Nimi: Martin, Amet: IT tugi, Palk: 2600
ID: 013, Nimi: Kadri, Amet: Müügimees, Palk: 2900
ID: 014, Nimi: Tõnu, Amet: Turundaja, Palk: 3300
ID: 015, Nimi: Ene, Amet: Raamatupidaja, Palk: 2400

Sisesta ameti nimetus: it tugi

Kõik it tugi:
ID: 012, Nimi: Martin, Palk: 2600

Ettevõtte keskmine palk: 3240.0

Kõrgeima palga saajad on:
ID: 004, Nimi: Toomas, Amet: Juht, Palk: 5000

Teen arendajatele palgatõusu 5%
Mari: 3200€ -> 3360€
Kati: 3500€ -> 3675€
Kristiina: 3800€ -> 3990€
Laura: 3400€ -> 3570€

Sisesta uue töötaja ID: 007
ID '007' on juba kasutusel!
Määran automaatselt uue ID: 016
Sisesta uue töötaja nimi: Gregor
Sisesta uue töötaja amet: Koristaja
Sisesta uue töötaja palk: 5555

Lisatud uus töötaja: Gregor
ID: 001, Nimi: Mari, Amet: Arendaja, Palk: 3360
ID: 002, Nimi: Jüri, Amet: Disainer, Palk: 2900
ID: 003, Nimi: Kati, Amet: Arendaja, Palk: 3675
ID: 004, Nimi: Toomas, Amet: Juht, Palk: 5000
ID: 005, Nimi: Liis, Amet: Disainer, Palk: 2800
ID: 006, Nimi: Andres, Amet: Müügimees, Palk: 2700
ID: 007, Nimi: Kristiina, Amet: Arendaja, Palk: 3990
ID: 008, Nimi: Peeter, Amet: Juht, Palk: 4500
ID: 009, Nimi: Maarika, Amet: Raamatupidaja, Palk: 2500
ID: 010, Nimi: Risto, Amet: Disainer, Palk: 3100
ID: 011, Nimi: Laura, Amet: Arendaja, Palk: 3570
ID: 012, Nimi: Martin, Amet: IT tugi, Palk: 2600
ID: 013, Nimi: Kadri, Amet: Müügimees, Palk: 2900
ID: 014, Nimi: Tõnu, Amet: Turundaja, Palk: 3300
ID: 015, Nimi: Ene, Amet: Raamatupidaja, Palk: 2400
ID: 016, Nimi: Gregor, Amet: Koristaja, Palk: 5555
```

--- 

## Ülesanne 7 – Kehtivate sünniaastate filtreerimine
**Failinimi:** `sorteeri_sunniaastad.py`

### Eesmärk
Sa töötad uuringufirmas ning sa pead tegema andmeanalüüsi. Fail sisaldab igal real ühte sünniaasta väärtust, kuid osa neist on:
1. Vigased -> abcd, tühjad read, kirjavead
2. Liiga vanad või ebarealistlikud -> 1800, 3025
3. Ebasobivad uuringu jaoks -> meid huvitavad **ainult inimesed sünniaastatega 2000–2025**

### Ettevalmistus
1. Veendu, et `andmete_lugeja.py` on loodud ja toimib
2. Tutvu faili `sunniaastad_data.txt` sisuga

Sinu ülesanne on:
- Töödelda fail automaatselt
- Jätta alles **ainult kehtivad ja huvipakkuvad sünniaastad**
- Salvestada need uude listi ning kuvada vastavad statistilised tulemused

### Nõuded
1. Loo funktsioon `lae_koik_sunniaastad_failist(failinimi)`:
    - **Parameeter:**
        - - failinimi (str): Faili nimi, kust inimeste andmeid lugeda
    - **Tagastab:**
        - List: list, kus on kõik sünniaastad
        - []: Tühi list vea korral
    - **Kirjeldus:**
        - Import: Impordi failist `andmete_lugeja.py` funktsioon `loe_tekst_failist(failinimi)`
        - Faili lugemine: Kasuta importitud funktsiooni faili sisu lugemiseks
        - Vea kontroll: Kui loetud faili sisu on `None`, kuva veateade ja tagasta tühi list
        - Andmete töötlemine:
            - Jäta välja tühjad read
            - Tükelda rida sobiva eraldajaga -> vaata faili formaati
            - Kui rida ei ole täisarv, ignoreeri -> kasuta `try-except` blokki
        - Lisa kõik sünniaastad listi
        - Tagastus: Tagasta sünniaastade list

2. Loo funktsioon `filtreeri_sunniaastad(andmete_list, min_aasta=2000, max_aasta=2025)`:
    - **Parameetrid:**
        - List: List, kust on kõik sünniaastad
        - int: Minimaalne kehtiv aasta (vaikeväärtus: 2000)
        - int: Maksimaalne kehtiv aasta (vaikeväärtus: 2025)
    - **Tagastab:**
        - List: list, kus on kõik sobivad sünniaastad, mis on vahemikus min_aasta (2000) kuni max_aasta (2025)
        - []: Tühi list vea korral
    - **Kirjeldus:**
        - Vea kontroll: Kui parameeter `None`, kuva veateade ja tagasta tühi list
        - Kui sünniaasta ei jää vahemikku (2000) kuni max_aasta (2025) (kaasaarvatud), eemalda see listist
        - Prindi välja sobivate andmete kogus
        - Tagastus: Tagasta list, kus on ainult sünniaastad vahemikus min_aasta kuni max_aasta


3. Loo funktsioon `leia_andmed(sobivad_sunniaastad)`:
 - **Parameeter:** sobivad_sunniaastad (list): List, kus on kõik sobivad sünniaastad
    - **Tagastab:**
        - Tuple, kujul:
            - Int -> Keskmine sünniaasta või `None` kui ei leitud
            - Int -> Vanim isik sünniaasta järgi või `None` kui ei leitud
            - Int -> Noorim isik sünniaasta järgi või `None` kui ei leitud
    - **Kirjeldus:**
        - Vea kontroll: Kui parameeter `None`, kuva veateade ja tagasta tühi list
        - Leia keskmine sünniaasta (int)
        - Leia kõige noorem (int) ja vanim isik (int) sünniaasta järgi
        - Tagastus: Keskmine sünniaasta (int), vanim (int) ja noorim (int) isik sünniaasta järgi

4. Loo funktsioon `main()`:
    - Kutsu välja kõik  vajalikud funktsioonid
    - Prindi keskmine, vanim ja noorim sünniaasta
    - Prindi vanima isiku vanus 2025. aastal
    - Prindi noorima isiku vanus 2025. aastal

5. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus

### Programmi väljund
```python
Loen sünniaastate andmeid failist...
Kokku leitud 131 numbrilist väärtust
Sobivaid sünniaastaid kokku: 63
Keskmine sünniaasta: 2013
Vanim isik sünniaasta järgi: 2000
Noorim isik sünniaasta järgi: 2025

Vanima isiku vanus 2025. aastal: 25 aastat
Noorima isiku vanus 2025. aastal: 0 aastat
```

---

