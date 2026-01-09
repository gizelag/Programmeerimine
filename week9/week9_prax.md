# Nädal 9 praktikum – Rekursioon

## Eesmärk

1. Rekursiivse mõtlemise arendamine - õpilased õpivad lahutama keerulisi probleeme väiksemateks alamprobleemideks
2. Rekursiooni põhikomponentide valdamine - baasi ja rekursiivse sammu selge identifitseerimine ja implementeerimine
3. Praktiliste algoritmide rakendamine - rekursiooni kasutamine erinevates kontekstides nagu astendamine, otsingud ja andmestruktuurid
4. Koodikvaliteedi oskuste arendamine - type hint'ide, dokumentatsiooni ja selgete kommentaaride kirjutamine

---

## Seadistamine

1. Loo kaust/directory nimega `week9`
2. Sinna kausta salvesta kõik selle nädala praktikumi ülesanded
3. Peale lõpetamist lae kõik vajalikud failid `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kõik funktsioonid peavad olema rekursiivsed
3. Rekursiooni baas ja rekursiivne samm peavad olema selgelt määratletud
4. Kood peab olema kommenteeritud
5. Koodi stiil peab olema puhas ja loetav
6. Vigade käsitlus peab olema implementeeritud
7. Koodi käivitamine käib läbi `main()` funktsiooni kaudu

---

## Soovitused

- Kasuta `Type hint`-e kõikjal: `def funktsioon(param: int) -> int:`
- Lisa põhjalikud docstring'id kõikidele funktsioonidele
- Lisa kommentaarid, mis seletavad sinu loodud rekursiooni baasi ja sammu

---

## Ülesanne 1 – Arvu aste
**Failinimi:** `arvu_aste.py`

### Eesmärk
Loo rekursiivne funktsioon, mis arvutab arvu astme ilma `**` operaatorit kasutamata.

### Mida tähendab aste?
Aste on korrutamise lühend:
- 2³ = 2 × 2 × 2 = 8
- 5⁴ = 5 × 5 × 5 × 5 = 625

**Erijuhud:**
- Iga arv astmel 0 on 1: `5⁰ = 1`
- Negatiivne aste tähendab murdosa: `2⁻³ = 1/(2³) = 0.125`

### Rekursiooni idee
Mõtle nii:
- `2⁵ = 2 × (2⁴)`
- `2⁴ = 2 × (2³)`
- `2³ = 2 × (2²)`
- ...kuniks jõuad baasini

**Küsimused, mille üle mõelda:**
1. Mis on rekursiooni baas? (Millal lõpetame?)
2. Kuidas lihtsustada probleemi iga sammuga?
3. Kuidas käsitleda negatiivseid astendajaid?

### Nõuded
1. Funktsioon `aste(alus: int, astendaja: int) -> float`:
    - **Parameetrid:**
        - `alus (int)`: Astme alus
        - `astendaja (int)`: Arvu astendaja
    - **Tagastab:**
        - int: Astendatud väärtus
        - None: Vea korral
    - **Ülesanne:**
        - Kontrolli, kas sisendid on täisarvud, kasuta selleks `isinstance()` funktsiooni:
            - Kui sisend pole täisarv, kuva veateade ja tagasta `None`
        - Lahenda ülesanne rekursiivselt (ilma `**` operaatorita)
        - Pea meeles rekursiooni baasi ja sammu

2. Funktsioon `main()`:
    - Testi oma funktsiooni allpool toodud andmetega
    - Kuva tulemused arusaadaval kujul

3. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Testimisandmed
```python
# (alus, astendaja) → oodatav tulemus
(2, 3)      # → 8
(5, 0)      # → 1
(3, 4)      # → 81
(10, 2)     # → 100
(7, 1)      # → 7
(2, 10)    # → 1024
(4, 3)      # → 64
(2, -3)     # → 0.125
(5, -2)     # → 0.04
```

---

## Ülesanne 2 – Massiivi elementide summa
**Failinimi:** `massiivi_elementide_summa.py`

### Eesmärk
Loo rekursiivne funktsioon, mis arvutab massiivi kõigi elementide summa ilma `sum()` funktsiooni kasutamata.

### Näited
```python
[1, 2, 3, 4] → 10
[5] → 5
[] → 0  (tühja massiivi summa on 0)
```

### Rekursiooni idee
Massiivi summa saab jagada väiksemateks osadeks:
- `[1, 2, 3, 4]` summa = `1` + `[2, 3, 4]` summa
- `[2, 3, 4]` summa = `2` + `[3, 4]` summa
- `[3, 4]` summa = `3` + `[4]` summa
- `[4]` summa = `4` + `[]` summa
- `[]` summa = ?

**Küsimused, mille üle mõelda:**
1. Mis on rekursiooni baas? (Millal lõpetame?)
2. Kuidas jagada massiiv väiksemaks osaks?
3. Kuidas kombineerida esimene element ülejäänud summaga?

### Nõuded
1. Funktsioon `massiivi_summa(massiiv: list[int]) -> int`:
    - **Parameeter:**
        - `massiiv (list[int])`: Masiiv, mis sisaldab täisarve
    - **Tagastab:**
        - int: Massiivi elementide summa
        - None: Vea korral
    - **Ülesanne:**
        - Funktsioon arvutab massiivi elementide summa rekursiivselt:
            - Kontrolli, kas sisend on list, kasuta selleks `isinstance()` funktsiooni:
                - Kui sisend pole list, kuva veateade ja tagasta `None`
            - Loo sobiv rekursiooni baas
            - Loo sobiv rekursiooni samm
        - **NB!:**: kuidas saad massiivist võtta ühe elemendi ja jätkata ülejäänutega?

2. Funktsioon `main()`:
   - Testi oma funktsiooni allpool toodud andmetega
   - Kuva tulemused selgelt

3. Programmi käivitamine:
```python
   if __name__ == "__main__":
       main()
