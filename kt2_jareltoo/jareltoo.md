# Kontrolltöö 2, järeltöö

## Seadistamine

1. Loo kaust/directory nimega `kt2_jareltoo`
2. Sinna kausta loo kõik selle kontrolltöö ülesanded
3. Lae Moodlist alla vajalik `.txt` fail, selle leiate Moodlist: `Kontrolltöö 2 praktiline - Järeltöö` -> `Järeltöö - Failid`
4. Sinna kausta pane:
    1. Allalaetud `.txt` fail
    2. Sinu loodud koodid
5. Peale lõpetamist lae kõik vajalikud failid GitLabi
6. Oma lahendus peab olema esitatud kell 11:45

**PS! Enda koode saab hakata testima alates `11:25-11:45`**

---

# Ülesanne 1: Arvu digitite summa (rekursioon)

## Kirjeldus:

Kirjuta rekursiivne funktsioon `digit_sum(n)`, mis leiab ja tagastab täisarvu `n` kõigi digitite summa. Näiteks:
```python
123 -> 6, sest:s
1 + 2 + 3 = 6

9875 -> 29, sest:
9 + 8 + 7 + 5 = 29

1000 -> 1, sest:
1 + 0 + 0 + 0 = 1
```

**Failinimi:** `rekursioon_digit_sum.py`

## Nõuded:

**Vihje:** Mõtle, kuidas saad eraldada viimase digiti (jääk 10-ga jagamisel) ja ülejäänud arvu

1. Loo funktsioon `digit_sum(n)`:
    - **Parameeter:**
        - `n` (int): Täisarv
    - **Tagastab:**
        - int: Arvu digitite summa
    - **Kirjeldus:**
        - Kui sisend ei ole `int`, tekita `TypeError` koos veateadega
        - Kontrolli, et `n` ei ole negatiivne arv:
            - Tekita `ValueError` koos veateatega
        - Loo sobiv rekursiooni baas
        - Loo sobiv rekursiooni samm
        - Tagasta arvu digitite summa

2. Loo funktsioon `main()`:
    - Testi oma funktsiooni allpool toodud andmetega
    - Kuva tulemus

3. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()
    ```

## Andmed ja väljund
```python
digit_sum(0)        # 0
digit_sum(7)        # 7
digit_sum(123)      # 6
digit_sum(9875)     # 29
digit_sum(1000)     # 1
digit_sum(1.09)     # TypeError: Funktsiooni sisend pole `int`, on hoopis: <class 'float'>
digit_sum(-999)     # ValueError: Arv peab olema mittenegatiivne
digit_sum("111")    # TypeError: Funktsiooni sisend pole `int`, on hoopis: <class 'str'>
digit_sum(999)      # 27
```

--- 

# Ülesanne 2: Majutuskohtade haldussüsteem

## Kirjeldus:

Loo majutuskohtade haldussüsteem, mis kasutab pärimist ja polümorfismi erinevate majutuskohtade tüüpide haldamiseks. Süsteem peab suutma hallata hotelle, hosteleid, AirBnB-sid ja campsite'e ning nende spetsiifilisi omadusi.

**Failinimi:** `accommodation.py`

## Nõuded:

### Vanemklass: Accommodation

1. Loo vanemklass `Accommodation` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - `accommodation_type` (str): Majutuskoha tüüp, mille iga alamklass peab üle kirjutama. Alamklass kirjutab selle üle väärtusega: `Hotel`/`AirBnB`/`Campsite`
    - **Parameetrid:**
        - `name` (str): Majutuskoha nimi
        - `address` (str): Majutuskoha aadress
        - `city` (str): Linn
        - `base_price` (float): Baashind öösel eurodes
        - `rating` (float): Hinnang (0.0-5.0)
        - `capacity` (int): Maksimaalne külaliste arv
        - `has_wifi` (bool): Kas pakub WiFi-t
        - `has_parking` (bool): Kas pakub parkimist
        - `has_breakfast` (bool): Kas pakub hommikusööki
        - `check_in_time` (str): Sisseregistreerimise aeg formaadis "HH:MM"
        - `check_out_time` (str): Väljaregistreerimise aeg formaadis "HH:MM"
        - `min_nights` (int): Minimaalne ööde arv
    - **Kirjeldus:**
        - Kasuta staatilist meetodit `is_valid_time()`, et kontrollida, kas sisseregistreerimise ja väljaregistreerimise aeg on õiges formaadis:
            - Kui aeg ei ole korrektne, tõsta `ValueError` ja kuva sobiv teade, näiteks: `Majutuskoha {name} sisseregistreerimise/väljaregistreerimise aeg peab olema formaadis HH:MM! Saadud: {time}`
        - Kasuta staatilist meetodit `is_valid_rating()`, et kontrollida, kas hinnang on vahemikus 0.0-5.0:
            - Kui hinnang ei ole korrektne, tõsta `ValueError` ja kuva sobiv teade, näiteks: `Majutuskoha {name} hinnang peab olema 0.0-5.0 vahel! Saadud: {rating}`
        - Kasuta staatilist meetodit `is_valid_price()`, et kontrollida, kas baashind on positiivne:
            - Kui hind ei ole korrektne, tõsta `ValueError` ja kuva sobiv teade, näiteks: `Majutuskoha {name} baashind peab olema positiivne! Saadud: {base_price}`
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
        - Kontrolli, kas `rating` on vahemikus 0.0 kuni 10.0 (kaasa arvatud)
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

4. Loo staatiline meetod `is_valid_price(price)`:
    - **Parameeter:**
        - `price` (float): Kontrollitav hind
    - **Tagastab:**
        - bool: True kui hind on sobiv
    - **Kirjeldus:**
        - Kontrolli, kas `price` on sobivat tüüpi
        - Kontrolli, kas `price` on suurem kui 0
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

5. Loo abstraktne meetod `calculate_nightly_rate(season, num_guests)`:
    - **Parameeter:**
        - `season` (str): Hooaeg: `"summer"`/`"winter"`/`"spring"`/`"autumn"`
        - `num_guests` (int): Külaliste arv
    - **Tagastab:**
        - float: Arvutatud ööhind vastavalt hooajale ja külaliste arvule, ümardatuna kahe komakohani
    - **Kirjeldus:**
        - See on abstraktne meetod

6. Loo meetod `get_check_in_out_times()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: Sisse- ja väljaregistreerimise ajad
    - **Kirjeldus:**
        - Tagasta string kujul: `Check-in: {check_in_time}, Check-out: {check_out_time}`
            - Näiteks: `"Check-in: 15:00, Check-out: 12:00"`

7. Loo meetod `get_amenities()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - list: Nimekiri mugavustest
    - **Kirjeldus:**
        - Kui `has_wifi` on `True`, lisa listi string: `"WiFi"`
        - Kui `has_parking` on `True`, lisa listi string: `"Parking"`
        - Kui `has_breakfast` on `True`, lisa listi string: `"Breakfast"`
        - Tagasta list, mis sisaldab mugavusi

8. Loo meetod `__repr__()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab majutuskoha infot
    - **Kirjeldus:**
        - Tagasta tekst, kus on kirjas majutuskoha põhiinfo
        - Tagastatud tekst on kujul:
            ```python
            Type: {accommodation_type}
            Name: {name}
            Address: {address}, {city}
            Base price: {base_price}€ per night
            Rating: {rating}/10.0
            Capacity: {capacity} guests
            Minimum nights: {min_nights}
            {get_check_in_out_times()}
            Amenities: {get_amenities() tagastus komaga eraldatuna või "None"}
            ```

---

### Alamklass: Hotel

1. Loo alamklass `Hotel` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `accommodation_type` üle väärtusega `"Hotel"`
    - **Parameetrid:**
        - Kõik `Accommodation` parameetrid
        - `stars` (int): Tärnide arv (1-5)
        - `has_spa` (bool): Kas on SPA
        - `room_service` (bool): Kas on toateenindus
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `Accommodation`
        - Kutsu välja vanemklassi konstruktor
        - Kasuta staatilist meetodit `is_valid_stars()`, et kontrollida tärnide arvu:
            - Kui ei ole korrektne, tõsta `ValueError`
        - Loo uued atribuudid hotellile spetsiifilistele parameetritele

