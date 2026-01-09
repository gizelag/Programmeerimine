F#  


















Week 11 – Opbjekt orienteeritud programeerimine



## Eesmärk
1. Selle praktikumi eesmärk on õppida OOP põhimõtteid
2. 
3. 
4. 
5. Klasside, klassiobjektide ja objekti meetodite rakendamine

---

## Seadistamine

1. Lae Moodlist alla kõik vajalikud `.txt` failid -> need on iga vastava nädala `Praktikumi materjalid` all
2. Loo kaust/directory nimega `week11`
3. Sinna kausta pane kõik vajaminevad `.txt` failid ning salvesta sinna ka kõik selle nädala praktikumi ülesanded
4. Peale lõpetamist lae kõik vajalikud failid `GitLabi`





---

## Hindamiskriteeriumid
















1. 
2. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. 
3. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
6. Programmi käivitamine käib läbi:
    ```python
    if __name__ == "__main__:
        main()
    ```

---

## Ülesanne 1 – Linna planeerimine
**Failinimi:** `linna_planeerimine.py`

### Eesmärk
Loo klassipõhine süsteem linnas olevate majade haldamiseks, kasutades objektorienteeritud programmeerimise põhimõtteid.

### Mida tähendab objektorienteeritud programmeerimine?
Kujuta ette, et oled linnaplaneerija:

- **Klass** on nagu maja projekt/joonistus – see määratleb, millised omadused ja võimalused igal majal on
- **Objekt** on konkreetne maja, mis selle projekti järgi ehitati
- **Atribuudid** on maja omadused: `aadress = "Tartu mnt 5"`, `kortereid = 24`
- **Meetodid** on tegevused, mida majaga saab teha: `lisa_elanik()`, `renoveeri()`
- **Konstruktor (__init__)** on eriline meetod, mis käivitatakse automaatselt, kui loome uue objekti. See seab maja algsed omadused (atribuudid) paika."

**Näide analoogia:**
- Klass `Maja` ← Arhitekti joonised
- Objekt `vana_maja` ← Konkreetne maja aadressil Riia 14
- Atribuut `elanike_arv` ← Kui palju inimesi majas elab
- Meetod `lisa_elanik()` ← Keegi kolib majja sisse
 N       
### Objekti loomine ja kasutamine
```python
# Loome objekti (ehitame maja)
vana_maja = Maja("Riia 14", 12, 1985)

# Kasutame meetodit (teeme majaga midagi)
vana_maja.lisa_elanik()

# Loome teise objekti samast klassist
uus_maja = Maja("Tartu mnt 5", 24, 2018)
```

**Küsimused, mille üle mõelda:**
1. Millised andmed iga maja kohta peaksime salvestama?
2. Millised tegevused on majaga võimalikud?
3. Kuidas tagada, et elanike arv ei lähe negatiivseks?

### Nõuded
1. Loo klass `Maja` ning selle klassi konstruktor:
  - **Parameetrid:**
    - `aadress` (str): Maja aadress
    - `korterite_arv` (int): Korterite arv majas
    - `ehitusaasta` (int): Aasta, mil maja ehitati
  - **Atribuudid:**
    - `aadress (str)`: Maja aadress
    - `korterite_arv (int)`: Korterite arv majas
    - `ehitusaasta (int)`: Aasta, mil maja ehitati
    - `elanike_arv (int)`: Praegune elanike arv (algväärtus 0)
    - `renoveeritud (bool)`: Kas maja on renoveeritud (algväärtus False)

2. Loo meetod `lisa_elanik()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Suurendab olemas olevate elanike arvu ühe võrra
    - Kui uus elanik lisatakse kuvab sõnumi, näiteks: `"Majja [aadress] lisandus uus elanik. Elanikke kokku: [elanike_arv]"`

3. Loo meetod `eemalda_elanik()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Vähendab olemas olevate elanike arvu ühe võrra:
      - Kui majas on rohkem kui 0 inimest kuvab sõnumi, näiteks: `"Majast [aadress] lahkus elanik. Elanikke kokku: [elanike_arv]"`
      - Kui peale elaniku eemaldamist ei ela majas ühtegi inimest kuvab sõnumi, näiteks: `"Majast [aadress] ei saa elanikku eemaldada, sest majas pole ühtegi elanikku!"`