```

### Andmed ja väljund
```python
[1, 2, 3, 4]           # → 10
[]                     # → 0
[5]                    # → 5
[10, -5, 3, 7]         # → 15
[2, 4, 6, 8, 10]       # → 30
[100, 200, 300]        # → 600
[0, 0, 0, 1]           # → 1
```

---

## Ülesanne 3 – Sõne pööramine tagurpidi
**Failinimi:** `sone_pooramine_tagurpidi.py`

### Eesmärk
Loo rekursiivne funktsioon, mis pöörab sõne tagurpidi ilma `slicing`-ut (`[::-1]`) kasutamata.

### Näited
```python
"tere" → "eret"
"python" → "nohtyp"
"a" → "a"
"" → ""
```

### Rekursiooni idee
Sõne pööramine on nagu massiiv – võta tükkhaaval:
- "tere" tagurpidi = "e" + "ret" tagurpidi
- "ret" tagurpidi = "t" + "re" tagurpidi
- "re" tagurpidi = "e" + "r" tagurpidi
- "r" tagurpidi = "r"
- "" tagurpidi = ""

**Küsimused, mille üle mõelda:**
1. Mis on rekursiooni baas? (Millised sõned ei vaja pööramist?)
2. Kuidas võtta sõnest üks täht (algusest või lõpust)?
3. Kuidas kombineerida üks täht ülejäänud pööratud sõnega?

### Nõuded
1. Funktsioon `poora_sone(sone: str) -> str`:
    - **Parameeter:**
        - `sone (str)`: Sõne, mis pööratakse ümber
    - **Tagastab:**
        - str: Ümberpööratud `sone`
        - None: Vea korral
    - **Ülesanne:**
        - Funktsioon pöörab sõne tagurpidi rekursiivselt:
            - Kontrolli, kas sisend on string (sõne), kasuta selleks `isinstance()` funktsiooni:
                - Kui sisend pole string, kuva veateade ja tagasta `None`
            - Loo sobiv rekursiooni baas
            - Loo sobiv rekursiooni samm
            - Tagasta ümberpööratud string
        - **NB!:** Ära kasuta `[::-1]` ega teisi valmis pööramisfunktsioone!

2. Funktsioon `main()`:
    - Testi oma funktsiooni allpool toodud andmetega
    - Kuva tulemused selgelt

3. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Andmed ja väljund
```python
"tere"            # → "eret"
"python"          # → "nohtyp"
"a"               # → "a"
""                # → ""
"hello world"     # → "dlrow olleh"
"12345"           # → "54321"
"AbCdE"           # → "EdCbA"
1                 # → "Funktsiooni sisend pole 'str'