2. Loo staatiline meetod `is_valid_stars(stars)`:
    - **Parameeter:**
        - `stars` (int): Tärnide arv
    - **Tagastab:**
        - bool: True kui tärnide arv on sobiv
    - **Kirjeldus:**
        - Kontrolli, kas `stars` on sobivat tüüpi
        - Kontrolli, kas `stars` on vahemikus 1-5 (kaasa arvatud)
        - Tagasta `True` kui kõik kontrollid läbitud, `False` kui ei

3. Kirjuta meetod `calculate_nightly_rate(season, num_guests)` üle:
    - **Parameeter:**
        - `season` (str): Hooaeg: `"summer"`/`"winter"`/`"spring"`/`"autumn"`
        - `num_guests` (int): Külaliste arv
    - **Tagastab:**
        - float: Arvutatud ööhind ümardatuna kahe komakohani
    - **Kirjeldus:**
        - Rakenda hooajalisust (korrutamisega):
            - `summer`: +50% (korruta 1.5-ga)
            - `winter`: -20% (korruta 0.8-ga)
            - `spring` ja `autumn`: baashind (korruta 1.0-ga)
        - Kontrolli, kas parameeter `season` on sobiv ehk kas läheb kokku hooaegadega:
            - Kui ei ole korrektne, tõsta `ValueError` koos sobiva teatega
        - Lisa tärnide boonushind:
            - Iga tärni kohta lisa 10% algsest baashinnast (mitte hooajalisest hinnast!)
            - Valem: `stars * base_price * 0.1`
        - Lisa külaliste tasu:
            - Standartne on 2 külalist
            - Iga täiendav külalise eest (üle 2) lisa 25€
        - Lisa SPA tasu:
            - Kui hotellis on SPA, siis lisa 15€ hinnale juurde
        - Lisa toateeninduse tasu:
            - Kui hotellis on toateenindus, korruta kogu hind 1.1-ga (+10%)
        - Tagasta arvutatud hind ümardatuna kahe komakohani

4. Loo klassi meetod `get_object_data(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik TXT rea andmetega, kus:
            - Võtmed on TXT päise veerunimed, näiteks: `"name"`, `"address"`, `"city"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - Hotel: Uus objekti instants, mis on loodud TXT rea andmetest
    - **Kirjeldus:**
        - Teisenda TXT rea andmed õigesse tüüpi:
            - `name`: string
            - `address`: string
            - `city`: string
            - `base_price`: float
            - `rating`: float
            - `capacity`: int
            - `has_wifi`: bool
            - `has_parking`: bool
            - `has_breakfast`: bool
            - `check_in_time`: string
            - `check_out_time`: string
            - `min_nights`: int
            - `stars`: int
            - `has_spa`: bool
            - `room_service`:bool
        - Tagasta `Hotel` objekti kõigi parameetritega

5. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab hotelli infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod
        - Lisa sinna:
            - `Stars: {stars}`
            - `Spa: {"Yes" kui has_spa on True, muidu "No"}`
            - `Room service: {"Yes" kui room_service on True, muidu "No"}`
        - Tagasta string, mis sisaldab hotelli infot

---

### Alamklass: AirBnB

1. Loo alamklass `AirBnB` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `accommodation_type` üle väärtusega `"AirBnB"`
    - **Parameetrid:**
        - Kõik `Accommodation` parameetrid
        - `is_entire_place` (bool): Kas on kogu elamine (True) või ainult tuba (False)
        - `host_name` (str): Majutaja nimi
        - `instant_booking` (bool): Kas on instant booking võimalus
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `Accommodation`
        - Kutsu välja vanemklassi konstruktor
        - Loo uued atribuudid AirBnB-le spetsiifilistele parameetritele