4. Loo meetod `renoveeri()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Renoveerib maja ehk muudab maja renoveeritud väärtuse `True`
    - Kuvab sõnumi, näiteks: `"Maja [aadress] on nüüd renoveeritud!"`

5. Loo meetod `__str__()`
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - str: Vormindatud string maja andmetega -> vaata väljundi näidet
  - **Kirjeldus:**
    - Tagastab kõik maja andmed vormindatult stringina -> vaata väljundi näidet
    - Renoveeritud väli: `"Jah"` kui True, `"Ei"` kui False

6. Loo funktsioon `main()`:
  - Loo neli erinevat `Maja` objekti
  - Demonstreeri kõigi meetodite kasutamist vähemalt kahe maja peal

7. Programmi käivitamine:
  - **Kirjeldus:**
    - Käivita programm läbi `main()` funktsiooni:
    ```python
    if __name__ == "__main__":
        main()
    ```

**PS! Testi ka ise erinevaid maju ning analüüsi, et kõik erinevad majad töötavad korrektselt!**

### Testimisandmed
```python
# Loome neli erinevat maja
vana_maja = Maja("Riia 14", 12, 1985)
uus_maja = Maja("Tartu mnt 5", 24, 2018)
kohvik_mandel = Maja("Veski 5", 3, 2000)
taltech_tartu = Maja("Puiestee 78", 0, 1878)

# Demonstreerime meetodite kasutamist
print(vana_maja)
vana_maja.lisa_elanik()
vana_maja.lisa_elanik()
vana_maja.renoveeri()
print(vana_maja)

print(uus_maja)
uus_maja.lisa_elanik()
uus_maja.eemalda_elanik()
uus_maja.eemalda_elanik()
uus_maja.lisa_elanik()
uus_maja.lisa_elanik()
print(uus_maja)
```

### Oodatav väljund
```
Maja – Riia 14
Ehitusaasta – 1985
Korterite arv: 12
Elanike arv: 0
Renoveeritud: Ei

Majja Riia 14 lisandus uus elanik. Elanikke kokku: 1
Majja Riia 14 lisandus uus elanik. Elanikke kokku: 2
Maja Riia 14 on nüüd renoveeritud!

Maja – Riia 14
Ehitusaasta – 1985
Korterite arv: 12
Elanike arv: 2
Renoveeritud: Jah


Maja – Tartu mnt 5
Ehitusaasta – 2018
Korterite arv: 24
Elanike arv: 0
Renoveeritud: Ei

Majja Tartu mnt 5 lisandus uus elanik. Elanikke kokku: 1
Majast Tartu mnt 5 lahkus elanik. Elanikke kokku: 0
Majast Tartu mnt 5 ei saa elanikku eemaldada, sest majas pole ühtegi elanikku!
Majja Tartu mnt 5 lisandus uus elanik. Elanikke kokku: 1
Majja Tartu mnt 5 lisandus uus elanik. Elanikke kokku: 2