```


---

## Ülesanne 4 – Arvu numbrite summa
**Failinimi:** `arvu_numbrite_summa.py`

### Eesmärk
Loo rekursiivne funktsioon, mis leiab arvu kõigi numbrite summa.

### Näited
```python
123 → 1 + 2 + 3 = 6
456 → 4 + 5 + 6 = 15
0 → 0
7 → 7
```

### Rekursiooni idee
Arvu saab jagada numbriteks:
- 456 = [4, 5, 6]
- Numbrite summa = 6 + (45 numbrite summa)
- 45 numbrite summa = 5 + (4 numbrite summa)
- 4 numbrite summa = 4 + (0 numbrite summa)
- 0 numbrite summa = ?

**Küsimused, mille üle mõelda:**
1. Mis on rekursiooni baas? (Millal numbrid lõppevad?)
2. Kuidas saada arvust viimast numbrit?
3. Kuidas eemaldada arvust viimane number?
4. Milline on seos `123`, `12` ja `1` vahel?

### Nõuded
1. Funktsioon `numbrite_summa(arv: int) -> int`:
    - **Parameeter:**
        - `arv (int)`: Suvaline täisarv
    - **Tagastab:**
        - int: `arv`-u numbrite summa
        - None: Vea korral
    - **Ülesanne:**
        - Funktsioon arvutab arvu numbrite summa rekursiivselt:
            - Kontrolli, kas sisend on int, kasuta selleks `isinstance()` funktsiooni:
                - Kui sisend pole int, kuva veateade ja tagasta `None`
            - Loo sobiv rekursiooni baas
            - Loo sobiv rekursiooni samm
            - Tagasta numbrite summa

2. Funktsioon `main()`:
   - Testi oma funktsiooni allpool toodud andmetega
   - Kuva tulemused selgelt

3. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Andmed ja väljund
```python
123         # → 6
456         # → 15
0           # → 0
7           # → 7
999         # → 27
9876543210  # → 45
1024        # → 7
5678        # → 26
-1          # → 1
-10         # → 1
```

---

## Ülesanne 5 – Kahendotsing (Binary Search)
**Failinimi:** `kahendotsing.py`

### Eesmärk
Loo rekursiivne kahendotsingu algoritm, mis leiab elemendi sorteeritud massiivist logaritmilise keerukusega O(log n).

### Algoritmi selgitus
Kui sul on sorteeritud massiiv, saad otsida palju kiiremini kui iga elementi üle vaadates!
Kahendotsing töötab nii:
    1. Vaata massiivi keskmist elementi
    2. Kui keskmine element on otsitav – leidsid!
    3. Kui otsitav on väiksem kui keskmine – otsi vasakust poolest
    4. Kui otsitav on suurem kui keskmine – otsi paremast poolest
    5. Korda, kuni leiad või massiiv saab otsa (tühi massiivi)

**Päris eluline näide:** Otsid telefoniraamatust (sorteeritud tähestiku järgi):
- Aeglane viis: Vaata iga nime läbi algusest lõpuni
- Kiire viis: Ava raamat keskelt, vaata kas otsitav on ees või taga, ja korda

### Näide
```python
Massiiv: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Otsime: 7

Samm 1: Vaata keskelt (indeks 4, väärtus 9)
        7 < 9, seega otsi vasakust poolest
        [1, 3, 5, 7, 9]

Samm 2: Vaata keskelt (indeks 2, väärtus 5)
        7 > 5, seega otsi paremast poolest
        [7, 9]

Samm 3: Vaata keskelt (indeks 3, väärtus 7)
        7 == 7, LEITUD! Indeks on 3