2. Kirjuta meetod `calculate_nightly_rate(season, num_guests)` üle:
    - **Parameeter:**
        - `season` (str): Hooaeg: `"summer"`/`"winter"`/`"spring"`/`"autumn"`
        - `num_guests` (int): Külaliste arv
    - **Tagastab:**
        - float: Arvutatud ööhind ümardatuna kahe komakohani
    - **Kirjeldus:**
        - Alusta baashinnaga: `base_price`
        - Kontrolli külaliste arvu:
            - Kui `num_guests` on suurem kui `capacity`, tõsta `ValueError` teatega:
                - Kui rendid kogu elamise kuva tekst: `"Korter mahutab maksimaalselt {capacity} külalist!"`
                - Kui rendid ainult ühe toa, kuva tekst: `"Tuba mahutab maksimaalselt {capacity} külalist!"`
        - Kontrolli, kas parameeter `season` on sobiv ehk kas läheb kokku hooaegadega:
            - Kui ei ole korrektne, tõsta `ValueError` koos sobiva teatega
        - Rakenda hooajalisust (korrutamisega):
            - `summer`: +40% (korruta 1.4-ga)
            - `winter`: -15% (korruta 0.85-ga)
            - `spring` ja `autumn`: baashind (korruta 1.0-ga)
        - Kontrolli majutuse tüüpi:
            - Kui renditakse kogu elamime:
                - Kui külaliste arv on suurem kui 4, lisa iga täiendava külalise eest (üle 4) 10€
            - Kui renditakse ainult tuba:
                - Kui külaliste arv on suurem kui 1, lisa iga täiendava külalise eest (üle 1) 15€
        - Lisa instant booking soodustus:
            - Kui `instant_booking`-u võimalus on olemas on, korruta hind 0.95-ga (-5%)
        - Lisa minimaalsete ööde soodustus:
            - Kui `min_nights` on suurem või võrdne kui 3, korruta hind 0.9-ga (-10%)
        - Tagasta arvutatud hind ümardatuna kahe komakohani

3. Loo klassi meetod `get_object_data(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik TXT rea andmetega, kus:
            - Võtmed on TXT päise veerunimed, näiteks: `"name"`, `"address"`, `"city"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - AirBnB: Uus objekti instants
    - **Kirjeldus:**
        - Teisenda TXT rea andmed õigesse tüüpi:
            - `name`: string
            - `address`: string
            - `city`: string
            - `base_price`: float
            - `rating`: float
            - `capacity`: int
            - `has_wifi`: bool
            - `has_parking`: bool
            - `has_breakfast`: bool
            - `check_in_time`: string
            - `check_out_time`: string
            - `min_nights`: int
            - `is_entire_place`: bool
            - `host_name`: string
            - `instant_booking`:bool
        - Tagasta `AirBnB` objekti kõigi parameetritega

4. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab AirBnB infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod
        - Lisa sinna:
            - Kui `is_entire_place` on `True`: `"Entire place hosted by {host_name}"`
            - Kui `is_entire_place` on `False`: `"Private room hosted by {host_name}"`
            - `Instant booking: {"Available" kui instant_booking on True, muidu "Not available"}`
        - Tagasta string, mis sisaldab AirBnB infot

---

### Alamklass: Campsite

1. Loo alamklass `Campsite` ning selle klassi konstruktor:
    - **Klassimuutuja:**
        - Loo vastav klassimuutuja, mis kirjutab `accommodation_type` üle väärtusega `"Campsite"`
    - **Parameetrid:**
        - Kõik `Accommodation` parameetrid
        - `max_tent_spots_in_camping` (int): Maksimum telgikohtade arv kämpingu alal
        - `has_electricity` (bool): Kas on elekter
        - `has_showers` (bool): Kas on dušid
    - **Kirjeldus:**
        - Alamklass pärib vanemklassist `Accommodation`
        - Kutsu välja vanemklassi konstruktor
        - Loo uued atribuudid campsite'ile spetsiifilistele parameetritele

