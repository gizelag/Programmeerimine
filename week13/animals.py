from abc import ABC, abstractmethod
kuni 85

# Week 15 – Kontrolltöö 2, grupp 1

## Ülesanded

### Seadistamine

1. Loo kaust/directory nimega `week15_kt2_grupp1`
2. Sinna kausta loo kõik selle kontrolltöö ülesanded
3. Lae Moodlist alla kõik vajalik `.csv` fail, need leiate Moodlist: `Nädal 15 - Kontrolltöö 2` -> `Kontrolltöö 2, grupp 1 - Praktiline osa, failid`
4. Sinna kausta pane:
    1. Allalaetud `.csv` fail
    2. Sinu loodud koodid
5. Peale lõpetamist lae kõik vajalikud failid GitLabi

**PS! Enda koode saab hakata testima alates `15:25-15:45`**

---

## Hindamiskriteeriumid

1. Kõik ülesanded peavad tehtud olema vastavalt juhendile
2. Kood peab olema kommenteeritud
3. Koodi stiil peab olema puhas ja loetav
4. Vigade käsitlus peab olema implementeeritud
5. Koodi käivitamine käib läbi `main()` funktsiooni kaudu
6. Oma lahendus peab olema esitatud kell 15:45

---

## Ülesanne 1: Rekursioon, listi pööramine

**Failinimi:** `reverse_list.py`

### Eesmärk
Koostada rekursioone funktsioon, mis pöörab listi tagurpidi. Näiteks:
```python
[1, 2, 3] -> [3, 2, 1]
[5] -> [5]
[] -> []
[0, 2, 4, 6, 8, 10] -> [10, 8, 6, 4, 2, 0]
```

### Nõuded

1. Loo funktsioon `reverse_list(sisend_list)`:
    - **Parameeter:**
        - sisend_list (list): List, mille elemendid pööratakse vastupidisesse järjekorda
    - **Tagastab:**
        - list: Uus list, kus elemendid on vastupidises järjekorras
    - **Kirjeldus:**
        - Funktsioon pöörab listi elemendid rekursiivselt vastupidisesse järjekorda:
            - Kui sisend ei ole `list`, tekita `TypeError` koos veateadega
            - Loo sobiv rekursiooni baas
            - Loo sobiv rekursiooni samm

2. Loo funktsioon `main()`:
    - Testi oma funktsiooni allpool toodud andmetega
    - Kuva tulemus

3. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Andmed ja väljund
```python
[1, 2, 3]                   # -> [3, 2, 1]
[]                          # -> []
[5]                         # -> [5]
[0, 2, 4, 6, 8, 10]         # -> [10, 8, 6, 4, 2, 0]
1                           # TypeError: Sisend pole list, on hoopis: <class 'int'>
list                        # TypeError: Sisend pole list, on hoopis: <class 'type'>
["t", "e", "r", "e"]        # ['e', 'r', 'e', 't']
[None, 3.0, 'kaks', 1]      # [1, 'kaks', 3.0, None]
```

---

## Ülesanne 2: Toidukohtade haldussüsteem

### Kirjeldus:

Loo toidukohtade haldussüsteem, mis kasutab pärimist ja polümorfismi erinevate toidukohtade tüüpide haldamiseks. Süsteem peab suutma hallata restorane, kohvikuid ja kiirtoidukohti ning nende spetsiifilisi omadusi.

**Failinimi:** `food_places.py`

### Nõuded:

#### Vanemklass: FoodPlace

1. Loo vanemklass `FoodPlace` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - `place_type` (str): Toidukoha tüüp, mille iga alamklass peab üle kirjutama. Alamklass kirjutab selle üle väärtusega: `restaurant`/`cafe`/`fastfood`
    - **Parameetrid:**
        - `name` (str): Toidukoha nimi
        - `address` (str): Toidukoha aadress
        - `opening_time` (str): Avamise aeg formaadis "HH:MM"
        - `closing_time` (str): Sulgemise aeg formaadis "HH:MM"
        - `avg_meal_price` (float): Keskmine einehind eurodes
        - `rating` (float): Hinnang (0.0-5.0)
        - `seating_capacity` (int): Istekohti
        - `has_delivery` (bool): Kas pakub toidu kojuvedu
    - **Kirjeldus:**
        - Kasuta staatilist meetodit `is_valid_time()`, et kontrollida, kas avamise ja sulgemise aeg on õiges formaadis:
            - Kui aeg ei ole korrektne, tõsta `ValueError` ja kuva sobiv teade, näiteks: `Toidukoha {name} avamise/sulgemise aeg peab olema formaadis HH:MM! Saadud: {time}`
        - Kasuta staatilist meetodit `is_valid_rating()`, et kontrollida, kas hinnang on vahemikus 0.0-5.0:
            - Kui hinnang ei ole korrektne, tõsta `ValueError` ja kuva sobiv teade, näiteks: `Toidukoha {name} hinnang peab olema 0.0-5.0 vahel! Saadud: {rating}`
        - Loo atribuudid kõigile parameetritele