```

### Küsimused, mille üle mõelda:
1. Kuidas leida massiivi keskmine indeks?
2. Mis on rekursiooni baas? (Millal lõpetada otsing?)
3. Kuidas öelda funktsioonile, et otsi ainult vasakust/paremast poolest?

### Nõuded
1. Loo funktsioon `kahendotsing(sorteeritud_massiiv: list[int], otsitav: int, algus: int, lopp: int) -> int`:
    - **Parameetrid:**
        - sorteeritud_massiiv (list[int]): Massiiv, mis sisaldab täisarve ning on kasvavas järjekorras
        - otsitav (int): Number, mida otsime
        - algus (int): Kust indeksist otsimist alustatakse
        - lopp (int): Millise indeksini otsime
    - **Tagastab:**
        - int: Otsitava elemendi indeks massiivis
        - None: Vea korral või kui elementi ei leita
    - **Kirjeldus:**
        - Funktsioon leiab rekursiivselt otsitava elemendi indeksi sorteeritud massiivis:
            - Kontrolli, kas sisend `sorteeritud_massiiv` on massiiv ja `otsitav` on täisarv, kasuta selleks `isinstance()` funktsiooni:
                - Kui sisend pole massiiv või otsitav pole täisarv, kuva veateade ja tagasta `None`
            - Määra parameeter `lopp`
                - See on massiivi viimane element
            - Tagasta otsitava elemendi indeks või `None`

**NB!** Selles ülesandes on oluline anda kaasa listi algus ja lõpp indeksid. Need töötavad nagu mälu - isegi kui me oleme juba sügaval rekursioonis ja meie 21 elemendilisest listist on saanud 5 elemendiline, teame me ikka oma alamlisti asukohta algses listis.

2. Loo funktsioon `main()`:
    - Määra sorteeritud massiiv
    - Testi oma funktsiooni allpool toodud andmetega
    - Kuva tulemused arusaadaval kujul

3. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Andmed ja väljund 1
```python
# Sorteeritud massiiv
sorteeritud_massiiv = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Juhtumid (otsitav)
(7)    # Indeks: 3
(1)    # Indeks: 0
(15)   # Indeks: 7
(19)   # Indeks: 9
(4)    # Indeks: None
(0)    # Indeks: None
```

### Andmed ja väljund 2
```python
# Sorteeritud massiiv
sorteeritud_massiiv = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

# Juhtumid (otsitav)
10    # Indeks: 4
2     # Indeks: 0
24    # Indeks: 11
14    # Indeks: 6
5     # Indeks: None
25    # Indeks: None
```

### Andmed ja väljund 3
```python
# Sorteeritud massiiv
sorteeritud_massiiv = [10, 25, 40, 55, 70, 85, 100]

# Juhtumid (otsitav)
55    # Indeks: 3
10    # Indeks: 0
100   # Indeks: 6
70    # Indeks: 4
50    # Indeks: None
105   # Indeks: None
```

---

## Ülesanne 6 – Failide ja kaustade suurus
**Failinimi:** `faili_suurus.py`

### Eesmärk
Kirjuta rekursiivne funktsioon, mis simuleerib failisüsteemi struktuuri ja arvutab kausta kogusuuruse. Failide suurused on baitides (byte).

### Failisüsteemi struktuur
Failisüsteem on esitatud **sõnastikuna** (dictionary), kus:
- **Võti (key):** Faili või kausta nimi (string)
- **Väärtus (value):**
    - `int` → Faili suurus baitides
    - `dict` → Alamkaust (sisaldab omakorda faile ja kaustu)

### Näide
```python
{
    "fail1.txt": 100,        # Fail, suurus 100 baiti
    "kaust1": {              # Kaust
        "fail2.txt": 200,    # Fail kausta sees
        "alamkaust": {       # Alamkaust
            "fail3.txt": 50
        }
    }
}

Kogusuurus: 100 + 200 + 50 = 350 baiti

