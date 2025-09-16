# Nädal 2 praktikum - Loogikalaused, muutujad

## Eesmärk
1. Selle praktikumi eesmärk on õppida kasutama loogikalauseid (`if`, `elif`, `else`) ja töötama erinevate andmetüüpidega Pythonis
2. ***PS! Sõna `väljasta` tähendab `print`***

---

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week2`
2. Sinna kausta loo kõik selle nädala praktikumi ülesanded
3. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud

---

### Ülesanne 1: Kas oled piisavalt vana?
**Failinimi:** `vanus.py`

**Nõuded:**

1. Kirjuta programm, mis küsib kasutajalt tema vanust:
    - Küsi kasutajalt vanust kujul: `Sisesta oma vanus: `
    - Kasuta teksti: `Sisesta oma vanus: `
    - Kasutaja vanus peab olema täisarv

2. Väljasta vastav sõnum vanuse põhjal:
    - Negatiivne vanus, kuva tekst kujul: `Vigane vanus`
    - Alla 18 aasta, kuva tekst kujul: `Oled veel liiga noor`
    - 18-65 aastat (kaasaarvatud), kuva tekst kujul: `Oled tööeas`
    - Üle 65, kuva tekst kujul: `Oled pensionieas`

### Programmi väljund
Näide 1:
```python
Sisesta oma vanus: 3
Oled veel liiga noor
```

Näide 2:
```python
Sisesta oma vanus: 18
Oled tööeas
```

Näide 2:
```python
Sisesta oma vanus: 69
Oled pensionieas
```

Näide 4:
```python
Sisesta oma vanus: -9
Vigane vanus
```

---

### Ülesanne 2: Temperatuuri tsoonid

**Failinimi:** `temperatuuri_tsoonid.py`

**Nõuded:**

1. Küsi kasutajalt temperatuur kraadides (int)
    - Küsi kasutajalt temperatuur kujul: `Sisesta temperatuur kraadides: `
    - Kasutaja poolt sisestatud temperatuurb peab olema integer (täisarv), juhul kui ei ole lõppeb programm

2.  Väljasta vastav sõnum temperatuuri põhjal:
    - Alla 0 kraadi, kuva tekst kujul: `Jäätumine`
    - 0-10 kraadi (kaasa arvatud), kuva tekst kujul: `Külm`
    - 11-20 kraadi (kaasa arvatud), kuva tekst kujul:`Mõnus kevadilm`
    - 21-30 kraadi (kaasa arvatud), kuva tekst kujul:`Soe suvi`
    - Üle 30 kraadi, kuva tekst kujul: `Liiga kuum`

### Programmi väljund
Näide 1:
```python
Sisesta temperatuur kraadides: 12
Mõnus kevadilm
```

Näide 2:
```python
Sisesta temperatuur kraadides: 33
Liiga kuum
```

Näide 2:
```python
Sisesta temperatuur kraadides: 2
Külm
```

Näide 4:
```python
Sisesta temperatuur kraadides: 26
Soe suvi
```

Näide 5:
```python
Sisesta temperatuur kraadides: -8
Jäätumine
```

---

### Ülesanne 3: Kas arv jagub?

**Failinimi:** `kas_arv_jagub.py`

**Nõuded:**

1. Küsi kasutajalt täisarvu:
    - Küsi kasutajalt täisarvu kujul: `Sisesta täisarv: `

2. Kontrolli, kas kasutaja pool sisestatud arv jagub:
    - Kui arv jagub 3-ga, väljasta sõnum `See arv jagub 3-ga`
    - Kui arv jagub 5-ga, väljasta sõnum `See arv jagub 5-ga`
    - Kui arv jagub nii 3 kui ka 5-ga, väljasta sõnum `See arv jagub nii 3 kui ka 5-ga`
    - Kui arv ei jagu kummagagi, väljasta sõnum `See arv ei jagu 3 ega 5-ga`

### Programmi väljund
Näide 1, arv ei jagu kummagagi:
```python
Sisesta täisarv: 4
Ei jagu 3 ega 5-ga
```

Näide 2, arv nii kolme kui ka viiega:
```python
Sisesta täisarv: 15
See arv jagub nii 3 kui ka 5-ga
```

Näide 3, arv jagub ainult kolmega:
```python
Sisesta täisarv: 12
See arv jagub 3-ga
```

Näide 4, arv jagub ainult viiega:
```python
Sisesta täisarv: 55
See arv jagub 5-ga
```

---

### Ülesanne 4: Liitmine ja lahutamine

**Failinimi:** `liitmine_lahutamine.py`

**Nõuded:**

1. Küsi kasutajalt kahte täisarvu ja arvuta nende summa:
    - Kontrolli, et mõlemad arvud oleksi täisarvud
    - Kui summa on suurem kui 100, siis lahuta summast 50 ning väljasta lõpp summa
    - Kui summa on väiksem kui 50, siis korruta summa 2-ga ning väljasta lõpp summa
    - Kui summa on vahemikus 50-100, siis jäta see summa samaks ning väljasta see summa

---

### Ülesanne 5: Kas on kolmnurk?

**Failinimi:** `kolmnurk.py`

**Nõuded:**

1. Küsi kasutajalt kolme arvu, mis esindavad kolmnurga külgede pikkusi:
    - Kontrolli, et kasutaja poolt sisestatud külgede pikkused oleksid integer tüüpi
    - Kontrolli, kas neist saab moodustada kolmnurga, kasutades kolmnurga tekkimise tingimust (kahe külje summa peab olema suurem kui kolmas külg)
    - Kui külgedest saab moodusta kolmnurga:
        - Väljasta tekst, kujul: `Sellest saab moodustada kolmnurga`
        - Arvuta kolmnurga ümbermõõt ja prindi see välja, kujul: `Kolmnurga ümbermõõt: {kolmnurga_umbermoot}`
    - Kui külgedest ei saa moodustada kolmnurka:
        - Väljasta tekst, kujul: `Sellest ei saa moodustada kolmnurka`

### Programmi väljund
Näide:
```python
Sisesta esimene külg: 3
Sisesta teine külg: 8
Sisesta kolmas külg: 7
Sellest saab moodustada kolmnurga.
Kolmnurga ümbermõõt: 18
```

---

### Ülesanne 6: Liikluskaamera trahv

**Failinimi:** `liikluskaamera_trahv.py`

**Nõuded:**

1. Küsi kasutajalt auto kiirust (float):
    - Kasuta teksti: `Sisesta auto kiirus km/h: `
    - Kasutaja sisestatud kiirus on float tüüpi

2. Kontrolli kiirust ja väljasta vastav sõnum:
    - Alla 50 km/h: `Lubatud kiirus`
    - 50-80 km/h (kaasa arvatud): `Hoiatus: ole ettevaatlik!`
    - Kui kiirus on üle 80 km/h, arvuta trahvisumma ning kuva: `Kiirus! Trahv summas: {trahvi_summa} EUR`

3. Trahvisumma arvutamine:
    - Valem: `trahvi_summa = (ületatud_kiirus - 80) * 5`
    - Säilita täpsus - ära ümarda trahvisummat

---

### Ülesanne 7: Lihtne kalkulaator

**Failinimi:** `lihtne_kalkulaator.py`

**Kirjeldus:**

Loo lihtne kalkulaator, mis teeb põhilisi matemaatilisi tehted.

**Nõuded:**

1. Programm küsib kasutajalt ühte täisarvu -> kujul: `Sisesta esimene arv: `
2. Programm küsib kasutajalt tehet: `+`, `-`, `*`, `/` -> kujul: `Sisesta tehe (+, -, *, /): `
3. Programm küsib kasutajalt teist täisarvu -> kujul: `Sisesta teine arv: `
4. Programm arvutab ja väljastab tulemuse, kasutades kasutaja poolt sisestatud täisarve ning tehet
5. Kui kasutaja sisestab jagamiseks nulli, anna veateade -> kujul: `Viga! Nulliga jagamine pole lubatud.`
6. Kui tehe ei ole nimekirjas (+, -, *, /), väljasta veateade -> kujul: `Tundmatu tehe! Palun kasuta ainult +, -, * või /.`

### Programmi väljund
Näide:
```python
Sisesta esimene arv: 8
Sisesta tehe (+, -, *, /): +
Sisesta teine arv: 49
Tulemus: 57
```

---

### Ülesanne 8: Palgast maksudeni

**Failinimi:** `palk_maksud.py`

**Kirjeldus:**

Sa oled tööandja ja tahad teada kui palju töötaja enda palgast kätte saab.

**Nõuded:**

1. Küsi kasutajalt brutopalka:
    - Kasuta teksti: `Sisesta brutopalk (€): `
    - Brutopalk võib olla nii `float` kui ka `int` (näiteks 1000 või 1250.50)
    - Vigase sisendi korral lõppeb programm

2. Küsi ümardamise täpsust:
    - Kasuta teksti: `Sisesta komakohad (1 või 2): `
    - Kasutaja sisestab `1` või `2`, mis peab olema integer
    - Vigase sisendi korral lõppeb programm

3. Arvuta maksud:
    - Tulumaksu (22 %), kasutades muutujat `tulumaks`
    - Sotsiaalmaksu (33 %), kasutades muutujat `sotsiaalmaks`
    - Tööstuskindlustusmaksu (1,6 %), kasutades muutujat `tootuskindlustus`

4. Arvuta netopalk:
    - Arvutab netopalga, kasutades muutujat netopalk
    - Märkus: Sotsiaalmaksu maksab tööandja, mitte töötaja

5. Väljasta kokkuvõte, mis on ümardatud vastavalt kasutaja soovile, kujul:
    ```python
    Palgaarvestuse kokkuvõte:
    Brutopalk: {brutopalk} €
    Tulumaks (22%): {tulumaks} €
    Sotsiaalmaks (33%): {sotsiaalmaks} € (tööandja maksab)
    Töötuskindlustus (1,6%): {tootuskindlustus} €
    Netopalk (kätte saadav summa): {netopalk} €
    ```

### Programmi väljund

Näide 1 (kaks komakohta):
```python
Sisesta brutopalk (€): 1000
Sisesta komakohad (1 või 2): 2