Maja – Tartu mnt 5
Ehitusaasta – 2018
Korterite arv: 24
Elanike arv: 2
Renoveeritud: Ei
```

---

## Ülesanne 2 – Transpordi laenutus

### Nõuded 1

**Faili nimi:** `liikumisvahend.py`

1. Loo klass `Liikumisvahend` ning selle klassi konstruktor:
  - **Parameetrid:**
    - `firma (str)`: Liikumisvahendi firma
    - `alustustasu (float)`: Sõidu alustustasu eurodes
    - `saja_meetri_hind (float)`: 100 meetri hind eurodes
    - `soidukaugus (str)`: Liikumisvahendi sõidukaugus kilomeetrites
  - **Atribuudid:**
    - `firma (str)`: Liikumisvahendi firma
    - `alustustasu (float)`: Sõidu alustustasu eurodes
    - `saja_meetri_hind (float)`: 100 meetri hind eurodes
    - `soidukaugus (str)`: Liikumisvahendi sõidukaugus kilomeetrites

2. Loo meetod `soidu_hind(self, pikkus)`:
  - **Parameetrid:**
    - `pikkus (float)`: Sõidu pikkus kilomeetrites objekt
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Kui sõidu pikkus on suurem kui liikumisvahendi enda sõidukaugus:
        - Tagasta `1000`
    - Arvuta sõidu hind:
      - Kasuta valemit:
        - `hind = alustustasu + (kilomeetrid * 10 * 100 meetri hind)`
        - `1 km = 10 * 100 meetrit`
    - Tagasta sõidu hind eurodes või 1000 kui sõidukaugus pole piisav

3. Loo meetod `soida(self, pikkus)`:
  - **Parameetrid:**
    - `pikkus (float)`: Sõidu pikkus kilomeetrites
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - See meetod simuleerib liikumisvahendi sõitmist:
      - Meetod vähendab liikumisvahendi `soidukaugus` atribuuti sõidu pikkuse võrra
      - Pärast vähendamist kontrollitakse, kas `soidukaugus` on läinud negatiivseks:
        - Kui on siis määra see nulliks
        - See tagab, et sõidukaugus ei saa kunagi olla negatiivne arv
      - Meetod ei tagasta midagi, see muudab ainult objekti sisemist olekut

4. Loo meetod `lae(self, kilomeetrid)`:
  - **Parameetrid:**
    - `kilomeetrid (float)`: Kilomeetrite arv, mille võrra suurendada sõidukaugust
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - See meetod simuleerib liikumisvahendi laadimist:
      - Meetod suurendab liikumisvahendi `soidukaugus` atribuuti antud kilomeetrite võrra
      - Meetod ei tagasta midagi, see muudab ainult objekti sisemist olekut
      - Seda meetodit kasutatakse, kui liikumisvahend on laetud ja selle sõidukaugus suureneb

5. Loo meetod `__str__(self)`
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - `str`: Vormindatud string raamatu info
  - **Kirjeldus:**
    - Tagastab liikumisvahendi andmed vormindatult stringina kujul: `Firma: {self.firma}, Alustustasu: {self.alustustasu}, 100m hind: {self.saja_meetri_hind}, Sõidukaugus: {self.soidukaugus}`

6. Testige enda klassi:
    - **Kirjeldus:**
      - Lisage faili lõppu `if __name__ == "__main__":`
      - Looge `Liikumisvahend` objekt koos vastavate parameetritega:
        - Testige, kas meetod `lae`, `soida` jne teeb seda mida vaja
        - Kasutage `__str__` meetodit, et näha mida teie klassi meetodid teevad

### Nõuded 2

**Faili nimi:** `laenutus.py`

1. Loo klass `Laenutus` ning selle klassi konstruktor:
  - **Parameetrid:**
    - `liikumisvahendid` (list): List Liikumisvahendite objektidest
  - **Atribuudid:**
    - `liikumisvahendid` (list): List Liikumisvahendite objektidest

2. Loo meetod `kuva_valik(self, pikkus)`:
  - **Parameetrid:**
    - `pikkus` (float): Sõidu pikkus kilomeetrites
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Kuvab kõik liikumisvahendid järjestatuna odavaimast kallimani
    - Meetod käib läbi kõik liikumisvahendid ja arvutab igaühe jaoks antud pikkuse sõiduhinna:
      - Leia iga liikumisvahendi sõidu hind kasutades sobivat `Liikumisvahend` objekti meetodit
      - Loo list, mis sisaldab tuplet kujul (firma_nimi, hind):
        - Näidis väljund: `[('Tuvi', 115.99), ('Bolt', 6.5), ('Tuul', 8.5), ('Tartu linnaratas', 2.6)]`
      - Järjesta hinna järgi (odavaim enne) kasutades: `rattad_ja_hinnad.sort(key=lambda x: x[1])`, kus rattad_ja_hinnad on see sama list[tuple] ehk `[('Tuvi', 115.99), ('Bolt', 6.5), ('Tuul', 8.5), ('Tartu linnaratas', 2.6)]`:
        - Peale seda on see järjestatud hinna järgi ehk väljund on: `[('Tartu linnaratas', 2.6), ('Bolt', 6.5), ('Tuul', 8.5), ('Tuvi', 115.99)]`
    - Iga liikumisvahendi kuvatakse kujul: `{järjekorranumber}. {firma} - {hind} eurot`
    - Näide väljundist:
      ```
      1. Tartu linnaratas - 2.6 eurot
      2. Bolt - 6.5 eurot
      3. Tuul - 8.5 eurot
      4. Tuvi - 115.99 eurot
      ```

3. Loo meetod `laenuta(self, firma, pikkus)`:
  - **Parameetrid:**
    - `firma` (str): Liikumisvahendi firma nimi
    - `pikkus` (float): Sõidu pikkus kilomeetrites
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Meetod leiab liikumisvahendi antud firma nime järgi:
      - Kontrollitakse, kas liikumisvahendi `soidukaugus` on piisav antud pikkusega sõiduks:
        - Kui jah:
          - Arvutatakse sõidu hind kasutades sobivat `Liikumisvahend` objekti meetodit
          - Kuvatakse hind kujul, näiteks: `Sõidu hind oli {hind} eurot`
          - Vähenda sõidukaugust kasutades sobivat `Liikumisvahend` objekti meetodit
        - Kui ei:
          - Kuvatakse teade, näiteks: `Liikumisvahendi aku on liiga tühi selle sõidu jaoks.`
      - Meetod ei tagasta midagi, see muudab ainult `Liikumisvahend` objekti olekut

4. Loo meetod `lae_liikumisvahendit(self, firma, kilomeetrid)`:
  - **Parameetrid:**
    - `firma` (str): liikumisvahendi firma nimi
    - `kilomeetrid` (float): Kilomeetrite arv, mille võrra laadida
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Meetod leiab liikumisvahendi antud firma nime järgi:
      - Suurenda `soidukaugus` atribuuti kasutades sobivat `Liikumisvahend` objekti meetodit
      - Meetod ei tagasta midagi, see muudab ainult liikumisvahendi objekti olekut

### Nõuded 3

**Faili nimi:** `liikumisvahendite_programm.py`

1. Impordi mõlemad klassid siia faili:
  - **Kirjeldus:**
    Importimine käib kujul `from {failinimi_ilma_.py} import {funktsiooni/klassi nimi mida impordime}` ehk:
  ```python
      from liikumisvahend import Liikumisvahend
      from laenutus import Laenutus
  ```

2. Loo funktsioon `loe_liikumisvahendi_andmed_failist(failinimi)`:
  - **Parameetrid:**
    - `failinimi` (str): Faili nimi, kust andmeid lugeda
  - **Tagastab:**
    - `list`: List `Liikumisvahend` objektidest
    - `[]`: Vea korral
  - **Kirjeldus:**
    - Loeb liikumisvahendi andmed tekstifailist ja tagastab nende listi:
    - Loo tühi liikumisvahenite list
    - Kasuta `try-except` blokki, et käsitleda vigu:
        - Vea korral kuva veateade ja tagasta tühi list
        - Ava fail lugemiseks
        - Käi läbi kõik read failis:
          - Eemalda tühikud rea algusest ja lõpust
          - Jäta vahele tühjad read
          - Tükelda rida sobiva eraldajaga
          - Eemalda tühikud iga osa algusest ja lõpust
          - Kontrolli, et on täpselt 4 osa (firma nimi,  sõidu alustustasu, 100 meetri hind, sõidukaugus kilomeetrites)
          - Kui on 4 osa:
            - Esimene osa on liikumisvahendi firma nimi
            - Teine osa on sõidu alustustasu, teisenda `float()`
            - Kolmas osa on 100 meetri hind, teisenda `float()`
            - Neljas osa on liikumisvahendi sõidukaugus kilomeetrites, teisenda `float()`
            - Loo `Liikumisvahend` objekt nende andmetega
            - Lisa `Liikumisvahend` objekt liikumisvahenite listi
          - Kui ei ole 4 osa, jätka
        - Püüa kinni `FileNotFoundError` viga:
          - Kuva veateada ja tagasta tühi list
        - Püüa kinni kõik muud tekkivad vead:
          - Kuva üldine veateade ja tagasta tühi list
      - Tagasta liikumisvahenite objektide list

3. Loo funktsioon `main()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Põhiprogramm, mis juhib liikumisvahendite laenutussüsteemi:
      - Lae liikumisvahendite andmed failist `andmed_liikumisvahendid.txt` kasutades sobivat funktsiooni
        - Kontrolli tulemust:
          - Kui tulemus on `None`:
            - Kuva veateatega teade, et liikumisvahendite laadimine ebaõnnestus või on tühi (näiteks: `Pole liikumisvahendeid seega lähen jala, programm lõppeb.`) - Lõpeta funktsioon (välju funktsioonist)
      - Loo laenutussüsteemi objekti ehk loo `Laenutus` objekti, mis sisaldab failis laetud liikumisvahendeid
      - Demonstreeri kõiki laenutus meetodeid kasutads sobivaid  `Laenutus` objekti meetodeid

