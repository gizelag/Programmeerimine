# Week 3 – Praktikum: Tsüklid ja loogika

## Eesmärk
1. Selle praktikumi eesmärk on õppida kasutama erinevaid tsükleid (`while`, `for`) ja luua ise erinevaid `funktsioone`
2. Rakendada tingimuslauseid reaalsetes olukordades
3. Kasutada `random` ja `time` mooduleid interaktiivsetes programmides
4. ***PS! Sõna `väljasta` tähendab `print`***

---

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week3`
2. Sinna kausta loo kõik selle nädala praktikumi ülesanded
3. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni
5. Lisatud on ka:
    ```python
    if __name__ == "__main__":
        main()
    ```

---

## Ülesanne 1 – Täringuvisked
**Failinimi:** `taringuvisked.py`

### Eesmärk
Kirjuta programm, mis simuleerib täringuviskeid seni, kuni tuleb number 6.

### Nõuded
- Loo funktsioon `taringuvise()`, mille sees on kogu programmi loogika
- Iga viske jaoks ootab, et kasutaja kirjutab sõna `"veereta"`
- Prindib iga viske tulemuse
- Kui tuleb 6, väljastab programm `Said kuue! Lõpp.` ja lõpetatakse programm
- Kasuta tsüklit, kuni kasutaja kirjutab `"lõpp"` või kuni täringu tulemuseks on `6`
- Loo funktsioon `main()`, mis on programmi põhiosa

### Abikood (alustus)
```python
import random

print("Kirjuta 'veereta', et visata täringut.")
print("Kirjuta 'lõpp', et programm lõpetada.")