Palgaarvestuse kokkuvõte:
Brutopalk: 1000.00 €
Tulumaks (22%): 220.00 €
Sotsiaalmaks (33%): 330.00 € (tööandja maksab)
Töötuskindlustus (1,6%): 16.00 €
Netopalk (kätte saadav summa): 764.00 €
```

Näide 2 (üks komakoht):
```python
Sisesta brutopalk (€): 1500.0
Sisesta komakohad (1 või 2): 1

Palgaarvestuse kokkuvõte:
Brutopalk: 1500.0 €
Tulumaks (22%): 330.0 €
Sotsiaalmaks (33%): 495.0 € (tööandja maksab)
Töötuskindlustus (1,6%): 24.0 €
Netopalk (kätte saadav summa): 1146.0 €
```

---

### Ülesanne 9: Kütusekulu ja tankimise hind

**Failinimi:** `kutusekulu.py`

**Kirjeldus:**

Planeerid autoreisi ja tahad teada, kui palju raha kulub tankimiseks.

**Nõuded:**

1. Küsi kasutajalt kolme väärtust:
    - Kütusekulu (float): `Sisesta auto keskmine kütusekulu (l/100km): `
    - Tee pikkus (float): `Sisesta tee pikkus (km): `
    - Kütuse hind (float): `Sisesta kütuse hind (€/liiter): `
    - Kui kasutaja sisestab teksti, siis programm katkeb

2. Arvuta kütusekulu ja maksumus:
    - Valemid:
        ```python
        kulu_liitrid = (keskmine_kulu * tee_pikkus) / 100
        kulu_maksumus = kulu_liitrid * kytuse_hind
        ```

3. Muutujate nimed, mida kasutada:
    - `kulu` -> keskmine kütusekulu (l/100km)
    - `tee_pikkus` -> teekonna pikkus (km)
    - `kütuse_hind` -> kütuse hind (€/liiter)
    - `kulu_liitrid` -> vajalik kütuse kogus (liitrid)
    - `kulu_maksumus` -> kogu maksumus (eurot)

4. Väljasta tulemused -> `kulu_liitrid` ja `kulu_maksumus`:
    - Ümarda vastused kahe komakohani, kasuta `round(väärtus, 2)` funktsiooni seleks
    - Väljasta vajalik kütuse kogus liitrites -> `Kogu teekonna jooksul kulub {kulu_liitrid} liitrit kütust.`
    - Väljasta kogu maksumus -> `Kogu tankimise maksumus on {kulu_maksumus} €.")`