4. Programmi käivitamine:
  - **Kirjeldus:**
    - Käivita programm läbi `main()` funktsiooni:
    ```python
    if __name__ == "__main__":
        main()
    ```

**PS! Testi ka ise kogu funktsionaalsust!**

### Testimisandmed
```python
# Kuvab kõik liikumisvahendid järjestatuna odavaimast kallimani:
laenutus.kuva_valik(5)

# Demonstreerime meetodite kasutamist
laenutus.laenuta("Tuvi", 12)  # Laenutan 'Tuvi', sõidupikkus 12km

laenutus.laenuta("Bolt", 3) # Laenutan 'Bolt', sõidupikkus 3km

laenutus.laenuta("Tuul", 18)  # Laenutan 'Tuul', sõidupikkus 18km

laenutus.laenuta("Tuul", 5) # Laenutan 'Tuul', sõidupikkus 5km

laenutus.lae_liikumisvahendit("Tuul", 5)  # Laen liikumisvahendit 'Tuul', sõidupikkus 5km

laenutus.laenuta("Tuul", 2) # Laenutan 'Tuul', sõidupikkus 5km

laenutus.laenuta("Tartu linnaratas", 30)  # Laenutan 'Tartu linnaratas', sõidupikkus 30km
```

### Oodatav väljund (PS! Need print laused pole kohustusliku vaid lisasin selleks, et te näeksite paremini mis toimub)
```
1. Tartu linnaratas - 2.6 eurot
2. Bolt - 6.5 eurot
3. Tuul - 8.5 eurot
4. Tuvi - 115.99 eurot


Laenutan 'Tuvi', sõidupikkus 12km
Sõidu hind oli 136.99 eurot

Laenutan 'Bolt', sõidupikkus 3km
Sõidu hind oli 4.5 eurot

Laenutan 'Tuul', sõidupikkus 18km
Sõidu hind oli 28.0 eurot

Laenutan 'Tuul', sõidupikkus 5km
Tõukeratta aku on liiga tühi selle sõidu jaoks.

Laen liikumisvahendit 'Tuul', sõidupikkus 5km

Laenutan 'Tuul' peale laadimist, sõidupikkus 2km
Sõidu hind oli 4.0 eurot

Laenutan 'Tartu linnaratas', sõidupikkus 30km
Sõidu hind oli 15.1 eurot
```