```

### Kuidas see töötab?
Mõtle nagu failihaldur (Explorer/Finder):
    - Kui näed **faili** -> lisa selle suurus
    - Kui näed **kausta** -> mine sisse ja liida kõik seal olev kokku
    - Kui kausta sees on **veel kaustu** -> mine ka sinna sisse

**See on rekursioon!** Kaust võib sisaldada kaustu, mis sisaldab kaustu...

### Küsimused, mille üle mõelda:
1. Kuidas kontrollida, kas väärtus on fail (int) või kaust (dict)?
2. Kuidas läbida kõiki elemente sõnastikus?
3. Mis on rekursiooni baas? (Millal lõpetada?)
4. Kuidas liita kokku failide suurused ja alamkaustade suurused?


### Nõuded
1. Loo funktsioon `arvuta_suurus(failisusteem: dict) -> int`:
    - **Parameeter:**
        - failisusteem (dict): Failisüsteemi struktuur, kus võtmed on failide/kaustade nimed ja väärtused on kas:
            - int: faili suurus baitides
            - dict: alamkaust, mis sisaldab omakorda faile ja kaustu
    - **Tagastab:**
        - int: Kogu kausta suurus baitides
        - None: Vea korral
    - **Kirjeldus:**
        - Funktsioon leiab rekursiivselt kausta kogusuuruse:
            - Kontrolli, kas sisend `failisusteem` on sõnastik, kasuta selleks `isinstance()` funktsiooni:
                - Kui sisend pole sõnastik, kuva veateade ja tagasta `None`
            - Loo sobiv rekursiooni baas
            - Loo sobiv rekursiooni samm
            - Käi läbi kõik elemendid sõnastikus ja summeeri nende suurused

2. Loo funktsioon `teisenda_suurus(failisusteem: dict) -> str`:
    - **Parameeter:**
        - failisusteem (dict): Failisüsteemi struktuur, kus võtmed on failide/kaustade nimed ja väärtused on kas:
            - int: faili suurus baitides
            - dict: alamkaust, mis sisaldab omakorda faile ja kaustu
    - **Tagastab:**
        - str: Kausta suurus koos sobiva ühikuga, näiteks `"1250 B"` või `"55 KB"`
        - None: Vea korral
    - **Kirjeldus:**
        - Kasuta `arvuta_suurus(failisusteem)` funktsiooni baitide leidmiseks:
            - Parameetri kontrollimine:
                - Kasuta `try-except` blokki võimalike vigade püüdmiseks
                - Kui tekib viga, kuva enda valitud veateade ja tagasta `None`
            - Kontrolli, kas funktsioon `arvuta_suurus(failisusteem)` tagastab sobiva väärtuse:
                - Kui ei tagasta, kuva enda valitud veateade ja tagasta `None`
            - Teisendamine:
                - Kui kausta kogusuurus on < 5000:
                    - Jäta ühik baitidesse (B)
                - Kui kausta kogusuurus on >= 5000:
                    - Teisenda kausta suurus kilobaiditeks (KB)
                    - Ümarda vastus kahe komakohani
            - Tagastus: Tagasta sõne koos vastava ühikuga

**NB!** Teisendus: `1 KB = 1024 B` (mitte 1000 B)

3. Loo funktsioon `main()`:
    - Kutsub välja `teisenda_suurus(failisusteem)` funktsiooni
    - Kuvab failisüsteemi kogusuurus selgel ja inimloetaval kujul

4. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Andmed ja väljund 1
```python
failisusteem = {
    "kaust1": {
        "fail1.txt": 100,
        "fail2.py": 250,
        "alamkaust1": {
            "fail3.txt": 75,
            "fail4.py": 300
        }
    },
    "kaust2": {
        "fail5.txt": 150,
        "alamkaust2": {
            "fail6.txt": 200,
            "alamkaust3": {
                "fail7.py": 125
            }
        }
    },
    "fail8.txt": 50
}

`Failisüsteemi suurus on 1250 B`

```

### Andmed ja väljund 2
```python
failisusteem = {
    "src": {
        "main1.py": 1500,
        "utils.py": 800,
        "models": {
            "user.py": 1200,
            "database.py": 2000
        }
    },
    "tests": {
        "test_main.py": 600,
        "test_utils.py": 400
    },
    "docs": {
        "README.md": 300,
        "manual.pdf": 500
    },
    "requirements.txt": 200
}

`Failisüsteemi suurus on 7.32 KB`

```

### Andmed ja väljund 3
```python
failisusteem = {
    "fail1.txt": 10000,
    "fail2.txt": 25000 
    }

`Failisüsteemi suurus on 34.18 KB`

```
---