**NB! Python'i round() kasutab "banker's rounding" reeglit**
Banker's rounding tähendab, et kui number on täpselt poolel teel (näiteks 2.5), siis ümardatakse lähima paarisarvuni:
- `round(2.5)` -> 2 (mitte 3)
- `round(3.5)` -> 4
- `round(4.5)` -> 4 (mitte 5)
- `round(5.5)` -> 6

**Miks?**
See vähendab ümardamisviga suurtes andmekogumites, sest pool numbreid läheb üles, pool alla.

**Tavaline ümardamine** viiks alati poole pealt ülespoole (2.5 → 3), mis tekitaks pikas perspektiivis kallutatuse.

### Programmi väljund
Näide:
```python
Sisesta auto keskmine kütusekulu (l/100km): 7
Sisesta tee pikkus (km): 200
Sisesta kütuse hind (€/liiter): 1.5
Kogu teekonna jooksul kulub 14.0 liitrit kütust.
Kogu tankimise maksumus on 21.0 €.
```

---

### Ülesanne 10: Hüppe kaugus– kui kaugele jõuad?

**Failinimi:** `huppe_kaugus.py`

**Kirjeldus:**

Sa oled sportlane ja tahad arvutada, kui kaugele hüppad, kui tead oma algkiirust ja hüppe nurka.