---

## Ülesanne 3 – Raamatukogu

### Nõuded 1
**Faili nimi:** `raamat.py`

1. Loo klass `Raamat` ning selle klassi konstruktor:
  - **Parameetrid:**
    - `pealkiri (str)`: Raamatu pealkiri
    - `autor (str)`: Raamatu autor
    - `lehekuljed (int)`: Lehekülgede arv raamatus
    - `liik (str)`: Raamatu liik (romaan, detektiiv, muinasjutt jne)
  - **Atribuudid:**
    - `pealkiri (str)`: Raamatu pealkiri
    - `autor (str)`: Raamatu autor
    - `lehekuljed (int)`: Lehekülgede arv raamatus
    - `liik (str)`: Raamatu liik (romaan, detektiiv, muinasjutt jne)

3. Loo meetod `__str__(self)`
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - `str`: Vormindatud string raamatu info
  - **Kirjeldus:**
    - Tagastab raamatu andmed vormindatult stringina kujul: `"{self.pealkiri}, {self.autor}, {self.leheküljed}, {self.liik}"`

4. Testige enda klassi:
    - **Kirjeldus:**
      - Lisage faili lõppu `if __name__ == "__main__":`
      - Looge `Raamat` objekt koos vastavate parameetritega
      - Testige `__str__` meetodit
      - Kontrollige, kas väljund on õiges vormis: `pealkiri, autor, lehekülgede_arv, liik`

### Nõuded 2

**Faili nimi:** `raamatukogu.py`

1. Impordi klass `Raamat` siia faili:
  - **Kirjeldus:**
  Importimine käib kujul `from {failinimi_ilma_.py} import {funktsiooni/klassi nimi mida impordime}` ehk:
  ```python
      from raamat import Raamat
  ```

2. Loo klass `Raamatukogu` ning selle klassi konstruktor:
    - **Atribuudid:**
        - `raamatud` (list): Tühi list
        - `laenutatud_raamatud` (list): Tühi list
    - **Parameetrid:**
        - Puudub

3. Loo meetod `lisa_raamat(self, raamat)`:
  - **Parameetrid:**
    - `raamat`: Raamatu objekt, mis lisatakse
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Lisab raamatu raamatukogusse ehk lisab raamatu objekti raamatute listi

4. Loo meetod `__str__(self)`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - `str`: Raamatukogu info stringina
  - **Kirjeldus:**
    - Kontrolli, kas raamatukogus (raamatute listis) on mõni raamat:
      - Kui raamatukogu on tühi:
        - Tagasta tekst, mis ütleb, et raamatukogu on tühi
      - Kui raamatukogus on raamatuid:
        - Käi läbi kõik raamatud
        - Lisa iga raamatu kohta uus rida koos raamatu infoga (kasuta `f"\n{raamat}"`) -> kasuta `__str__` meetodit selleks
        - Tagasta koostatud string

5. Loo meetod `kuva_raamatud(self)`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Kuva kõik olemasolevad raamatud:
      - Käi läbi kõik raamatukogus (raamatute list) olevad raamatud
      - Kuva olemasolevate raamatute info: pealkiri, autor, leheküljed, liik

6. Loo meetod `kuva_laenutatud_raamatud(self)`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Kuvab kõik kasutaja poolt laenutatud raamatud:
      - Kontrolli, kas kasutaja on välja laenutanud mõne raamatu:
        - Kui ei ole ühtegi raamatut välja laenutanud:
          - Kuva vastav tekst välja
        - Kui on vähemalt ühe raamatu laenutanud:
          - Kuva mitu raamatut on ta laenutanud
          - Kuva laenutatud raamatu(te) info: pealkiri, autor, leheküljed, liik

7. Loo meetod `on_juba_laenutatud(self, pealkiri)`:
  - **Parameetrid:**
    - `pealkiri` (str): Raamatu pealkiri
  - **Tagastab:**
    - `bool`: True kui kasutaja juba laenutas selle raamatu välja, muidu False
  - **Kirjeldus:**
    - Kontrollib, kas kasutaja on juba selle raamatu laenutanud:
      - Käi läbi kõik laenutatud raamatud
      - Võrdle iga laenutatud raamatu pealkirja antud pealkirjaga (tõstutundlikkuseta)
      - Kui leitakse ühtiv pealkiri:
        - Tagasta `True`
      - Kui ei leita ühtegi ühtivat pealkirja:
        - Tagasta `False`