2. Loo staatiline meetod `is_valid_time(time_str)`:
    - **Parameeter:**
        - `time_str` (str): Kontrollitav aeg
    - **Tagastab:**
        - bool: True kui aeg on õiges formaadis
    - **Kirjeldus:**
        - Kontrolli, kas `time_str` on sobivat tüüpi
        - Kontrolli, kas `time_str` on formaadis `"HH:MM"` (näiteks `len()` või `.split(....)`)
        - Kontrolli, kas tunnid on vahemikus `00-23` ja minutid `00-59`
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

3. Loo staatiline meetod `is_valid_rating(rating)`:
    - **Parameeter:**
        - `rating` (float): Kontrollitav hinnang
    - **Tagastab:**
        - bool: True kui hinnang on sobiv
    - **Kirjeldus:**
        - Kontrolli, kas `rating` on sobivat tüüpi
        - Kontrolli, kas `rating` on vahemikus 0.0 kuni 5.0 (kaasa arvatud)
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

4. Loo abstraktne meetod `calculate_meal_price(meal_type, hour)`:
    - **Parameeter:**
        - `meal_type` (str): Einetüüp: `"breakfast"`/`"lunch"`/`"dinner"`
        - `hour` (int): Kellaaeg vahemikus 0-23
    - **Tagastab:**
        - float: Arvutatud einehind koos ajapõhise korrektsiooniga, ümardatuna kahe komakohani
    - **Kirjeldus:**
        - See on abstraktne meetod

5. Loo meetod `get_opening_hours()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: Lahtiolekuajad
    - **Kirjeldus:**
        - Tagasta string kujul: `{opening_time} - {closing_time}`
            - Näiteks: `"12:00 - 23:00"`

6. Loo meetod `__repr__()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab toidukoha infot
    - **Kirjeldus:**
        - Tagasta tekst, kus on kirjas toidukoha põhiinfo
        - Tagastatud tekst on kujul:
            ```python
            Type: {place_type}
            Name: {name}
            Address: {address}
            Opening hours: {opening_time} - {closing_time}
            Average meal price: {avg_meal_price}€
            Rating: {rating}/5.0
            Seating capacity: {seating_capacity}
            Delivery: {`"Yes"` kui väärtus on `True` ning `"No"` kui `False`}
            ```

---

#### Alamklass: Restaurant

1. Loo alamklass `Restaurant` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `place_type` üle väärtusega `"Restaurant"`
    - **Parameetrid:**
        - Kõik `FoodPlace` parameetrid
        - `michelin_stars` (int): Michelin tärnide arv (0-3)
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `FoodPlace`
        - Kutsu välja vanemklassi konstruktor
        - Loo uued atribuudid restoranile spetsiifilistele parameetritele
        - Kasuta staatilist meetodit `is_valid_michelin_stars()`, et kontrollida Michelin tärnide arvu:
            - Kui ei ole korrektne, tõsta `ValueError`

2. Loo staatiline meetod `is_valid_michelin_stars(stars)`:
    - **Parameeter:**
        - `stars` (int): Michelin tärnide arv
    - **Tagastab:**
        - bool: True kui aeg tärnide arv on sobiv
    - **Kirjeldus:**
        - Kontrolli, kas `stars` on sobivat tüüpi
        - Kontrolli, kas `stars` on vahemikus 0-3 (kaasa arvatud)
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

3. Kirjuta meetod `calculate_meal_price(meal_type, hour)` üle:
    - **Parameeter:**
        - `meal_type` (str): Einetüüp: `"breakfast"`/`"lunch"`/`"dinner"`
        - `hour` (int): Kellaaeg vahemikus 0-23
    - **Tagastab:**
        - float: Arvutatud einehind koos ajapõhise korrektsiooniga, ümardatuna kahe komakohani
    - **Kirjeldus:**
        - Arvuta baas einehinnad järgmise loogika järgi:
            - `breakfast: avg_meal_price * 0.7`
            - `lunch: avg_meal_price * 0.8`
            - `dinner: avg_meal_price * 1.2`
        - Rakenda ajapõhist soodustust baashindadele (vahet ei ole kas `breakfast`, `lunch` või `dinner` ning kõik kellaajad on kaasaarvatud)
            - Hommikune rush (9:00 - 11:00): 15% odavam baashinnast
            - Happy hour (12:00-14:00): 20% odavam baashinnast
        - Lisa Michelin tärnide boonushind:
            - Iga tärni kohta lisa 15€ lõpphinnale
        - Tagasta arvutatud hind ümardatuna kahe komakohani