**Nõuded:**

1. Programm küsib kasutajalt:
    - Algkiirust (m/s), kujul: `Sisesta algkiirus (m/s): `
    - Hüppe nurka (kraadi, näiteks 30, 45, 60 jne), kujul: `Sisesta hüppe nurk (kraadi): `

2. Seejärel arvutab programm, kui kaugele sa hüppad, kasutades füüsika valemit
    - Hüppe kaugus ümarda kahe koma kohani
    - Väljasta ümardatud hüppe kaugus kasutades muutujat `kaugus`

**Hüppe kauguse valem:**

```
d = (v² × sin(2θ)) / g
```

kus:

1. `d` – hüppe kaugus (m)

2. `v` – algkiirus (m/s)

3. `θ` – hüppe nurk (kraadi, teisendatakse radiaanideks)

4. `g` – gravitatsioonikiirendus (9.81 m/s²)

**Selles ülesandes on vaja kasutada `sin` tehet, mis ei ole Pythonis niisama defineeritud. Peame kasutama `import math`, et saaksime kasutada rohkem tehteid.**

**Kui tahaksime leida `sin(60)`, siis oleks kood selleks selline:**

```python
import math  # Impordime math mooduli matemaatiliste funktsioonide jaoks

# math.sin() tahab radiaane, aga me mõtleme kraadides
nurk_kraadides = 60
nurk_radiaanides = math.radians(nurk_kraadides)  # Teisendame 60° → radiaanideks

vastus = math.sin(nurk_radiaanides)  # Arvutame siinuse

print(f"sin({nurk}) = {vastus:.3f}")
```

### Programmi väljund
Näide:
```python
Sisesta algkiirus (m/s): 3.5
Sisesta hüppe nurk (kraadi): 60
Sa hüppad 1.08 meetrit kaugele.
```
---

### Ülesanne 11: Teatripileti hind

**Faili nimi:** `teatripileti_hind.py`

**Nõuded:**