2. Kirjuta meetod `calculate_nightly_rate(season, num_guests)` üle:
    - **Parameeter:**
        - `season` (str): Hooaeg: `"summer"`/`"winter"`/`"spring"`/`"autumn"`
        - `num_guests` (int): Külaliste arv
    - **Tagastab:**
        - float: Arvutatud ööhind ümardatuna kahe komakohani
    - **Kirjeldus:**
        - TÄHELEPANU: Campsite'is on baashind telgikoha kohta, mitte inimese kohta!
        - Alusta baashinnaga: `base_price`
        - Rakenda hooajalisust (korrutamisega):
            - `summer`: +60% (korruta 1.6-ga)
            - `winter`: -65% (korruta 0.35-ga)
            - `spring`: +10% (korruta 1.1-ga)
            - `autumn`: baashind (korruta 1.0-ga)
        - Kontrolli, kas parameeter `season` on sobiv ehk kas läheb kokku hooaegadega:
            - Kui ei ole korrektne, tõsta `ValueError` koos sobiva teatega
        - Arvuta vajalike telkide arv:
            - Eeldame, et 2-3 inimest mahuvad ühte telki
            - Valem: `num_tents_needed = (külaliste_arv + 2) // 3`
            - Näiteks: 7 külalist = (7+2)//3 = 3 telki
        - Kontrolli telgikohtade olemasolu:
            - Kui vajalike telkide kogus on suurem kui telgikohtade arv, tõsta `ValueError` teatega: `"Campsite'il on ainult {tent_spots} telgikohta!"`
        - Arvuta telkide koguhind:
            - Korruta telgikoha hind vajalike telkide arvuga kui ühe telgi hind on 15€
        - Lisa elektri tasu:
            - Kui kämpingu alal on elekter, lisa iga telgi kohta 3€
        - Lisa WiFi tasu:
            - Kui `kämpingu alal on WiFi, lisa 2€ (ühekordne tasu, mitte telgi kohta)
        - Dušši tasu:
            - Kui kämpingu alal ei ole dušši võimalust, korruta hind 0.85-ga (-15%)
        - Tagasta arvutatud hind ümardatuna kahe komakohani

3. Loo klassi meetod `read_from_csv_row(row_dict)`:
    - **Parameeter:**
        - `row_dict` (dict): Sõnastik TXT rea andmetega, kus:
            - Võtmed on TXT päise veerunimed, näiteks: `"name"`, `"address"`, `"city"`
            - Väärtused on vastava rea andmed (kõik stringidena)
    - **Tagastab:**
        - Campsite: Uus objekti instants
    - **Kirjeldus:**
        - Teisenda TXT rea andmed õigesse tüüpi:
            - `name`: string
            - `address`: string
            - `city`: string
            - `base_price`: float
            - `rating`: float
            - `capacity`: int
            - `has_wifi`: bool
            - `has_parking`: bool
            - `has_breakfast`: bool
            - `check_in_time`: string
            - `check_out_time`: string
            - `min_nights`: int
            - `max_tent_spots_in_camping`: int
            - `has_electricity`: bool
            - `has_showers`:bool
        - Tagasta `Campsite` objekti kõigi parameetritega

4. Kirjuta meetod `__repr__` üle:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - str: String, mis sisaldab campsite'i infot
    - **Kirjeldus:**
        - Kutsu välja vanemklassi `__repr__()` meetod
        - Lisa sinna:
            - `Tent spots: {tent_spots}`
            - `Electricity: {"Available" kui has_electricity on True, muidu "Not available"}`
            - `Showers: {"Available" kui has_showers on True, muidu "Not available"}`
        - Tagasta string, mis sisaldab campsite'i infot

---

### Põhiprogramm

**Failinimi:** `main.py`

## Nõuded:

1. Loo funktsioon `load_accommodations_from_txt(filename)`:
    - **Parameeter:**
        - `filename` (str): TXT faili nimi või tee
    - **Tagastab:**
        - list: Nimekiri majutuskohtade objektidest (Hotel, AirBnB, Campsite)
    - **Kirjeldus:**
        - Ava fail ja loe selle sisu
        - Käi läbi iga rida failist:
            - Ignoreeri tühje ridu ja vigaseid/ebakorrektseid ridu
            - Jaga rida õigeks andmeteks
            - Tuvasta majutuskoha tüüp
            - Loo sõnastik (dictionary), mis sisaldab kõiki vajalikke välju vastava klassi jaoks
            - Kutsu välja vastava klassi klassimeetod `get_object_data(...)`, et luua objekt
            - Lisa loodud objekt nimekirja
            - Kui tüüp on tundmatu või tekib viga objekti loomisel, jätka järgmise reaga
        - **Vigade käsitlus:**
            - Kasuta `try-except` plokki failiga töötamiseks:
                - `FileNotFoundError`: Faili ei leitud - kuva kasutajale arusaadav teade
                - `Exception`: Muud vead - püüa kinni ja kuva informatsioon
        - Tagasta majutuskohtade nimekiri (ka siis kui see on tühi)

2. Loo funktsioon `main()`:
    - **Parameeter:**
        - Puudub
    - **Tagastab:**
        - Puudub
    - **Kirjeldus:**
        - Lae majutuskohad CSV failist `data_accommodation.txt` kasutades sobivat funktsiooni
        - Kontrolli ega majutuskohtade objektide list pole tühi:
            - Kui on tühi, siis kuva veateade ja lõpeta funktsioon
        - Kuva kõigi majutuskohtade info
        - Näita polümorfismi:
            - Vali üks hotell, üks AirBnB ja üks campsite
            - Kasuta erinevaid hooaegu (`summer`, `spring`, `winter`) ning kuva nende hind erinevate külaliste arvuga

3. Programmi käivitamine:
    - Kutsu välja `main()` funktsioon programmi lõpus:
    ```python
    if __name__ == "__main__":
        main()
    ```

---

## Programmi väljund: Majutuskohtade info kuvamine

```python
Laaditud 15 majutuskohta:

Type: Hotel
Name: Radisson Blu Sky
Address: Rävala 3
Base price: 150.0€ per night
Rating: 8.5/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 15:00, Check-out: 12:00
Amenities: ['WiFi', 'Parking', 'Breakfast']
Stars: 5
Spa: Yes
Room service: Yes
---------------------------------
Type: AirBnb
Name: Private Room in Kadriorg
Address: Weizenbergi 22
Base price: 45.0€ per night
Rating: 4.6/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 17:00, Check-out: 11:00
Amenities: ['WiFi', 'Breakfast']
Private room hosted by Anna
Instant booking: Not available
---------------------------------
Type: Campsite
Name: Stroomi Beach Camp
Address: Pelgurand
Base price: 12.0€ per night
Rating: 3.9/10.0
Capacity: 4 guests
Minimum nights: 1
Check-in: 10:00, Check-out: 12:00
Amenities: ['Parking']
Tent spots: 30
Electricity: Available
Showers: Available
---------------------------------
Type: AirBnb
Name: Seaside Apartment in Pirita
Address: Merivälja tee 3
Base price: 70.0€ per night
Rating: 4.7/10.0
Capacity: 4 guests
Minimum nights: 3
Check-in: 16:00, Check-out: 10:00
Amenities: ['WiFi', 'Parking']
Entire place hosted by Peeter
Instant booking: Available
---------------------------------
Type: Hotel
Name: Nordic Hotel Forum
Address: Viru väljak 3
Base price: 110.0€ per night
Rating: 9.2/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 15:00, Check-out: 11:00
Amenities: ['WiFi', 'Parking']
Stars: 4
Spa: No
Room service: Yes
---------------------------------
Type: AirBnb
Name: Cozy Old Town Apartment
Address: Pikk 45
Base price: 80.0€ per night
Rating: 4.8/10.0
Capacity: 4 guests
Minimum nights: 2
Check-in: 16:00, Check-out: 11:00
Amenities: ['WiFi']
Entire place hosted by Kristiina
Instant booking: Available
---------------------------------
Type: AirBnb
Name: Central Studio
Address: Gonsiori 18
Base price: 55.0€ per night
Rating: 4.5/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 15:00, Check-out: 11:00
Amenities: ['WiFi']
Entire place hosted by Liisa
Instant booking: Not available
---------------------------------
Type: Hotel
Name: Park Inn
Address: Narva mnt 7c
Base price: 85.0€ per night
Rating: 6.0/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 14:00, Check-out: 12:00
Amenities: ['WiFi', 'Parking', 'Breakfast']
Stars: 3
Spa: No
Room service: No
---------------------------------
Type: Hotel
Name: Go Hotel Shnelli
Address: Toompuiestee 37
Base price: 65.0€ per night
Rating: 3.8/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 15:00, Check-out: 12:00
Amenities: ['WiFi', 'Breakfast']
Stars: 2
Spa: No
Room service: No
---------------------------------
Type: Campsite
Name: Pirita Beach Camping
Address: Merivälja tee 1
Base price: 15.0€ per night
Rating: 4.2/10.0
Capacity: 4 guests
Minimum nights: 1
Check-in: 12:00, Check-out: 12:00
Amenities: ['Parking']
Tent spots: 50
Electricity: Available
Showers: Available
---------------------------------
Type: Campsite
Name: Kakumäe Camping
Address: Kakumäe tee 48
Base price: 18.0€ per night
Rating: 4.4/10.0
Capacity: 6 guests
Minimum nights: 1
Check-in: 11:00, Check-out: 11:00
Amenities: ['WiFi', 'Parking']
Tent spots: 40
Electricity: Available
Showers: Available
---------------------------------
Type: Hotel
Name: Tallink Spa & Conference
Address: Sadama 11a
Base price: 120.0€ per night
Rating: 6.3/10.0
Capacity: 2 guests
Minimum nights: 1
Check-in: 14:00, Check-out: 12:00
Amenities: ['WiFi', 'Parking', 'Breakfast']
Stars: 4
Spa: Yes
Room service: Yes
---------------------------------
Type: Campsite
Name: Harku Lake Camping
Address: Harku järv
Base price: 10.0€ per night
Rating: 4.0/10.0
Capacity: 4 guests
Minimum nights: 1
Check-in: 09:00, Check-out: 14:00
Amenities: No
Tent spots: 25
Electricity: Not available
Showers: Available
---------------------------------
Type: AirBnb
Name: Modern Kalamaja Loft
Address: Soo 15
Base price: 95.0€ per night
Rating: 4.9/10.0
Capacity: 6 guests
Minimum nights: 2
Check-in: 15:00, Check-out: 11:00
Amenities: ['WiFi', 'Parking']
Entire place hosted by Martin
Instant booking: Available
---------------------------------
Type: Campsite
Name: RMK Nõva Camping
Address: Nõva küla
Base price: 8.0€ per night
Rating: 4.3/10.0
Capacity: 6 guests
Minimum nights: 1
Check-in: 00:00, Check-out: 00:00
Amenities: ['Parking']
Tent spots: 60
Electricity: Available
Showers: Available
---------------------------------
```

---

## Programmi väljund: Polümorfism -> Hindade arvutamine

**PS! Polümorfismi väljund ei pea täpselt selline olema nagu siin. Ma tegin meelega sellise väljundi, et te näeksite paremini.**

```python
*** POLÜMORFISMI DEMONSTRATSIOON - Öise hinna arvutamine ***