4. Loo klassi meetod `read_from_csv_row(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik CSV rea andmetega, kus:
            - Võtmed on CSV päise veerunimed, näiteks: `"name"`, `"address"`, `"opening_time"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - Restaurant: Uus objekti instants, mis on loodud CSV rea andmetest
    - **Kirjeldus:**
        -  Loe `row_dict`-st välja `type` väärtus
        - Teisenda CSV rea andmed õigesse tüüpi:
            - `name` → string
            - `address` → string
            - `address` → string
            - `avg_meal_price` → float
            - `rating` → float
            - `seating_capacity` → int
            - `has_delivery` → bool
            - `michelin_stars` → int
        - Tagastab objekti parameetrid

5. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab restorani infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod:
            - Lisa sinna: `Michelin stars: {michelin_stars}`
        - Tagasta string, mis sisaldab restorani infot

---

#### Alamklass: Cafe

1. Loo alamklass `Cafe` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `place_type` üle väärtusega `"Cafe"`
    - **Parameetrid:**
        - Kõik `FoodPlace` parameetrid
        - `has_wifi` (bool): Kas on WiFi
        - `coffee_types` (list): Kohviliigid listina, näiteks `["Espresso", "Latte", "Cappuccino", "Americano"]`
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `FoodPlace`
        - Kutsu välja vanemklassi konstruktor
        - Loo uued atribuudid kohvikule spetsiifilistele parameetritele
        - Teisenda `coffee_types` string listi

2. Kirjuta meetod `calculate_meal_price(meal_type, hour)` üle:
    - **Parameeter:**
        - `meal_type` (str): Einetüüp: `"breakfast"`/`"lunch"`/`"dinner"`
        - `hour` (int): Kellaaeg vahemikus 0-23
    - **Tagastab:**
        - float: Arvutatud einehind koos ajapõhise korrektsiooniga, ümardatuna kahe komakohani
    - **Kirjeldus:**
        - Arvuta baas einehinnad järgmise loogika järgi:
            - `breakfast: avg_meal_price * 0.6`
            - `lunch: avg_meal_price * 0.7`
            - `dinner: avg_meal_price * 1.0`
        - Rakenda ajapõhist soodustust baashindadele (vahet ei ole kas `breakfast`, `lunch` või `dinner` ning kõik kellaajad on kaasaarvatud)
            - Hommikune rush (8:00 - 11:00): 15% odavam baashinnast
            - Happy hour (12:00-15:00): 10% odavam baashinnast
            - Hommikused saiakesed (Alates 22:00): 35% odavam baashinnast
        - Tagasta arvutatud hind ümardatuna kahe komakohani

3. Loo klassi meetod `read_from_csv_row(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik CSV rea andmetega, kus:
            - Võtmed on CSV päise veerunimed, näiteks: `"name"`, `"address"`, `"opening_time"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - Cafe: Uus objekti instants, mis on loodud CSV rea andmetest
    - **Kirjeldus:**
        -  Loe `row_dict`-st välja `type` väärtus
        - Teisenda CSV rea andmed õigesse tüüpi:
            - `name` → string
            - `address` → string
            - `address` → string
            - `avg_meal_price` → float
            - `rating` → float
            - `seating_capacity` → int
            - `has_delivery` → bool
            - `has_wifi` → bool
            - `coffee_types` → list (CSV-s on need semikooloniga eraldatud stringina, näiteks: `"Espresso;Latte;Cappuccino"` → teisenda listiks)
        - Tagastab objekti parameetrid

4. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab kohviku infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod:
            - Lisa sinna:
                - Kui WiFi on saadaval: `"Cozy cafe with WiFi and {kohviliikide_arv} types of coffee"`
                - Kui WiFi ei ole saadaval: `"Cozy cafe with {kohviliikide_arv} types of coffee"`
        - Tagasta string, mis sisaldab kohviku infot
---

#### Alamklass: FastFood

1. Loo alamklass `FastFood` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `place_type` üle väärtusega `"Fast Food"`
    - **Parameetrid:**
        - Kõik `FoodPlace` parameetrid
        - `parking_spots` (int): Parkimiskohtade arv
        - `drive_through` (bool): Kas on auto läbisõit ehk kas on drive-through võimalus
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `FoodPlace`
        - Kutsu välja vanemklassi konstruktor
        - Loo uued atribuudid kiirtoidukohale spetsiifilistele parameetritele