8. Loo meetod `laenuta_raamat(self, pealkiri)`:
  - **Parameetrid:**
    - `pealkiri` (str): Otsitava raamatu pealkiri
  - **Tagastab:**
    - `Raamat | str | None`:
        - Raamatu objekt kui vastav raamat laenutati
        - str: Kui raamat on juba laenutatud
        - None: kui raamatut ei leitud
  - **Kirjeldus:**
    - Otsib ja laenutab raamatu pealkirja järgi:
      - Kontrolli meetodi `on_juba_laenutatud(self)` abil, kas raamat on juba laenutatud:
        - Kui on juba laenutatud:
          - Tagasta string `juba_laenutatud`
      - Loo tsükkel, kus sa käid läbi kõik olemasolevad raamatud koos indeksiga:
        - Case-insensitive täpne vaste raamatute listist:
        - Võrdle raamatu pealkirja antud otsitava pealkirjaga (case-insensitive)
        - Kui leitakse täpne vaste:
          - Eemalda raamat raamatukohust (raamatute list)
          - Lisa see raamat laenutatud raamatute listi
          - Tagasta laenutatud raamat
      - Kui ei leidnud ühtegi vastet:
        - Tagasta `None`

9. Testige enda klassi:
    - **Kirjeldus:**
      - Lisage faili lõppu `if __name__ == "__main__":`
      - Looge `Raamatukogu` objekt koos vastavate parameetritega
      - Testige `__str__` meetodit
      - Analüüsige, kas teie klassi meetodid teevad seda mida peab

### Nõuded 3

**Faili nimi:** `raamatukogu_programm.py`

1. Impordi mõlemad klassid siia faili:
  - **Kirjeldus:**
    Importimine käib kujul `from {failinimi_ilma_.py} import {funktsiooni/klassi nimi mida impordime}` ehk:
  ```python
      from raamat import Raamat
      from raamatukogu import Raamatukogu
  ```

2. Loo funktsioon `loe_raamatud_failist(failinimi)`:
  - **Parameetrid:**
    - `failinimi` (str): Faili nimi, kust raamatuid lugeda
  - **Tagastab:**
    - `list`: List Raamat objektidest
    - `[]`: Vea korral
  - **Kirjeldus:**
    - Loeb raamatud tekstifailist ja tagastab nende listi:
    - Loo tühi raamatute list
    - Kasuta `try-except` blokki, et käsitleda vigu:
        - Vea korral kuva veateade ja tagasta tühi list
        - Ava fail lugemiseks
        - Käi läbi kõik read failis:
          - Eemalda tühikud rea algusest ja lõpust
          - Jäta vahele tühjad read
          - Tükelda rida sobiva eraldajaga
          - Eemalda tühikud iga osa algusest ja lõpust
          - Kontrolli, et on täpselt 4 osa (pealkiri, autor, lehekülgede arv, liik)
          - Kui on 4 osa:
            - Esimene osa on pealkiri
            - Teine osa on autor
            - Kolmas osa on lehekülgede arv, teisenda täisarvuks `int()`
            - Neljas osa on liik
            - Loo `Raamat` objekt nende andmetega
            - Lisa `Raama` objekt raamatute listi
          - Kui ei ole 4 osa:
            - Jäta vahele ja jätka
        - Püüa kinni `FileNotFoundError` viga:
          - Kuva veateada ja tagasta tühi list
        - Püüa kinni kõik muud tekkivad vead:
          - Kuva üldine veateade ja tagasta tühi list
      - Tagasta raamatute objektide list

3. Loo funktsioon `kasitle_juba_laenutatud(raamatukogu, pealkiri)`:
  - **Parameetrid:**
    - `raamatukogu` (Raamatukogu): Raamatukogu objekt
    - `pealkiri` (str): Raamatu pealkiri
  - **Tagastab:**
    - `bool`: True kui kasutaja soovib jätkata, False kui mitte
  - **Kirjeldus:**
    - Käsitleb olukorda, kus raamat on juba laenutatud:
      - Kuva kasutajale teade, et ta on selle raamatu juba laenutanud:
        - Näiteks kujul: `Sa oled raamatu {pealkiri} juba endale laenutanud`
      - Kuva kõik kasutaja laenutatud raamatud kasutades sobivat `Raamatukogu` klassi meetodit
      - Küsi, kas kasutaja soovib jätkata ehk kutsu välja sobiv funktsioon ning tagasta kasutaja vastus

4. Loo funktsioon `kysi_kas_jatkata(raamatukogu)`:
  - **Parameetrid:**
    - `raamatukogu` (Raamatukogu): Raamatukogu objekt
  - **Tagastab:**
    - `bool`: True kui kasutaja soovib jätkata, False kui mitte
  - **Kirjeldus:**
    - Küsib kasutajalt, kas ta soovib veel raamatuid laenutada:
      - Alusta lõputut tsüklit:
        - Küsi kasutajalt: `Kas soovid veel raamatuid laenutada? (jah/ei/minu): `
        - Kõikide vastuste puhul kasuta case-insensitive
            - Kui vastus on `minu`:
                - Kuva kõik kasutaja laenutatud raamatud kasutades sobivat `Raamatukogu` klassi meetodit
                - Jätka tsüklit, et küsida uuesti
            - Kui vastus on `jah`:
                - Tagasta `True`
            - Kui vastus on midagi muud ehk `ei`:
                - Tagasta `False`