Hotel: Radisson Blu Sky
Baashind: 150.0€ per öö
---------------------------------
  Summer   | 2 külalist -> 346.5€
  Summer   | 4 külalist -> 456.5€
  Summer   | 6 külalist -> 511.5€
  Spring   | 2 külalist -> 264.0€
  Spring   | 4 külalist -> 374.0€
  Spring   | 6 külalist -> 429.0€
  Winter   | 2 külalist -> 231.0€
  Winter   | 4 külalist -> 341.0€
  Winter   | 6 külalist -> 396.0€


AirBnb: Private Room in Kadriorg
Baashind: 45.0€ per öö
---------------------------------
  Summer   | 2 külalist -> 78.0€
  Summer   | 4 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!
  Summer   | 6 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!
  Spring   | 2 külalist -> 60.0€
  Spring   | 4 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!
  Spring   | 6 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!
  Winter   | 2 külalist -> 53.25€
  Winter   | 4 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!
  Winter   | 6 külalist -> Viga: Tuba mahutab maksimaalselt 2 külalist!


Campsite: Stroomi Beach Camp
Baashind: 12.0€ per öö
---------------------------------
  Summer   | 2 külalist -> 37.2€
  Summer   | 4 külalist -> 55.2€
  Summer   | 6 külalist -> 55.2€
  Spring   | 2 külalist -> 31.2€
  Spring   | 4 külalist -> 49.2€
  Spring   | 6 külalist -> 49.2€
  Winter   | 2 külalist -> 22.2€
  Winter   | 4 külalist -> 40.2€
  Winter   | 6 külalist -> 40.2€
```

---