2. Kirjuta meetod `calculate_meal_price(meal_type, hour)` üle:
    - **Parameeter:**
        - `meal_type` (str): Einetüüp: `"breakfast"`/`"lunch"`/`"dinner"`
        - `hour` (int): Kellaaeg vahemikus 0-23
    - **Tagastab:**
        - float: Arvutatud einehind ümardatuna kahe komakohani
    - **Kirjeldus:**
        - Arvuta baas einehinnad järgmise loogika järgi:
            - `breakfast: avg_meal_price * 0.4`
            - `lunch: avg_meal_price * 0.6`
            - `dinner: avg_meal_price * 1.0`
        - Rakenda ajapõhist soodustust baashindadele (vahet ei ole kas `breakfast`, `lunch` või `dinner` ning kõik kellaajad on kaasaarvatud)
            - Hommikune rush (9:00 - 11:00): 10% odavam baashinnast
            - Happy hour (12:00-14:00): 5% odavam baashinnast
            - Tänane kebab vaja ära müüa (Alates 21:00): 25% odavam baashinnast
        - Tagasta arvutatud hind ümardatuna kahe komakohani

3. Loo klassi meetod `read_from_csv_row(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik CSV rea andmetega, kus:
            - Võtmed on CSV päise veerunimed, näiteks: `"name"`, `"address"`, `"opening_time"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - FastFood: Uus objekti instants, mis on loodud CSV rea andmetest
    - **Kirjeldus:**
        -  Loe `row_dict`-st välja `type` väärtus
        - Teisenda CSV rea andmed õigesse tüüpi:
            - `name` → string
            - `address` → string
            - `address` → string
            - `avg_meal_price` → float
            - `rating` → float
            - `seating_capacity` → int
            - `has_delivery` → bool
            - `parking_spots` → int
        - Tagastab objekti parameetrid

4. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab kiirtoidu restorani infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod
        - Lisa sinna:
            - Kui on drive-through JA parkimiskohti on rohkem kui 30 (kaasa arvatud): `"Fast-food restaurant with drive-through and large parking ({parking_spots} spots)"`
            - Kui on drive-through KUID parkimiskohti vähem kui 30: `"Fast-food restaurant with drive-through and {parking_spots} parking spots"`
            - Kui ei ole drive-through'i: `"Fast-food restaurant without drive-through"`
        - Tagasta string, mis sisaldab kiirtoidu restorani infot

---

#### Põhiprogramm

**Failinimi:** `main.py`

### Nõuded:

1. Loo funktsioon `load_food_places_from_csv(filename)`:
    - **Parameeter:**
        - `filename` (str): CSV faili nimi
    - **Tagastab:**
        - list: Nimekiri toidukohtade objektidest
    - **Kirjeldus:**
        - Kasuta `try-except` plokki vigade käsitlemiseks:
            - Ava ja loe CSV fail:
                - Kasuta `csv.DictReader()` meetodit, mis:
                    - Loeb automaatselt päiserida (esimene rida)
                    - Teisendab iga järgneva rea sõnastikuks, kus:
                        - Võtmed = päise veerunimed
                        - Väärtused = rea lahtri väärtused
                - Käi läbi kõik read:
                    - Loe rea tüüp, csv failis `type`
                    - Eemalda tühikud ja tee väiketähtedeks
                    - Määra tüübi järgi sobiv klass:
                        - Vastava tüübi järgi kasuta klassimeetodit `read_from_csv_row(row_dict)`
                        - Kui tundmatu tüüp: Kuva hoiatus ja jätka järgmise reaga
        - Vigade käsitlus:
            - `FileNotFoundError`: Kui faili ei leita, kuva veateade
            - `Exception`: Kõik muud vead, kuva üldine veateade
        - Tagasta toidukohtade list, mis sisaldab toidukohtade objekte (ka siis kui on tühi vigade korral)

2. Loo funktsioon `main()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - Puudub
    - **Kirjeldus:**
        - Lae toidukohad CSV failist `data_food_places.csv` kasutades sobivat funktsiooni
        - Kontrolli ega toidukohtade objektide list pole tühi:
            - Kui on tühi, siis kuva veateade ja lõpeta funktsioon
        - Kuva kõigi toidukohtade info
        - Näita polümorfismi:
            - Vali üks restoran, üks kohvik ja üks kiirtoidukoht
            - Kasuta erinevaid kellaaegu ning kuva nende hommikusöögi, lõunasöögi ja õhtusöögi hinnad

3. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()

---

## Programmi väljund: Söögikohtade info kuvamine

```python
Type: Restaurant
Name: La Terrasse
Address: Viru väljak 4
Opening hours: 12:00 - 23:00
Average meal price: 45.5
Rating: 4.8
Seating capacity 80
Delivery: Yes
Michelin stars: 2

Type: Restaurant
Name: Rataskaevu 16
Address: Rataskaevu 16
Opening hours: 12:00 - 22:30
Average meal price: 38.0
Rating: 4.6
Seating capacity 60
Delivery: No
Michelin stars: 1

Type: Restaurant
Name: Tchaikovsky
Address: Vene 9
Opening hours: 18:00 - 23:00
Average meal price: 55.0
Rating: 4.9
Seating capacity 50
Delivery: No
Michelin stars: 0