5. Loo funktsioon `lopeta_programm(raamatukogu)`:
  - **Parameetrid:**
    - `raamatukogu` (Raamatukogu): Raamatukogu objekt
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Lõpetab programmi ja kuvab kasutaja laenutatud raamatud:
      - Kuva kasutajale lõpp sõnum/tänuteade, näiteks: `Aitäh raamatukogu külastamast!`
      - Kuva kõik kasutaja laenutatud raamatud kasutades sobivat `Raamatukogu` klassi meetodit

6. Loo funktsioon `kasitle_edukat_laenutust(raamatukogu, laenutatud_raamat)`:
  - **Parameetrid:**
    - `raamatukogu` (Raamatukogu): Raamatukogu objekt
    - `laenutatud_raamat` (Raamat): Laenutatud raamat
  - **Tagastab:**
    - `bool`: True kui kasutaja soovib jätkata, False kui mitte
  - **Kirjeldus:**
    - Käsitleb edukat raamatu laenutust:
        - Kuva kinnitussõnum, mis sisaldab laenutatud raamatu pealkirja, näiteks: `Raamat {laenutatud_raamat.pealkiri} edukalt laenutatud!`
      - Kuva kõik raamatukogus olevad raamatud kasutades sobivat `Raamatukogu` klassi meetodit
      - Küsi, kas kasutaja soovib jätkata ehk kutsu välja sobiv funktsioon ning tagasta kasutaja vastus

7. Loo funktsioon `initsialiseeri_raamatukogu(failinimi)`:
  - **Parameetrid:**
    - `failinimi` (str): Faili nimi, kust raamatuid lugeda
  - **Tagastab:**
    - `Raamatukogu`: Raamatukogu objekt
    - `None`: Vea korral või kui raamatukogu on tühi
  - **Kirjeldus:**
    - Initsialiseerib raamatukogu ja laeb raamatud failist:
      - Loo `Raamatukogu` objekt
      - Loe raamatud failist kasutades sobivat funktsiooni
      - **Kontrolli, kas failist lugemine õnnestus:**
        - Kui tulemus on `None`, tagasta `None` ehk faili ei leitud/oli vigane
      - Käi läbi kõik failis loetud raamatud:
        - Lisa iga raamat raamatukogusse kasutades sobivat `Raamatukogu` klassi meetodit
      - **Kontrolli, kas raamatukogusse lisati vähemalt üks raamat:**
        - Kui raamatukogu on tühi, tagasta `None`
      - Tagasta `Raamatukogu` objekt

8. Loo funktsioon `main()`:
  - **Parameetrid:**
    - Puudub
  - **Tagastab:**
    - Puudub
  - **Kirjeldus:**
    - Põhiprogramm, mis juhib raamatukogu laenutussüsteemi:
      - **Initsialiseerimise faas:**
        - Initialiseeri raamatukogu failist `raamatud.txt` kasutades sobivat funktsiooni
        - **Kontrolli initsialiseerimise tulemust:**
          - Kui tulemus on `None`, kuva veateatega teade, et raamatukogu laadimine ebaõnnestus või on tühi (näiteks: `Raamatukogu laadimine ebaõnnestus või on tühi. Programm lõppeb.`) ja lõpeta funktsioon (välju funktsioonist)
        - Kuva kõik raamatukogus olevad raamatud

      - **Põhitsükkel** (`while True`):
        - PS! Soovitus: Kuva tühi rida paremaks loetavuseks
        - Küsi kasutajalt raamatu pealkirja, mida ta soovib laenutada, näiteks: `Sisesta raamatu pealkiri, mida sa laenutada soovid: `
        - Proovi laenutada kasutaja poolt sisestatud raamatut ehk kasuta sobivat `Raamatukogu` klassi meetodit selleks ning:
            - **Kontrolli laenutamise tulemust:**
                - **Kui tulemus on `juba_laenutatud`:**
                  - Käsitle juba laenutatud raamatu olukorda ehk kutsu välja sobiv funktsioon
                  - Kui funktsioon tagastab `False` ehk kasutaja ei soovi enam jätkata:
                    - Lõpeta programm kasutades sobivat funktsiooni
                    - Lõpeta tsükkel

          - **Kui tulemus ei ole `None` ehk raamat leiti täpse vastega:**
            - Käsitle edukat laenutust ehk kutsu välja sobiv funktsioon
            - Kui funktsioon tagastab `False` ehk kasutaja ei soovi enam jätkata:
              - Lõpeta programm kasutades sobivat funktsiooni
              - Lõpeta tsükkel

          - **Kui tulemus on `None` ehk täpset raamatu vastet ei leitud:**
            - Kuva teavitustekst, et ühtegi raamatut ei leitud, näiteks: `Ei leidnud sellist raamatut, proovi uuesti!`
            - Küsi kasutajalt, kas ta soovib veel raamatuid laenutada ehk kutsu välja sobiv funktsioon:
              - Kui välja kutsutud funktsioon tagastab `False`:
                - Lõpeta programm ehk kutsu välja sobiv funktsioon
                - Lõpeta tsükkel