# Küsib kasutajalt sisendit
kasutaja_sisend = input("Sisend: ").lower().strip()
print(f"Kasutaja sisend: {kasutaja_sisend})

taring_tulemus = random.randint(1, 2)
print(f"Täring: {taring_tulemus}")

"""
TO DO: Lisa kogu loogika täringuviseteks ning käivita ka enda põhiprogramm
"""
```

### Programmi väljund
```python
Kirjuta 'veereta', et visata täringut.
Kirjuta 'lõpp', et programm lõpetada.
Täring: 3
Sisend: veereta
Täring: 5
Sisend: veereta
Täring: 6
Said kuue! Lõpp.
```

### Mõtlemiseks
- Kuidas kontrollida, kas visatud number on 6?
- Kuidas korrata protsessi, kuni tuleb 6?
- Miks kasutame `lower()` ja `strip()` meetodeid kasutaja sisendi puhul?

--- 

## Ülesanne 2 – Arvude analüüs
**Failinimi:** `arvude_analuus.py`

### Eesmärk
Kirjuta programm, mis küsib kasutajalt **arve (1 kuni 100) ükshaaval**, kuni kasutaja kirjutab `"lõpp"`, ning seejärel analüüsib sisestatud andmeid.

### Nõuded
1. Kasuta `while` tsüklit, et **küsida täisarve seni**, kuni kasutaja kirjutab `"lõpp"`
2. Iga sisestatud arvu kohta:
    - Lisa see summale
    - Võrdle suurima väärtusega
    - Kontrolli, kas on suurem kui 50 (kui jah, siis loenda see)
    - Loenda sisestuste arv
3. **Kirjuta järgmised funktsioonid:**
    - **`leia_suurim(uus, senine_max)`** -> võtab kaks arvu parameetriteks, võrdleb neid ja tagastab suurema arvu
    - **`kas_suurem_kui_50(arv)`** -> võtab ühe arvu parameetrina, kontrollib kas see on suurem kui 50, tagastab `True` või `False`
4. Loo põhifunktsioon `main()`, mis on programmi põhiosa ning väljastab:
    - Kontrollib, et kasutaja sisestas täisarvu
    - Väljastab tulemused:
        - **Summa**
        - **Suurima arvu**
        - **Keskmise**, mis on ümardatud ühe koma kohani
        - **Mitu arvu on suuremad kui 50**

### Nõutud funktsioonid

```python
def leia_suurim(uus, senine_max):
    """
    Võrdleb kahte arvu ja tagastab suurema.
    
    Args:
        uus: kasutaja poolt sisestatud arv
        senine_max: seni suurim arv

    Returns:
        suurema arvu

    TO DO: Lisa loogika
    """
    pass

def kas_suurem_kui_50(arv):
    """
    Kontrollib, kas arv on suurem kui 50.
    
    Args:
        arv: kasutaja poolt sisestatud arv

    Returns:
        True/False

    TO DO: Lisa loogika
    """
    pass
  
def main():
    """
    Põhifunktsioon, mis kogub arvud ja teeb analüüsi.

    TO DO:
      1. Lisa loogika
      3. Kasuta leia_suurim() funktsiooni
      4. Kasuta kas_suurem_kui_50() funktsiooni
    """

    print("Sisesta arvud ükshaaval (1-100), lõpetamiseks kirjuta 'lõpp'")
    
    # ......
    # ......
    # ......

    print(f"Sisestati {arv_kokku} arvu")
    
    # ......
    # ......
```

### Programmi väljund
```
Sisesta arvud ükshaaval (1-100), lõpetamiseks kirjuta 'lõpp'
Sisesta arv (või kirjuta 'lõpp'): 34
Sisesta arv (või kirjuta 'lõpp'): 72
Sisesta arv (või kirjuta 'lõpp'): 1000
Sisesta arv (või kirjuta 'lõpp'): 90
Sisesta arv (või kirjuta 'lõpp'): lõpp

Sisestati 3 sobivat arvu
Summa: 196
Keskmine: 65.3
Suurim arv: 90
Arvude arv üle 50: 2
```

### Mõtlemiseks
- Kuidas kontrollida, kas sisend on number või sõna "lõpp"?
- Mida teha, kui kasutaja sisestab vale andme (näiteks teksti number asemel)?
- Kuidas arvutada keskmist, kui arvude arv on 0?
- Mis peaks olema suurima arvu algväärtus?
- Miks kasutatakse siin just `while` tsüklit? Mis on teiste tsüklite plussid ja miinused?

---

## Ülesanne 3 – Parooli tugevuse kontroll
**Failinimi:** `parooli_kontroll.py`

### Eesmärk
Kirjuta programm, mis küsib kasutajalt parooli sisestamist ja kontrollib selle tugevust. Kasutajal on maksimaalselt 5 katset õige parooli sisestamiseks.

### Nõuded
1. Parool peab vastama **kõigile järgmistele tingimustele**:
    - Vähemalt 8 tähemärki pikk
    - Sisaldab **nii tähti kui numbreid**
    - **Ei tohi sisaldada tühikuid**
2. Kasutajal on **maksimaalselt 5 katset**
3. Kasuta `while` tsüklit programmi põhiosas, et hallata 5 katse limiiti
4. **Kirjuta järgmised funktsioonid:**
    - **`on_piisavalt_pikk(parool)`** -> võtab parooli parameetrina, kontrollib kas see on vähemalt 8 tähemärki pikk, tagastab `True` või `False`
    - **`sisaldab_tahti_ja_numbreid(parool)`** -> võtab parooli parameetrina, kontrollib kas sisaldab nii tähti kui numbreid, tagastab `True` või `False`
    - **`ei_sisalda_tuhikuid(parool)`** -> võtab parooli parameetrina, kontrollib kas ei sisalda tühikuid, tagastab `True` või `False`
5. Põhifunktsioon `main()`, mis küsib parooli ja kontrollib seda kuni 5 korda:
    - Peab väljastama:
        - Kui parool on tugev: `Parool aktsepteeritud.`
        - Kui parool ei sobi: `Parool ei sobi. Alles on X katset.`
        - Kui kõik katsed on kasutatud: `Liiga palju katseid. Ligipääs keelatud.`
6. Kutsu põhifunktsioon välja, kasutades `if __name__ == "__main__":`

### Nõutud funktsioonid

```python
def on_piisavalt_pikk(parool):
    """
    Kontrollib, kas parool on vähemalt 8 tähemärki pikk.
    
    Args:
        parool: kasutaja poolt sisestatud parool

    Returns:
        True/False

    TO DO: Lisa loogika
    """
    pass

def sisaldab_tahti_ja_numbreid(parool):
    """
    Kontrollib, kas parool sisaldab nii tähti kui numbreid.

    NB! Kasuta loopi
    
    Args:
        parool: kasutaja poolt sisestatud parool

    Returns:
        True/False

    TO DO: Lisa loogika
    """
    pass

def ei_sisalda_tuhikuid(parool):
    """
    Kontrollib, kas parool ei sisalda tühikuid.
    
    Args:
        parool: kasutaja poolt sisestatud parool

    Returns:
        True/False

    TO DO: Lisa loogika
    """
    pass
  
def main():
    """
    Põhifunktsioon, mis küsib parooli ja kontrollib seda kuni 5 korda.
        
    TO DO:
    1. Kasuta kõiki ülalpool nimetatud funktsioone
    2. Kui parool on tugev, prindi "Parool aktsepteeritud." ja lõpeta
    3. Kui parool ei sobi, vähenda katsete arvu
    4. Prindi allesjäänud katsete arv
    """

    # Kui siia jõuad, siis kõik katsed on kasutatud
    print("Liiga palju katseid. Ligipääs keelatud.")
```

### Programmi väljund

**Edukas sisselogimine:**
```
Sisesta parool: 123
Parool ei sobi. Alles on 4 katset.
Sisesta parool: salasõna 1
Parool ei sobi. Alles on 3 katset.
Sisesta parool: minuparool123
Parool aktsepteeritud.
```

**Kõik katsed kasutatud:**
```
Sisesta parool: test
Parool ei sobi. Alles on 4 katset.
Sisesta parool: 123
Parool ei sobi. Alles on 3 katset.
Sisesta parool: abc
Parool ei sobi. Alles on 2 katset.
Sisesta parool: test123
Parool ei sobi. Alles on 1 katset.
Sisesta parool: short
Parool ei sobi. Alles on 0 katset.
Liiga palju katseid. Ligipääs keelatud.
```

### Kuidas kontrollida, kas meil on täht ja/või number?

```python
# `char` on antud hetkes, mingi üksik täht või number
char = 'a'

# Kas on täht (a-z, A-Z)
if char.isalpha():
    # Tagastab True
    print("See on täht")

# Kas on number (0-9)
if char.isdigit():
    # Tagastab False (sest 'a' ei ole number)
    print("See on number")
```

### Mõtlemiseks
- Kuidas kontrollida, kas stringis on nii tähti kui numbreid?
- Kuidas kontrollida tühikute olemasolu?
- Kuidas kombineerida kõiki kontrolle ühes funktsioonis?
- Millal täpselt tuleb katsete arvu suurendada?
- Kuidas väljuda tsüklist, kui parool on aktsepteeritud?
- Miks kasutatakse põhiprogrammis just `while` tsüklit? Mis on teiste tsüklite plussid ja miinused?

---

## Ülesanne 4 – Tikumäng
**Failinimi:** `tikumang.py`

### Eesmärk
Kirjuta tikumäng, kus kaks mängijat (inimene ja arvuti) võtavad kordamööda 1-5 tikku. Kes võtab viimase tiku, kaotab mängu.

### Mängureeglid
- Mäng algab **20 tikuga**
- Kaks mängijat võtavad kordamööda **1 kuni 5 tikku**:
    - Mängija 1: sina (inimene)
    - Mängija 2: arvuti (kasutab juhuslikku valikut)
- Kes võtab **viimase tiku**, **kaotab**
- Iga mängija peab tegema oma käigu **5 sekundi jooksul**
- Kui aeg saab täis või sisestus on vigane, võetakse **automaatselt 1 tikk**

### Nõuded
1. Kasuta `while` tsüklit mängu juhtimiseks
2. Hoia tikkude arv muutujas `tikud`
3. Hoia aktiivset mängijat muutujas `mängija`
4. Ajalimiidi mõõtmiseks kasuta `time.time()`
5. Inimene alustab mängu
6. **Kirjuta järgmised funktsioonid:**
    - **`küsi_kasutaja_käik()`** -> küsib kasutajalt sisendit, 5 sekundi jooksul -> tagastab kehtiva tikkude arvu (1-5)
    - **`arvuti_käik()`** -> genereerib juhuslikult 1-5 tikku -> tagastab valitud arvu
    - Loo põhifunktsioon **`main()`**, mis juhib kogu mängu kulgu:
        - Prindib tervitussõnumid
        - Vahetab mängijat
        - Näitab alles olevate tikkude arvu
7. Automaatselt võetakse 1 tikk, kui:
    - Sisestus võtab rohkem kui 5 sekundit
    - Sisestus pole number
    - Soovitakse võtta tikkude arv, mis on väljaspool vahemikku 1-5
    - Soovitakse võtta rohkem tikke kui alles on
8. Kutsu põhifunktsioon välja, kasutades `if __name__ == "__main__":`

### Ajalimiidi rakendamine
**Märkus:** Python-is ei saa `input()` funktsiooni ajapiiranguga katkestada ilma keeruliste meetoditeta (nagu threading või signal handling). Selles ülesandes implementeeri ajalimiit lihtsalt ja õppeotstarbeliselt:
1. Mõõda aega enne ja pärast `input()` kutset
2. Kontrolli aega pärast sisendi saamist

### Vajalikud teegid
```python
import time
import random
```

### Nõutud funktsioonid

```python
import time
import random

def küsi_kasutaja_käik():
    """
    Küsib kasutajalt sisendi 5 sekundi jooksul.
    
    Returns:
        int: kehtiv tikkude arv (1-5)
    
    TO DO:
        1. Kontroll ajalimiiti (5 sekundit)
        2. Sisendi lugemine ja kontrollimine
        3. Tagasta kehtiv arv või 1 (kui probleem)
    """
    start_time = time.time()
    kasutaja_kaik = input("Mitu tikku võtad (1-5)? ")
    # ......
    # ......


    pass

def arvuti_käik(tikud_alles):
    """
    Genereerib arvuti käigu juhuslikult.
    Args:
        tikud_alles: mitu tikku on veel alles
    Returns:
        int: juhuslik arv 1-5 vahemikus (või vähem, kui tikke on vähe)
    TO DO: Lisa loogika
    """
    # Ei saa võtta rohkem tikke kui alles on
    max_võetav = min(5, tikud_alles)
    # ....
    pass
```

### Programmi väljund

**Tavaline mäng:**
```python
Tikumäng algab! Viimase tiku võtja kaotab.
Tikke järel: 20

Mängija 1 kord (sul on 5 sekundit):
Mitu tikku võtad (1-5)? 3
Kasutaja käik: 3
Alles: 17 tikku
Tikke järel: 17

Mängija 2 (arvuti) kord:
Arvuti käik: 5
Alles: 12 tikku
Tikke järel: 12

Mängija 1 kord (sul on 5 sekundit):
Mitu tikku võtad (1-5)? 4
Aeg läbi! Võetakse automaatselt 1 tikk.
Kasutaja käik: 1
Alles: 11 tikku
Tikke järel: 11

Mängija 2 (arvuti) kord:
Arvuti käik: 1
Alles: 10 tikku
Tikke järel: 10

Mängija 1 kord (sul on 5 sekundit):
Mitu tikku võtad (1-5)? 5
Kasutaja käik: 5
Alles: 5 tikku
Tikke järel: 5

Mängija 2 (arvuti) kord:
Arvuti käik: 4
Alles: 1 tikku
Tikke järel: 1

Mängija 1 kord (sul on 5 sekundit):
Mitu tikku võtad (1-5)? 1
Kasutaja käik: 1
Alles: 0 tikku

Mängija 1 (sina) võttis viimase tiku ja KAOTAS!
Arvuti võitis!
```

**Ajalimiidi ületamisega:**
```python
Tikumäng algab! Viimase tiku võtja kaotab.
Tikke järel: 20

Mängija 1 kord (sul on 5 sekundit):
Mitu tikku võtad (1-5)? 5
Aeg läbi! Võetakse automaatselt 1 tikk.
Kasutaja käik: 1
Alles: 19 tikku
Tikke järel: 19

Mängija 2 (arvuti) kord:
Arvuti käik: 2
Alles: 17 tikku
Tikke järel: 17
```

### Mõtlemiseks
- Kuidas mõõta, kas 5 sekundit on möödunud?
- Kuidas käsitleda vigaseid sisendeid (mitte-numbrid, valed arvud)?
- Kuidas kontrollida, et ei võeta rohkem tikke kui alles on?
- Millal täpselt mäng lõpeb?
- Kuidas vahelduvalt mängijaid vahetada?
- Miks kasutatakse siin just `while` tsüklit? Mis on teiste tsüklite plussid ja miinused?

---

## Ülesanne 5 – Virtuaalne tervisekontroll

**Failinimi:** `tervisekontroll.py`

### Eesmärk
Kirjuta programm, mis simuleerib **tervisekontrolli vastuvõttu**. Kasutajalt küsitakse tervisenäitajaid, igaühe kohta antakse tagasiside ja lõpuks tehakse otsus tervisseisundi kohta.

### Nõuded
1. Küsi kasutajalt **järjest järgmised andmed**:
    - **Kehatemperatuur** (°C), küsimus: `Sisesta kehatemperatuur (°C): ` (**float**)
    - **Süstoolne vererõhk** (ülemine rõhk, mmHg), küsimus: `Sisesta vererõhk (mmHg): ` (**int**)
    - **Pulss** (lööki minutis), küsimus: `Sisesta pulss (BPM): ` (**int**)
    - **Kas inimene tunneb end halvasti?** (`jah/ei`), küsimus: `Kas patsient tunneb end halvasti? (jah/ei): ` (**string**)

2. **Sisendi andmetüübid:**
    - Temperatuur peab olema **float** (nt 36.5)
    - Vererõhk ja pulss peavad olema **int** väärtused

3. **Kirjuta järgmised funktsioonid:**
    - **`kontrolli_temperatuur(temperature)`**:
        - Funktsioon parameeteter on kasutaja poolt sisestatud temperatuur , mille andmetüüp on `float`
        - Funktsioon tagastab vastava `string`-i -> `"norm"`, `"piiripealne"` või `"kõrvalekalle"`
    - **`kontrolli_vererõhk(blood_pressure)`**:
        - Funktsioon parameeteter on kasutaja poolt sisestatud vererõhk, mille andmetüüp on `int`
        - Funktsioon tagastab vastava `string`-i -> `"norm"`, `"piiripealne"` või `"kõrvalekalle"`
    - **`kontrolli_pulss(pulse)`**:
        - Funktsioon parameeteter on kasutaja poolt sisestatud pulss, mille andmetüüp on `int`
        - Funktsioon tagastab vastava `string`-i -> `"norm"`, `"piiripealne"` või `"kõrvalekalle"`
    - **`main()`**:
        - Põhifunktsioon, mis küsib kasutajalt andmeid, analüüsib ja koostab kokkuvõte vastavalt reeglitele ning prindib soovituse
        - Koosta **kokkuvõte** vastavate reeglite järgi
        - Iga näitaja kohta prindi tagasiside (norm/piiripealne/kõrvalekalle) kohe välja

4. Kutsu põhifunktsioon välja, kasutades `if __name__ == "__main__":`

### Tervisenäitajate piirid

| Näitaja | Norm | Piiripealne | Kõrvalekalle |
|---------|------|-------------|--------------|
| **Temperatuur (°C)** | 36.0–37.5 | 35.5–35.9 või 37.6–38.0 | <35.5 või >38.0 |
| **Vererõhk (mmHg)** | 100–129 | 90–99 või 130–139 | <90 või >139 |
| **Pulss (BPM)** | 60–100 | 50–59 või 101–110 | <50 või >110 |


### Otsuse tegemise reeglid
1. Kui vähemalt **2 näitajat on "kõrvalekalle"** -> soovita arsti poole pöördumist
2. Kui **halvasti = "jah"** ja on vähemalt **1 kõrvalekalle või piiripealne** -> soovita arsti poole pöördumist
3. Kui ainult piiripealsed näitajad -> soovita jälgimist
4. Kui kõik normis -> `"Tervislik seisund on hea."`

### Nõutud funktsioonid
```python
def kontrolli_temperatuur(temperature):
    """
    Kontrollib kehatemperatuuri vastavust normile.
    
    Args:
        temperature: kehatemperatuur (float)

    Returns:
        string: "norm", "piiripealne" või "kõrvalekalle"
    """

def kontrolli_vererõhk(blood_pressure):
    """
    Kontrollib vererõhu vastavust normile.
    
    Args:
        blood_pressure: vererõhk (int)

    Returns:
        string: "norm", "piiripealne" või "kõrvalekalle"
    """

def kontrolli_pulss(pulse):
    """
    Kontrollib pulssi vastavust normile.
    
    Args:
        pulse: pulss (int)

    Returns:
        string: "norm", "piiripealne" või "kõrvalekalle"
    """
```

### Programmi väljund

**Arsti poole pöördumise soovitus:**
```
Sisesta kehatemperatuur (°C): 37.7
Temperatuur: piiripealne
Sisesta vererõhk (mmHg): 144
Vererõhk: kõrvalekalle
Sisesta pulss (BPM): 97
Pulss: norm
Kas patsient tunneb end halvasti? (jah/ei): jah
KOKKUVÕTE: 1 kõrvalekalle, 1 piiripealne.
Soovitus: Pöördu arsti poole.
```

**Hea tervislik seisund:**
```
Sisesta kehatemperatuur (°C): 36.8
Temperatuur: norm
Sisesta vererõhk (mmHg): 115
Vererõhk: norm
Sisesta pulss (BPM): 72
Pulss: norm
Kas patsient tunneb end halvasti? (jah/ei): ei
KOKKUVÕTE: 0 kõrvalekalle, 0 piiripealne.
Soovitus: Tervislik seisund on hea.
```

### Mõtlemiseks
- Kuidas kontrollida, kas arv jääb teatud vahemikku?
- Kuidas loendada erinevaid tulemusi (norm, piiripealne, kõrvalekalle)?
- Kuidas kombineerida mitut tingimust otsuse tegemisel?
- Kas "jah" ja "ei" vastused on õigesti kirjutatud?

---

## Sissejuhatus: Mis on turtle?

Python `turtle` on lihtne graafikateek, mis võimaldab joonistada **käsureal toimuvate käskudega**, justkui juhiksid ekraanil olevat pliiatsit. Sobib väga hästi programmeerimise harjutamiseks, eriti funktsioonide ja tsüklite õppimisel.

#### Peamised käsud

| Käsk | Kirjeldus |
|------|-----------|
| `import turtle` | Toob turtle-mooduli programmi |
| `turtle.forward(x)` | Liigub x ühikut edasi |
| `turtle.backward(x)` | Liigub x ühikut tagasi |
| `turtle.left(kraadid)` | Pöörab vasakule |
| `turtle.right(kraadid)` | Pöörab paremale |
| `turtle.penup()` | Tõstab pliiatsi – ei joonista |
| `turtle.pendown()` | Paneb pliiatsi alla – hakkab joonistama |
| `turtle.goto(x, y)` | Liigub otse koordinaati |
| `turtle.color('red')` | Muudab joone värvi |
| `turtle.speed(0–10)` | Määrab joonistamise kiiruse |
| `turtle.circle(r)` | Joonistab ringi raadiusega `r` |
| `turtle.done()` | Lõpetab programmi |

**Lisa leiad dokumentatsioonist:** [https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

---

## Ülesanne 6 – Lihtne Kujundite Joonistaja
**Failinimi:** `turtle_kujundid.py`

### Eesmärk
Kirjuta programm, mis joonistab **kolmnurga**, **ruudu** ja **viisnurga** -> igaüks oma funktsioonis ja värvis.

### Nõuded
1. **loo 3 erinevat funktsiooni** kujundite joonistamiseks
2. **Iga kujund kasutab `for` tsüklit** külgede joonistamiseks
3. **Värvid ja kujundite asukohad peavad vastama tabelis toodud väärtustele**
4. **Kirjuta järgmised funktsioonid:**
    - **`joonista_kolmnurk()`** -> joonistab kolmnurga
    - **`joonista_ruut()`** -> joonistab ruudu
    - **`joonista_viisnurk()`** -> joonistab viisnurga
    - **`main()`** -> põhifunktsioon, mis kutsub kõik funktsioonid välja
5. **Pöördenurga arvutamine: 360° ÷ külgede_arv**

### Kujundite andmed

| Kujund | Külgede arv | Mitu ühikut liigub | Pöördenurk | Värv | Asukoht |
|--------|-------------|-------------|-----------|----------------|-------------------|
| **Kolmnurk** | 3 | 100 | 120° | `red` | (-150, 0) |
| **Ruut** | 4 | 150 | 90° | `blue` | (-50, 0) |
| **Viisnurk** | 5 | 250 | 72° | `green` | (150, 0) |

### Nõutud funktsioonid

```python
import turtle

def joonista_kolmnurk():
    """
    Joonistab punase kolmnurga.

    Kasuta for tsüklit kolmnurga joonistamiseks
    """
    turtle.goto(-100, 0)  # Liigub asukohta
    turtle.color('red')
    
    for i in range(3):
        # ......
        # ......

def joonista_ruut():
    """
    Joonistab sinise ruudu.

    TO DO: 
    1. Liiguta ruut kindlasse asukohta
    2. Lisa värv
    3. Kasuta for tsüklit ruudu joonistamiseks
    """

def joonista_viisnurk():
    """
    Joonistab rohelise viisnurga.
    
    TO DO: 
    1. Liiguta viisnurk kindlasse asukohta
    2. Lisa värv
    3. Kasuta for tsüklit viisnurga joonistamiseks
    """

def main():
    """
    Põhifunktsioon, mis joonistab kõik kujundid.
    """
    turtle.speed(5)  # Määra joonistamise kiirus
    
    # Joonista kõik kujundid
    
    # Lõpeta programm
    turtle.done()
```

### Oodatav väljund

*Programm joonistab punase kolmnurga, sinise ruudu ja rohelise viisnurga.*

![Turtle kujundid](turtle_kujundid.png)

### Mõtlemiseks
- Kuidas arvutada õiget pöördenurka iga kujundi jaoks?
- Miks on vaja `turtle.penup()` ja `turtle.pendown()` käske?
- Kuidas muuta kujundite suurust?
- Miks kasutame `for` tsüklit kujundite joonistamisel?
- Kuidas organiseerida koodi, et see oleks selge ja korduvkasutav?

---

## Ülesanne 7 – Muster kasvava kujundiga
**Failinimi:** `turtle_muster.py`

### Eesmärk
Kirjuta programm, mis joonistab kasvava mustri — iga kujund on suurem ja pööratud võrreldes eelneva sama kujundiga. Kasuta **kahte FOR tsüklit** ühes funktsioonis: üks kujundite kordamiseks, teine kujundi külgede joonistamiseks.

### Nõuded
1. **Kasuta kahte FOR tsüklit ühes funktsioonis** 
   - Esimene FOR kordab kujundeid (3 ruutu või 5 kolmnurka)
   - Teine FOR joonistab ühe kujundi külgi (4 ruudu külge või 3 kolmnurga külge)
2. **Kasuta eraldi funktsioone** kujundite joonistamiseks
3. **Joonista 3 ruutu ja 5 kolmnurka**
4. **Iga kujund on suurem ja rohkem pööratud** võrreldes eelnevaga

### Kirjuta järgmised funktsioonid:

- **`joonista_3_ruutu(alg_suurus, kasv, alg_nurk, nurga_kasv, varv)`**:
    - Joonistab 3 ruutu kasvava suuruse ja pööramisnurgaga
    - Parameetrid määravad algväärtused ja kasvusuurused
    - Ruutude asukoht: `(-100, 100)`
    - Kasutab **kahte FOR tsüklit**: välimist kujundite jaoks, sisemist külgede jaoks
    - Parameetrid:
        - `alg_suurus`=30 -> ruudu algne suurus
        - `kasv`=15 -> ruudu suuruse kasv võrreldes algse suurusega
        - `alg_nurk`=10 -> ruudu algne nurk
        - `nurga_kasv`=20 -> ruudu nurga kasv võrreldes algse nurgaga
        - `varv`=red -> ruutude värv

- **`joonista_5_kolmnurka(alg_suurus, kasv, alg_nurk, nurga_kasv, varv)`**:
    - Joonistab 5 kolmnurka kasvava suuruse ja pööramisnurgaga
    - Kolmnurkade asukoht: `(100, -100)`
    - Kasutab **kahte FOR tsüklit**: välimist kujundite jaoks, sisemist külgede jaoks
    - Parameetrid:
    - `alg_suurus`=25 -> kolmnurga algne suurus
    - `kasv`=15 -> kolmnurga suuruse kasv võrreldes algse suurusega
    - `alg_nurk`=5 -> kolmnurga algne nurk
    - `nurga_kasv`=10 -> kolmnurga nurga kasv võrreldes algse nurgaga
    - `varv`=purple -> kolmnurga värv

- **`main()`**:
    - Põhifunktsioon, mis määrab kiiruse ja kutsub teised funktsioonid välja
    - Lõpetab programmi `turtle.done()` käsuga`

### Oodatav väljund
![Turtle muster](turtle_muster.png)

### Mõtlemiseks
- Kuidas muuta nii suurust kui ka pööramisnurka iga tsükli sammuga?
- Miks on oluline kasutada `penup()` enne `goto()`?
- Kuidas kaks `for` tsüklit koos töötavad?
- Mis vahe on `turtle.right()` ja `turtle.setheading()` vahel?

---

## Ülesanne 8 – Loominguline stseen – "Sama Asi 3 Korda"
**Failinimi:** `turtle_stseen.py`

### Eesmärk
Joonista oma valitud lihtne pilt (nt puu, maja, robot, lill), ja pane see pilt lõuendile kolm korda erinevates kohtades.

### Nõuded
1. **Koosta funktsioon**, mis joonistab sinu poolt valitud pildi
2. **Kutsu seda funktsiooni 3 korda välja, kassutdes `goto(x, y)`**
3. **Värvid, suurused ja nurgad võivad varieeruda**
4. **Kasuta `turtle` dokumentatsiooni**

### Näited võimalikest piltidest:
- **Joonista 3 puud erinevates värvides**
- **Sama maja kolmes asukohas, üks suurem kui teine**
- **3 robotit: üks seisab, teine kaldus, kolmas pööratud**

### Kirjuta järgmised funktsioonid:
- **`joonista_objekt(x, y, suurus, värv)`** - joonistab valitud objekti antud asukohas ja parameetritega
- **`main()`** - põhifunktsioon, mis kutsub joonistamisfunktsiooni 3 korda

### Abikood (alustus)

```python
import turtle

def joonista_objekt(x, y, suurus, värv):
    """
    Joonistab valitud objekti (näiteks maja) antud parameetritega.
    
    Args:
        x, y: objekti asukoht
        suurus: objekti suurus (baassuurus)
        värv: peamine värv
    
    TO DO: Joonista oma valitud objekt
    """
    # Liigub asukohta
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.color(värv)
    
    # Maja alus (ruut)
    for i in range(4):
      # ......
    
    # Katus (kolmnurk)
    # ......

```

### Kaks võimalikku väljundit

![Turtle tseen robot](turtle_tseen_robot.png)

![Turtle tseen robmajaot](turtle_tseen_maja.png)

---