Type: Cafe
Name: Caffeine
Address: Narva mnt 5
Opening hours: 08:00 - 20:00
Average meal price: 8.5
Rating: 4.3
Seating capacity 35
Delivery: Yes
Cozy cafe with WiFi and 4 types of coffee
Coffees are: ['Espresso', 'Latte', 'Cappuccino', 'Americano']

Type: Cafe
Name: Rukis
Address: Roseni 7
Opening hours: 07:30 - 19:00
Average meal price: 9.2
Rating: 4.5
Seating capacity 25
Delivery: No
Cozy cafe with WiFi and 3 types of coffee
Coffees are: ['Espresso', 'Flat White', 'Pour Over']

Type: Cafe
Name: Pierre Chocolaterie
Address: Vene 6
Opening hours: 10:00 - 21:00
Average meal price: 12.0
Rating: 4.7
Seating capacity 40
Delivery: Yes
Cozy cafe with WiFi and 3 types of coffee
Coffees are: ['Espresso', 'Mocha', 'Hot chocolate']

Type: Fast Food
Name: McDonald's Viru
Address: Viru väljak 2
Opening hours: 07:00 - 23:00
Average meal price: 7.5
Rating: 3.8
Seating capacity 120
Delivery: Yes
Fast-food restaurant without drive-through

Type: Fast Food
Name: Hesburger Kaubamaja
Address: Gonsiori 2
Opening hours: 09:00 - 22:00
Average meal price: 6.8
Rating: 3.9
Seating capacity 80
Delivery: Yes
Fast-food restaurant with drive-through and 20 parking spots

Type: Fast Food
Name: KFC Kristiine
Address: Endla 45
Opening hours: 10:00 - 22:00
Average meal price: 8.2
Rating: 4.0
Seating capacity 100
Delivery: Yes
Fast-food restaurant with drive-through and large parking (500) spots

Type: Fast Food
Name: Subway Ülemiste
Address: Suur-Sõjamäe 4
Opening hours: 08:00 - 21:00
Average meal price: 6.5
Rating: 4.1
Seating capacity 50
Delivery: No
Fast-food restaurant without drive-through
```

---

## Programmi väljund: Polümorfism -> Hindade arvutamine

**PS! Polümorfismi väljund ei pea täpselt selline olema nagu siin. Ma tegin meelega sellise väljundi, et te näeksite paremini.**

```python
La Terrasse (Restaurant)
  HOMMIKUSÖÖK:
  ---------
    Kell 08:00 - 61.85€
    Kell 09:00 - 57.07€
    Kell 10:00 - 57.07€
    Kell 11:00 - 57.07€
    Kell 12:00 - 55.48€
    Kell 13:00 - 55.48€
    Kell 14:00 - 55.48€
    Kell 15:00 - 61.85€
    Kell 18:00 - 61.85€
    Kell 21:00 - 61.85€
    Kell 22:00 - 61.85€
    Kell 23:00 - 61.85€

  LÕUNA:
  ---------
    Kell 08:00 - 66.4€
    Kell 09:00 - 60.94€
    Kell 10:00 - 60.94€
    Kell 11:00 - 60.94€
    Kell 12:00 - 59.12€
    Kell 13:00 - 59.12€
    Kell 14:00 - 59.12€
    Kell 15:00 - 66.4€
    Kell 18:00 - 66.4€
    Kell 21:00 - 66.4€
    Kell 22:00 - 66.4€
    Kell 23:00 - 66.4€

  ÕHTUSÖÖK:
  ---------
    Kell 08:00 - 84.6€
    Kell 09:00 - 76.41€
    Kell 10:00 - 76.41€
    Kell 11:00 - 76.41€
    Kell 12:00 - 73.68€
    Kell 13:00 - 73.68€
    Kell 14:00 - 73.68€
    Kell 15:00 - 84.6€
    Kell 18:00 - 84.6€
    Kell 21:00 - 84.6€
    Kell 22:00 - 84.6€
    Kell 23:00 - 84.6€