9. Programmi käivitamine:
  - **Kirjeldus:**
    - Käivita programm läbi `main()` funktsiooni:
    ```python
    if __name__ == "__main__":
        main()
    ```

## Programmi loogika ülevaade

### Põhivoog:
1. Programm loeb raamatud failist ja loob need raamatud raamatukokku
2. Kuvab kõik saadaolevad raamatud
3. Küsib kasutajalt raamatu pealkirja
4. Proovib leida, kas see kasutaja poolt soovitud raamat on raamatukogus
6. Kui leitakse raamat, küsib kasutajalt kinnitust
7. Laenutab raamatu ja kuvab uuendatud raamatute nimekirja
8. Küsib, kas kasutaja soovib jätkata
9. Kordub samm 3-st kuni kasutaja lõpetab

### Eriolukordade käsitlus:
- **Raamat juba laenutatud:** Kuvatakse teade ja laenutatud raamatud
- **Raamatut ei leitud:** Kuvatakse veateade
- **Faili lugemise viga:** Kuvatakse veateade ja tagastatakse tühi list

### Väljundi näide 1: Raamatukogu laenutamine
```
Raamatukogus olevad raamatud:
Tõde ja õigus I, A. H. Tammsaare, 453, romaan
Sherlock Holmesi seiklused, A. C. Doyle, 233, detektiiv
Läänerindel muutuseta, E. M. Remarque, 310, romaan
Punamütsike, Charles Perrault, 17, muinasjutt
Eesriie, Agatha Christie, 98, detektiiv
Suur Gatsby, F. Scott Fitzgerald, 188, romaan

Sisesta raamatu pealkiri, mida sa laenutada soovid: eEsrIIe
Raamat Eesriie edukalt laenutatud!

Raamatukogus olevad raamatud:
Tõde ja õigus I, A. H. Tammsaare, 453, romaan
Sherlock Holmesi seiklused, A. C. Doyle, 233, detektiiv
Läänerindel muutuseta, E. M. Remarque, 310, romaan
Punamütsike, Charles Perrault, 17, muinasjutt
Suur Gatsby, F. Scott Fitzgerald, 188, romaan

Kas soovid veel raamatuid laenutada? (jah/ei/minu): minu

Sinu laenutatud raamatud (1):
Eesriie, Agatha Christie, 98, detektiiv

Kas soovid veel raamatuid laenutada? (jah/ei/minu): jah

Sisesta raamatu pealkiri, mida sa laenutada soovid: SUUR GATSBY
Raamat Suur Gatsby edukalt laenutatud!

Raamatukogus olevad raamatud:
Tõde ja õigus I, A. H. Tammsaare, 453, romaan
Sherlock Holmesi seiklused, A. C. Doyle, 233, detektiiv
Läänerindel muutuseta, E. M. Remarque, 310, romaan
Punamütsike, Charles Perrault, 17, muinasjutt

Kas soovid veel raamatuid laenutada? (jah/ei/minu): minu

Sinu laenutatud raamatud (2):
Eesriie, Agatha Christie, 98, detektiiv
Suur Gatsby, F. Scott Fitzgerald, 188, romaan

Kas soovid veel raamatuid laenutada? (jah/ei/minu): ei

Aitäh raamatukogu külastamast!

Sinu laenutatud raamatud (2):
Eesriie, Agatha Christie, 98, detektiiv
Suur Gatsby, F. Scott Fitzgerald, 188, romaan
```

### Väljundi näide 2: Raamatukogus pole sobivat raamatut
```
Raamatukogus olevad raamatud:
Tõde ja õigus I, A. H. Tammsaare, 453, romaan
Sherlock Holmesi seiklused, A. C. Doyle, 233, detektiiv
Läänerindel muutuseta, E. M. Remarque, 310, romaan
Punamütsike, Charles Perrault, 17, muinasjutt
Eesriie, Agatha Christie, 98, detektiiv
Suur Gatsby, F. Scott Fitzgerald, 188, romaan

Sisesta raamatu pealkiri, mida sa laenutada soovid: Muumid
Ei leidnud sellist raamatut

Kas soovid veel raamatuid laenutada? (jah/ei/minu): minu

Sul pole veel ühtegi raamatut laenutatud.

Kas soovid veel raamatuid laenutada? (jah/ei/minu): jah

Sisesta raamatu pealkiri, mida sa laenutada soovid: tode ja oigus
Ei leidnud sellist raamatut

Kas soovid veel raamatuid laenutada? (jah/ei/minu): ei

Aitäh raamatukogu külastamast!

Sul pole veel ühtegi raamatut laenutatud.
```

### Väljundi näide 3: Programm lõppeb kohe
```
Raamatukogu laadimine ebaõnnestus või on tühi. Programm lõppeb.
```
---