1. Küsi kasutajalt vanust ja määra selle põhjal teatripileti hind:
    - Küsi kasutaja vanust, kujul: `Sisesta oma vanus: `
    - Kontrolli, et vanus oleks täisarv
    - Kui vanus on 0 või negatiivne, väljasta sõnum: `Vanus ei saa olla 0 või negatiivne!` ja lõpeta programm
    - Tavapiletihinnad:
        - 1-5 aastat (kaasa arvatud) -> hind = 0
        - 6-17 aastat (kaasa arvatud) -> hind = 8
        - 18-64 aastat (kaasa arvatud) -> hind = 12
        - 65+ aastat -> hind = 7

2. Õpilaspileti soodustus:
    - Küsi ainult 6-17-aastastelt õpilaspileti olemasolu, kujul: `Kas sul on õpilaspilet? (jah/ei): `
    - Kui kasutaja sisestab `jah`, rakenda 10% soodustus piletihinnale
    - Kõik muud vastused käsitle kui `ei`

3. Väljundi formaat:
    - Kuvab lõpliku hinna kahe komakohaga
    - Kuva piletihind kujul: `Sinu teatripileti hind on {piletihind} €.`

**Näidis väljund**

Näide 1 (tasuta pilet):
```python
Sisesta oma vanus: 4
Sinu teatripileti hind on 0.00 €.
```

Näide 2 (lapse pilet ilma soodustuseta):
```python
Sisesta oma vanus: 10
Kas sul on õpilaspilet? (jah/ei): ei
Sinu teatripileti hind on 8.00 €.
```

Näide 3 (lapse pilet õpilaspilega):
```python
Sisesta oma vanus: 15
Kas sul on õpilaspilet? (jah/ei): jah
Sinu teatripileti hind on 7.20 €.
```

Näide 4 (vanus on 0):

```python
Sisesta oma vanus: 0
Vanus ei saa olla 0 või negatiivne!
```

Näide 5 (vanus on negatiivne):

```python
Sisesta oma vanus: -1
Vanus ei saa olla 0 või negatiivne!
```

---

### Ülesanne 12: Temperatuurimuundur

**Failinimi:** `temperatuurimuundur.py`

**Ülesande kirjeldus:**

Kirjuta programm, mis küsib kasutajalt temperatuuri ja selle mõõtühiku (Celsius või Fahrenheit) ning teisendab selle teise ühikusse.

**Valemid teisendamiseks:**

1. **Celsius -> Fahrenheit**

```
F = C × (9/5) + 32
```

2. **Fahrenheit -> Celsius**

```
C = (F - 32) × (5/9)
```

**Nõuded:**

1. Küsi kasutajalt temperatuuri väärtust, kasuta selleks muutujat nimega `tempeeratuur`:
    - Temperatuuri väärtus võib olla nii integer kui ka float
    - Küsi seda kujul: `Sisesta temperatuur: `
2. Küsi kasutajalt mõõtühikut (C või F):
    - Kasuta selleks muutujat nimega `mootuhik`
    - Küsi kasutaja mõõtühikud kujul: `Kas temperatuur on C (Celsius) või F (Fahrenheit)? `
3. Tee vastavalt valik ja teisenda see teise mõõtühikusse
4. Vastav tulemus:
    - Programm teisendab kasutaja poolt sisestatud temperatuuri vastavasse mõõtühikusse
    - Programm ümardab tulemuse ühe komakohani
    - Kasuta selleks muutujat nimega `teisendatud`:
    - Väljastab teisendatud tulemused, kujul: `{temp_fahrenheit}°F on {temp_celsius}°C.`
5. Kui kasutaja sisestab tundmatu ühiku, väljastab programm sõnumi `Tundmatu mõõtühik!`


### Programmi väljund

Näide 1:
```python
Sisesta temperatuur: 28.4
Kas temperatuur on C (Celsius) või F (Fahrenheit)? F
28.4°F on -2.0°C.
```

Näide 2:
```python
Sisesta temperatuur: 18
Kas temperatuur on C (Celsius) või F (Fahrenheit)? C
18.0°C on 64.4°F.
```

Näide 3:
```python
Sisesta temperatuur: 14.4
Kas temperatuur on C (Celsius) või F (Fahrenheit)? a
Tundmatu mõõtühik!
```

---