Caffeine (Cafe)
  HOMMIKUSÖÖK:
  ---------
    Kell 08:00 - 4.33€
    Kell 09:00 - 4.33€
    Kell 10:00 - 4.33€
    Kell 11:00 - 4.33€
    Kell 12:00 - 4.59€
    Kell 13:00 - 4.59€
    Kell 14:00 - 4.59€
    Kell 15:00 - 4.59€
    Kell 18:00 - 5.1€
    Kell 21:00 - 5.1€
    Kell 22:00 - 3.31€
    Kell 23:00 - 3.31€

  LÕUNA:
  ---------
    Kell 08:00 - 5.06€
    Kell 09:00 - 5.06€
    Kell 10:00 - 5.06€
    Kell 11:00 - 5.06€
    Kell 12:00 - 5.35€
    Kell 13:00 - 5.35€
    Kell 14:00 - 5.35€
    Kell 15:00 - 5.35€
    Kell 18:00 - 5.95€
    Kell 21:00 - 5.95€
    Kell 22:00 - 3.87€
    Kell 23:00 - 3.87€

  ÕHTUSÖÖK:
  ---------
    Kell 08:00 - 7.22€
    Kell 09:00 - 7.22€
    Kell 10:00 - 7.22€
    Kell 11:00 - 7.22€
    Kell 12:00 - 7.65€
    Kell 13:00 - 7.65€
    Kell 14:00 - 7.65€
    Kell 15:00 - 7.65€
    Kell 18:00 - 8.5€
    Kell 21:00 - 8.5€
    Kell 22:00 - 5.53€
    Kell 23:00 - 5.53€


McDonald's Viru (Fast Food)
  HOMMIKUSÖÖK:
  ---------
    Kell 08:00 - 3.0€
    Kell 09:00 - 2.7€
    Kell 10:00 - 2.7€
    Kell 11:00 - 2.7€
    Kell 12:00 - 2.85€
    Kell 13:00 - 2.85€
    Kell 14:00 - 2.85€
    Kell 15:00 - 3.0€
    Kell 18:00 - 3.0€
    Kell 21:00 - 2.25€
    Kell 22:00 - 2.25€
    Kell 23:00 - 2.25€

  LÕUNA:
  ---------
    Kell 08:00 - 4.5€
    Kell 09:00 - 4.05€
    Kell 10:00 - 4.05€
    Kell 11:00 - 4.05€
    Kell 12:00 - 4.27€
    Kell 13:00 - 4.27€
    Kell 14:00 - 4.27€
    Kell 15:00 - 4.5€
    Kell 18:00 - 4.5€
    Kell 21:00 - 3.38€
    Kell 22:00 - 3.38€
    Kell 23:00 - 3.38€

  ÕHTUSÖÖK:
  ---------
    Kell 08:00 - 7.5€
    Kell 09:00 - 6.75€
    Kell 10:00 - 6.75€
    Kell 11:00 - 6.75€
    Kell 12:00 - 7.12€
    Kell 13:00 - 7.12€
    Kell 14:00 - 7.12€
    Kell 15:00 - 7.5€
    Kell 18:00 - 7.5€
    Kell 21:00 - 5.62€
    Kell 22:00 - 5.62€
    Kell 23:00 - 5.62€
```

---
esimene
"""import csv
from food_places import Restaurant, Cafe, FastFood


def load_food_places_from_csv(filename):
    """
    Laeb toidukohad CSV failist.
    Tagastab list objektidest.
    """
    food_places = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                type_str = row['type'].strip().lower()
                try:
                    # Vali tüüp ja loome objekti
                    if type_str == "restaurant":
                        obj = Restaurant.read_from_csv_row(row)
                    elif type_str == "cafe":
                        obj = Cafe.read_from_csv_row(row)
                    elif type_str == "fastfood":
                        obj = FastFood.read_from_csv_row(row)
                    else:
                        print(f"Hoiatus: tundmatu tüüp {row['type']}, vahele jäetud.")
                        continue
                    food_places.append(obj)
                except Exception as e:
                    # Vigade käsitlemine rea lugemisel
                    print(f"Viga rea lugemisel: {e}")
    except FileNotFoundError:
        print(f"Faili {filename} ei leitud!")
    except Exception as e:
        print(f"Tekkis üldine viga: {e}")

    return food_places


def main():
    # Laeme andmed CSV-st
    places = load_food_places_from_csv("data_food_places.csv")

    if not places:
        print("Toidukohti ei leitud!")
        return

    # Kuvame kõikide toidukohtade info
    print("=== Kõik toidukohad ===")
    for place in places:
        print(place)
        print("-" * 40)

    # Näitame polümorfismi
    print("\n=== Näide polümorfismist ===")
    restaurant = next((p for p in places if isinstance(p, Restaurant)), None)
    cafe = next((p for p in places if isinstance(p, Cafe)), None)
    fastfood = next((p for p in places if isinstance(p, FastFood)), None)

    if restaurant:
        print(f"\n{restaurant.name} eine hinnad:")
        for hour in [10, 13, 19]:  # hommik, lõuna, õhtu
            print(f"{hour}:00 -> Breakfast: {restaurant.calculate_meal_price('breakfast', hour)}€, "
                  f"Lunch: {restaurant.calculate_meal_price('lunch', hour)}€, "
                  f"Dinner: {restaurant.calculate_meal_price('dinner', hour)}€")

    if cafe:
        print(f"\n{cafe.name} eine hinnad:")
        for hour in [9, 14, 22]:
            print(f"{hour}:00 -> Breakfast: {cafe.calculate_meal_price('breakfast', hour)}€, "
                  f"Lunch: {cafe.calculate_meal_price('lunch', hour)}€, "
                  f"Dinner: {cafe.calculate_meal_price('dinner', hour)}€")

    if fastfood:
        print(f"\n{fastfood.name} eine hinnad:")
        for hour in [10, 13, 21]:
            print(f"{hour}:00 -> Breakfast: {fastfood.calculate_meal_price('breakfast', hour)}€, "
                  f"Lunch: {fastfood.calculate_meal_price('lunch', hour)}€, "
                  f"Dinner: {fastfood.calculate_meal_price('dinner', hour)}€")


if __name__ == "__main__":
    main()"""

reversiime
"""def reverse_list(sisend_list):
    # Kontrolli, kas sisend on list
    if not isinstance(sisend_list, list):
        raise TypeError(f"Sisend pole list, on hoopis: {type(sisend_list)}")

    # Baasjuht: tühi või ühe elemendiga list
    if len(sisend_list) <= 1:
        return sisend_list

    # Rekursiivne samm: viimase elemendi lisamine pööratud ülejäänule
    return [sisend_list[-1]] + reverse_list(sisend_list[:-1])


def main():
    # Testandmed
    test_data = [
        [1, 2, 3],
        [],
        [5],
        [0, 2, 4, 6, 8, 10],
        1,  # Vale tüüp
        list,  # Vale tüüp
        ["t", "e", "r", "e"],
        [None, 3.0, 'kaks', 1]
    ]

    for data in test_data:
        try:
            # Kuvame originaali ja pööratud listi
            print(f"{data} -> {reverse_list(data)}")
        except TypeError as e:
            # Kui sisend pole list, kuvame veateate
            print(e)


if __name__ == "__main__":
    main() """

kolmas
"""from abc import ABC, abstractmethod

# ---------------- Vanemklass ----------------
class FoodPlace(ABC):
    place_type = None  # Klassimuutuja: tüüp (Restaurant/Cafe/Fast Food)

    def __init__(self, name, address, opening_time, closing_time, avg_meal_price,
                 rating, seating_capacity, has_delivery):
        # Kontrollime avamise ja sulgemise aega
        if not self.is_valid_time(opening_time):
            raise ValueError(f"{name} avamise aeg vigane: {opening_time}")
        if not self.is_valid_time(closing_time):
            raise ValueError(f"{name} sulgemise aeg vigane: {closing_time}")
        # Kontrollime hinnangut 0-5
        if not self.is_valid_rating(rating):
            raise ValueError(f"{name} hinnang vigane: {rating}")

        # Salvesta atribuudid
        self.name = name
        self.address = address
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.avg_meal_price = avg_meal_price
        self.rating = rating
        self.seating_capacity = seating_capacity
        self.has_delivery = has_delivery

    @staticmethod
    def is_valid_time(time_str):
        # Kontrollime HH:MM formaati
        if not isinstance(time_str, str):
            return False
        parts = time_str.split(":")
        if len(parts) != 2:
            return False
        try:
            hour = int(parts[0])
            minute = int(parts[1])
        except ValueError:
            return False
        return 0 <= hour <= 23 and 0 <= minute <= 59

    @staticmethod
    def is_valid_rating(rating):
        # Kontrollime, et hinnang oleks 0.0-5.0
        return isinstance(rating, (int, float)) and 0.0 <= rating <= 5.0

    @abstractmethod
    def calculate_meal_price(self, meal_type, hour):
        # Abstraktne meetod, arvutab eine hinna
        pass

    def get_opening_hours(self):
        # Tagastab avamisajad
        return f"{self.opening_time} - {self.closing_time}"

    def __repr__(self):
        # Põhiteave toidukoha kohta
        delivery = "Yes" if self.has_delivery else "No"
        return (f"Type: {self.place_type}\n"
                f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"Opening hours: {self.opening_time} - {self.closing_time}\n"
                f"Average meal price: {self.avg_meal_price}€\n"
                f"Rating: {self.rating}/5.0\n"
                f"Seating capacity: {self.seating_capacity}\n"
                f"Delivery: {delivery}")

# ---------------- Restaurant ----------------
class Restaurant(FoodPlace):
    place_type = "Restaurant"

    def __init__(self, name, address, opening_time, closing_time, avg_meal_price,
                 rating, seating_capacity, has_delivery, michelin_stars):
        super().__init__(name, address, opening_time, closing_time, avg_meal_price,
                         rating, seating_capacity, has_delivery)
        # Kontrollime Michelin tärne 0-3
        if not self.is_valid_michelin_stars(michelin_stars):
            raise ValueError(f"Michelin tärnid 0-3! Saadud: {michelin_stars}")
        self.michelin_stars = michelin_stars

    @staticmethod
    def is_valid_michelin_stars(stars):
        # Kontroll tärnide arv 0-3
        return isinstance(stars, int) and 0 <= stars <= 3

    def calculate_meal_price(self, meal_type, hour):
        # Baashinnad
        base_prices = {"breakfast": self.avg_meal_price*0.7,
                       "lunch": self.avg_meal_price*0.8,
                       "dinner": self.avg_meal_price*1.2}
        price = base_prices.get(meal_type, self.avg_meal_price)
        # Ajapõhised soodustused
        if 9 <= hour <= 11: price *= 0.85  # hommikune rush
        elif 12 <= hour <= 14: price *= 0.8  # happy hour
        # Michelin tärnid lisatakse
        price += self.michelin_stars * 15
        return round(price, 2)

    @classmethod """
class Animal(ABC):
    animal_type = None

    def __init__(self, name, age:int, gender, weight):

        if not Animal.is_valid_age(age):
            raise ValueError(f"Looma {name} vanus peab olema 0-100 vahel! Saadud: {age}")

        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    @staticmethod
    def is_valid_age(age):
        if not isinstance(age, int):
            return False
        if 100 < age or age < 0:
            return False
        return True

    @classmethod
    def calc_age_in_human_years(cls, age):
        looma_age_dict = {"dog": 7,
                          "cat": 6,
                          "bird": 4,
                          "fish": 2
                          }
        if cls.animal_type in looma_age_dict.keys():
            return age * looma_age_dict[cls.animal_type]

    def eat(self):
        print(f"{self.name} sööb maitsvat toitu")

    def sleep(self):
        print(f"{self.name} magab magusalt")

    def get_human_years(self):
        return self.__class__.calc_age_in_human_years(self.age)

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return (f"\nAnimal name: {self.name}\n"
                f"Age: {self.age} years ({self.get_human_years()} in human years))\n"
                f"Gender: {self.gender}\n"
                f"Weight: {self.weight}kg\n")


class Mammal(Animal):
    def __init__(self, name, age, gender, weight, hair_color):
        super().__init__(name, age, gender, weight)
        self.hair_color = hair_color

    def __repr__(self):
        return super().__repr__() + f"Hair color: {self.hair_color}\n"


class Bird(Animal):
    animal_type = "bird"

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight)
        self.wingspan = wingspan
        self.flying_ability = can_fly

    def __repr__(self):
        tekst = "No"
        if self.flying_ability:
            tekst = "Yes"
        return super().__repr__() + f"Wingspan: {self.wingspan}cm. Can fly:{tekst}\n"


class Fish(Animal):
    animal_type = "fish"

    def __init__(self, name, age, gender, weight, max_depth, water_type):
        super().__init__(name, age, gender, weight)
        self.max_depth = max_depth
        self.water_type = water_type

    def __repr__(self):
        return super().__repr__() + f"Max depth: {self.max_depth}m Water type: {self.water_type}\n"


class Dog(Mammal):
    animal_type = "dog"

    def __init__(self, name, age, gender, weight, hair_color, breed):
        super().__init__(name, age, gender, weight, hair_color)
        self.hair_color = hair_color
        self.breed = breed

    def make_sound(self):
        print(f"\n{self.name} haugub: Auh, AUh, Auh!\n")

    def __repr__(self):
        return super().__repr__() + f"Dog breed: {self.breed}\n"


class Cat(Mammal):
    animal_type = "cat"
    def __init__(self, name, age, gender, weight, hair_color, indoor_cat):
        super().__init__(name, age, gender, weight, hair_color)
        self.hair_color = hair_color
        self.indoor_cat = indoor_cat

    def make_sound(self):
        print (f"{self.name} näugub: Mjäu Mjäu!")

    def __repr__(self):
        tekst = "No"
        if self.indoor_cat:
            tekst = "Yes"
        return super().__repr__() + f"Indoor cat: {tekst}\n"


class Eagle(Bird):

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight, wingspan, can_fly)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} karjub: Kiih Kiih")


class Penguin(Bird):
    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight, wingspan, can_fly)
        self.wingspan = wingspan
        self.can_fly = can_fly

    def make_sound(self):
        print(f"\n{self.name} kvääksub: Kvääk Kvääk\n")


class Shark(Fish):
    def __init__(self, name, age, gender, weight, max_depth, water_type, danger_level):
        super().__init__(name, age, gender, weight, max_depth, water_type)
        self.max_depth = max_depth
        self.water_type = water_type
        if 10 < danger_level or danger_level <=0:
            raise ValueError("Danger level must 0-10!")
        else:
            self.danger_level = danger_level

    def make_sound(self):
        print(f"{self.name} teeb: Mull Mull")#

    def __repr__(self):
        return super().__repr__() + f"Danger level: {self.danger_level}/10\n"