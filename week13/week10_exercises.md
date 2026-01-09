# Nädal 10 praktikum - HTTP päringud ja API-de kasutamine

## Seadistamine

1. Loo kaust/directory nimega `week10`
2. Sinna kausta loo kõik selle nädala praktikumide ülesanded
3. Peale praktikumi lõpetamist lae need `GitLabi`

---

## Hindamiskriteeriumid

1. Kõik API päringud peavad kasutama `requests` moodulit
2. Vigade käsitlemine peab olema implementeeritud: `try-except`
3. JSON andmete töötlemine peab olema korrektne
4. API võtmed peavad olema eraldi failides, mitte koodi sees
5. Kood peab olema kommenteeritud ja dokumenteeritud
6. Kasutada `type hinte` kus võimalik
7. Kasuta `isinstance()` funktsiooni, et kontrollida, kas parameeter on õiget tüüpi
8. Koodi käivitamine käib  `main()` funktsiooni kaudu

---

## Ülesanne 1 - Lihtne andmete hankimine
**Faili nimi:** `get_json_data.py`

### Eesmärk:
Loo programm, mis hangib kõik kasutajad JSONPlaceholder API-st ning töötleb nende andmeid. Vigade käsitlemine peab olema implementeeritud (try-except).

### API teenus ja endpointid
    ```bash
    https://jsonplaceholder.typicode.com/users
    ```

### Nõuded
1. Funktsioon `get_all_users(base_api_url)`:
    - **Parameeter:**
        - `base_api_url` (str): API link
    - **Tagastab:** 
        - `dict`: Kasutajanimi on võti ja vastav e-mail väärtus, kõikide kasutajate kohta
        - `{}`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetrite tüüpe:
            - Vea korral kuva veateade ja lõpeta funktsioon
        - Vigade käsitlemine `GET requesti` ajal:
            - Kasuta üldist `try-except` blokki ootamatu vea püüdmiseks
            - Kasuta `try-except` blokki HTTP päringute jaoks: `requests.exceptions.RequestException`
            - Kontrolli HTTP vastuse staatust: `response.status_code`
            - Vea korral kuva enda valitud veateade ja tagasta tühi sõnastik
        - Saata GET request:
            - Vastuseks saadud andmed pane vajadusel  õigesse formaati
            - Loo sõnastik, kus võtmeteks on kasutaja nimed ja väärtusteks nimedega seotud e-mailid: `{"name": "email", ...}`
        - Tagasta `dictionary`, kus võtmeteks on kasutaja enda täisnimi ja väärtusteks animedega seotud e-mailid

2. Funktsioon `get_user_count(users_data)`:
    - **Parameeter:**
        - `users_data` (dict): Kasutajate andmed, kus võtmeteks on kasutajanimed ja väärtusteks kasutajanimedega seotud e-mailid
    - **Tagastab:**
        - `int`: Kasutajate koguarv
        - `None`: Vea korral
    - Vigade käsitlemine:
        - Kontrolli, kas `users_data` on dict tüüpi
        - Kontrolli, kas dict ei ole tühi
        - Mõlemal juhul tagasta `None` ja kuva veateade
    - Andmete töötlemine:
        - Loenda sisendis antud kasutajate kogus ja tagasta selle väärtus

3. Funktsioon `main()`:
    - Kutsu välja funktsioon `get_all_users(base_api_url)` koos vastava parameetriga
    - Kutsu välja funktsioon `get_user_count(users_data)` koos vastava parameetriga:
    - Kuva kasutajad nummerdatud loendina 
    - Kuva kasutajate koguarv
    - Kui mõlemad funktsioonid tagastavad vea indikaatorid (tühi dict ja None), kuva sobiv tekst, näiteks: `Viga: ei suutnud andmeid hankida`


4. Programmi käivitamine:
    ```python
    if __name__=="__main__":
        main()
    ```

### Väljundi näide kui andmed on olemas:
```
KASUTAJAD:
1. Leanne Graham (Sincere@april.biz)
2. Ervin Howell (Shanna@melissa.tv)
3. Clementine Bauch (Nathan@yesenia.net)
...
10. Clementina DuBuque (Rey.Padberg@karina.biz)

KASUTAJATE KOGU ARV:
Kasutajaid kokku on: 10
```

### Väljundi näide kui andmeid ei ole olemas:
```
Viga: ei suutnud andmeid hankida
```

---

## Ülesanne 2 - JSONPlaceholder API töötlemine
**Failinimi:** `json_placeholder_analytics.py`

### Eesmärk
Loo programm, mis kasutab JSONPlaceholder API-t andmete analüüsimiseks ja töötlemiseks. See on Code Along 1 edasiarendus. Vigade käsitlemine peab olema implementeeritud (try-except).


### API teenus ja endpointid
Baas URL: `https://jsonplaceholder.typicode.com/users`

Kasutatavad endpointid:
- Konkreetne kasutaja:
```
  https://jsonplaceholder.typicode.com/users/{id}
```
- Kasutaja postitused:
```
  https://jsonplaceholder.typicode.com/users/{id}/posts
```
- Kõik kommentaarid:
```
  https://jsonplaceholder.typicode.com/comments
```

### Nõuded

1. Funktsioon `analyze_email_domains(base_api_url)`:
    - **Parameeter:**
        - `base_api_url` (str): API põhilink
    - **Tagastab:**
        - `dict`: Domeeni lõppude statistika, näiteks `{".com": 4, ".net": 3}`
        - `{}`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetri tüüpi:
            - `base_api_url` peab olema `str`
            - Vea korral kuva veateade ja tagasta `{}`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki
            - Kontrolli HTTP staatust
            - Vea korral kuva enda valitud veateade ja tagasta `{}`
        - Andmete töötlemine:          
            - Analüüsi kõigi kasutajate emailide domeeni lõppe
            - Iga kasutaja email on formaadis: `"username@domain.extension"`
            - Eraldi domeeni lõpp, näiteks `".com", ".net", ".org", ".biz"`
            - Loe kokku, mitu korda iga lõpp esineb
            - **Näide:** Email `"Sincere@april.biz"` -> domeeni lõpp on `".biz"`
        - Tagasta dict: võtmeks domeeni lõpp, väärtuseks esinemiste arv

2. Funktsioon `get_user_info(base_api_url, user_id)`:
    - **Parameetrid:**
        - `base_api_url` (str): API põhilink
        - `user_id` (int): Kasutaja ID number (1-10)
    - **Tagastab:** 
        - `dict`: Kasutaja detailsed andmed
        - `{}`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetrite tüüpe:
            - `base_api_url` peab olema `str`
            - `user_id` peab olema `int`
            - Vea korral kuva veateade ja tagasta `{}`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki HTTP päringute jaoks: `requests.exceptions.RequestException`
            - Kontrolli HTTP staatust: `response.status_code == 200`
            - Vea korral kuva veateade ja tagasta `{}`
        - Andmete töötlemine:
            - Saada GET päring: `{base_api_url}/users/{user_id}`
            - Hangi konkreetse kasutaja andmed API-st
            - Tagasta API vastus JSON formaadis (dict)

3. Funktsioon `get_user_posts(base_api_url, user_id)`:
    - **Parameetrid:**
        - `base_api_url` (str): API põhilink
        - `user_id` (int): Kasutaja ID number
    - **Tagastab:**
        - `list[dict]`: Kasutaja postituste andmed
        - `[]`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetrite tüüpe:
            - `base_api_url` peab olema `str`
            - `user_id` peab olema `int`
            - Vea korral kuva veateade ja tagasta `[]`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki HTTP päringute jaoks
            - Kontrolli HTTP staatust
            - Vea korral kuva enda valitud veateade ja tagasta `[]`
        - Andmete töötlemine:
            - Saada sobiv GET päring
            - Hangi kõik kasutaja postitused
            - **NB:** Iga postitus on dict, mis sisaldab välju: `userId, id, title, body`
        - Tagasta kõik kasutaja postitused listina

4. Funktsioon `count_user_comments(base_api_url, user_id)`:
    - **Parameetrid:**
        - `base_api_url` (str): API põhilink
        - `user_id` (int): Kasutaja ID number
    - **Tagastab:**
        - `int`: Kommentaaride koguarv
        - `None`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetrite tüüpe:
            - Vea korral kuva veateade ja tagasta `None`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki
            - Vea korral kuva veateade ja tagasta `None`
        - Andmete töötlemine:
            1. Hangi kasutaja postitused, kasuta selleks loodud funktsiooni `get_user_posts(base_api_url, user_id)`
            2. Loo list postituste ID-dest: `post_ids = [1, 2, 3, ...]`
            3. Hangi kõik kommentaarid kasutades GET päringut /comments endpointile
            4. Iga kommentaar sisaldab välja postId, seega filtreeri kommentaarid, kus `comment['postId']` on post_ids listis
            5. Tagasta filtreeritud kommentaaride arv

5. Funktsioon `generate_users_report(base_api_url, filename="users_raport.txt)`:
    - **Parameetrid:**
        - `base_api_url` (str): API põhilink
        - `filename` (str): Faili nimi, vaikimisi `"users_raport.txt"`
    - **Tagastab:**
        - `None`: Funktsioon ainult prindib väljundi
    - **Kirjeldus:**
        - Funktsioon loob faili kasutajate 1-10 raportitega
        - Kontrolli parameetrite tüüpe:
            - Vea korral kuva veateade ja lõpeta funktsioon
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki
            - Kui mõni funktsioon tagastab vea indikaatori, kuva veateade ja lõpeta
        - Raporti loomine:
            - Loo tsükkel, mis käib läbi user_id väärtused `1-10`:
                - Hangi kasutaja info, kasuta funktsiooni `get_user_info(base_api_url, user_id)`
                - Hangi kasutaja postitused, kasuta funktsiooni `get_user_posts(base_api_url, user_id)`
                - Hangi kommentaaride arv, kasuta funktsiooni `count_user_comments(base_api_url, user_id)`
            - Kasuta parameetrit `filename` ja loo fail, formaadis:
                ```text
                    KASUTAJA {id} RAPORT
                    Nimi: {name}
                    Email: {email}
                    Telefon: {phone}
                    Veebileht: {website}
                    
                    Aadress: {street}, {city} {zipcode}
                    Ettevõte: {company.name}
                    
                    Postitused ({arv} tk):
                    1. {esimese postituse title}
                    2. {teise postituse title}
                    ...
                    
                    Kokku kommentaare kasutaja postitustel: {arv}


                ```
            - Faili sisaldab kõikide kasutajate andmeid
            - Jäta paar tühja rida iga kasutaja vahele
            - **NB:**
                - Aadressi andmed on struktuuris: `address.street`
                - Ettevõte andmed on struktuuris: `company.name`
        - Kui fail on edukalt loodud, kuva vabalt valitud teade

6. Funktsioon `main()`:
    - **Kirjeldus:**
        - Määra konstantne baas URL:
        ```python
                BASE_API_URL = "https://jsonplaceholder.typicode.com"
        ```
        - Kutsu välja ja kuva tulemused:
            1. `analyze_email_domains(base_api_url)`
                - Kuva iga domeeni lõpp ja kasutajate arv:
                    ```
                        .com: 4 kasutajat
                        .net: 3 kasutajat
                        ...
                    ```
                - Kui funktsioon tagastab `{}`, kuva: `"Viga: domeene ei suudetud analüüsida"`
            
            2. Loo ja salvesta raport kasutades funktsiooni `generate_users_report(base_api_url, filename="users_raport.txt)`

7. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### Väljundi näide:
```bash
    E-MAILIDE DOMEENID
    .com: 4 kasutajat
    .net: 3 kasutajat
    .org: 2 kasutajat
    .biz: 1 kasutajat

    Faili `users_raport.txt` loomine õnnestus edukalt!
```

### Faili `users_raport.txt` sisu, mis sisaldab ainult kasutaja 1 raportit:
```text
KASUTAJA 1 RAPORT
Nimi: Leanne Graham
Email: Sincere@april.biz
Telefon: 1-770-736-8031 x56442
Veebileht: hildegard.org

Aadress: Kulas Light, Gwenborough 92998-3874
Ettevõte: Romaguera-Crona

Postitused (10 tk):
1. sunt aut facere repellat provident occaecati excepturi optio reprehenderit
2. qui est esse
3. ea molestias quasi exercitationem repellat qui ipsa sit aut
4. eum et est occaecati
5. nesciunt quas odio
6. dolorem eum magni eos aperiam quia
7. magnam facilis autem
8. dolorem dolore est ipsam
9. nesciunt iure omnis dolorem tempora et accusantium
10. optio molestias id quia eum

Kokku kommentaare kasutaja postitustel: 50


```

### Näpunäited
1. **Email domeeni analüüsiks:** kasuta `.split()` meetodid
2. **Kommentaaride lugemiseks:** hangi kõik kommentaarid ja filtreeri `postId` järgi
3. **Aadressi vormindamiseks:** kombineeri `address` objekti väljad
4. **Vigade käsitlemiseks:** kontrolli `response.status_code` ja kasuta `try-except`

---

## Ülesanne 3 - Ilmajaam
**Failinimi:** `weather_analytics.py`

### Eesmärk
Loo täiustatud ilmarakendus, mis kogub, salvestab ja analüüsib ilmaandmeid mitme linna kohta. See on Code Along 3 edasiarendus.

### Failide struktuur:

- `weather_analytics.py` - põhiprogramm
- `weather_api_key.txt` - sinu API võti
- `todays_weather_data.txt` - tänase ilma andmed
- `weather_forecast_data.json` - salvestatud ilma prognoos

### API võtme loomine:
1. Mine lehel https://www.weatherapi.com
2. Loo seal endale kasutaja, selles on vaja e-maili ning loo endale sobiv password
3. Logi sisse
4. Dashboard/API -> Generate API Key
5. Kui API Key on loodud, kopeeri see ning salvesta faili `weather_api_key.txt`


### API teenuse baas URL:
    ```bash
        http://api.weatherapi.com/v1
    ```

### API teenuse dokumentatsioon
    ```bash
        https://www.weatherapi.com/docs/
    ```

### Linnade nimekiri
```python
cities = [
    "Tallinn", "Riga", "Vilnius", "Helsinki",
    "Stockholm", "Warsaw", "Copenhagen", 
    "Amsterdam", "Madrid", "London"
]
```

### Nõuded
1. Funktsioon `read_api_key(api_key_filename = "weather_api_key.txt")`:
    - **Parameeter:**
        - `api_key_filename` (str): API võtme faili nimi
    - **Tagastab:** 
        - `str`: Sinu API võti
        - `None`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetri tüüpi:
            - Vea korral kuva veateade ja tagasta `None`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki  `FileNotFoundError` ja üldise `Exception` püüdmiseks
            - Kui mõni funktsioon tagastab vea veateade, kuva veateade ja tagasta `None`
        - Loe API võti failist:
            - Loe kogu faili sisu ühte stringi
            - Eemalda tühikud ja reavahetused nii algusest ka kui lõpust
        - Kontrolli, et API võti on olemas:
            - Failist loetud string pole tühi string
            - Stringi pikkus on 31
            - Vea korral kuva enda valitud veateade ja tagasta `None`
            - API võtme olemasolul tagasta see võti

2. Funktsioon `get_weather_data_multiple_cities(api_base_url, api_key, cities, todays_data_filename="todays_weather_data.txt")`:
    - **Parameetrid:**
        - `api_base_url` (str): API baas URL
        - `api_key` (str): Sinu API võti
        - `cities` (list[str]): Linnade nimekiri
        - `todays_data_filename` (str): Väljundfaili nimi (vaikimisi:`todays_weather_data.txt`)
    - **Tagastab:**
        - `int`: Edukalt salvestatud linnade arv
        - `None`: Vea korral
    - **Kirjeldus:**
        - Kontrolli parameetrite tüüpe:
            - Vea korral kuva veateade ja tagasta `None`
        - Loo tsükkel, kus iga linna kohta:
            - Vigade käsitlemine:
                - Kasuta `try-except` blokki HTTP päringute jaoks: `requests.exceptions.RequestException`
                - Kontrolli HTTP staatust: `response.status_code == 200`
                - Kui linna päringu/töötluse ajal tekib viga, kuva veateade ja jätka järgmise linnaga
            - HTTP päring:
                - Tee HTTP päring `/current.json` endpointile
                - Kasuta `timeout`-i või `retry`-d `RequestException` korral
            - Ekstrakti vajalikud andmed JSON vastusest ja salvesta dictionary-sse:
                - `location`: Linna nimi
                - `local_time`: Kohalik aeg
                - `temperature`: Temperatuur (°C)
                - `wind_speed`: Tuule kiirus (km/h)
                - `humidity`: Õhuniiskus (%)
                - `uv_index`: UV indeks
                - Kutsu välja funktsioon `save_todays_weather_data(city_data, todays_data_filename)` ning salvesta linna andmed faili
            - Loenda salvestatud linnade andmeid:
                - Kui `save_todays_weather_data(city_data)` tagastas `True` siis lisa loendusesse üks juurde
                - Kuva ühegi linna andmeid ei salvestatud, siis kuva veateade ja tagasta `None`
        - Tagasta linnade kogus, mis salvestati faili

3. Funktsioon `save_todays_weather_data(city_data, todays_data_filename= "todays_weather_data.txt")`:
    - **Parameetrid:**
        - `city_data` (dict): Ühe linna ilmaandmed (dictionary järgmiste võtmetega: `location`, `local_time`, `temperature`, `wind_speed`, `humidity`, `uv_index`)
        - `todays_data_filename` (str): Väljundfaili nimi (vaikimisi: `todays_weather_data.txt`)
    - **Tagastab:**
        - `bool`: `True` kui salvestamine õnnestus, `False` kui ebaõnnestus
    - **Kirjeldus:**
        - Kontrolli, kas linna andmed on olemas:
            - Vea korral kuva enda valitud veateade ja tagasta `False`
        - Vigade käsitlemine:
            - Kasuta `try-except` blokki faili kirjutamiseks
            - Vea korral kuva enda valitud veateade ja tagasta `False`
        - Faili loomine: 
            - Ava fail õiges režiimis, et mitte üle kirjutada eelmisi andmeid
            - Kasuta sobivat `encoding`-ut
        - Salvesta linna kohta järgmised andmed kujul:
            - `Linn: `
            - `Kohalik aeg: `
            - `Temperatuur: °C`
            - `Tuule kiirus:  km/h`
            - `Õhuniiskus: %`
            - `UV indeks: `
            - Jäta iga linna vahele üks/kaks tühja rida, et oleks loetavam
        - Kui andmed linna kohta salvestatud tagasta `True`

4. Funktsioon `get_weather_forecast_multiple_cities(api_base_url, api_key, cities)`:
    - **Parameetrid:**
        - `api_base_url` (str): API põhilink
        - `api_key` (str): API võti
        - `cities` (list[str]): Linnade nimekiri
    - **Tagastab:**
        - Puudub
    - **Kirjeldus:**
        - Loo tühi dictionary prognoosiandmete kogumiseks
        - Loo tsükkel, kus iga linna kohta:
            - Vigade käsitlemine:
                - Kasuta `try-except` blokki HTTP päringute jaoks: `requests.exceptions.RequestException`
                - Kasuta `try-except` blokki JSON töötlemise jaoks: `KeyError`
                - Kasuta üldist `try-except` blokki muude vigade püüdmiseks: `Exception`
                - Kontrolli HTTP staatust: `response.status_code == 200`
                - Kui linna päringu/töötluse ajal tekib viga:
                    - Kuva veateade
                    - Jätka järgmise linnaga
            - HTTP päring:
                - Tee HTTP päring `/forecast.json` endpointile
                - Kasuta `timeout`-i või `retry`-d `RequestException` korral
            - Andmete ekstraktimine ja salvestamine:
                - Ekstrakti järgmise 3 päeva ilmaprognoos JSON vastusest
                - Iga päeva kohta salvesta järgmised andmed dictionary-sse:
                    - `date`: Kuupäev
                    - `temperature`: Keskmine temperatuur (`avgtemp_c`)
                    - `max_wind_speed`: Maksimum tuule kiirus (`maxwind_kph`)
                    - `humidity`: Keskmine õhuniiskus (`avghumidity`)
                    - `uv_index`: UV indeks
                - Loo list päevade andmetest, näiteks: `city_forecast = [day1_data, day2_data, day3_data]`
                - Lisa linna prognoos sõnastikku, kus `key`= linna nimi ja `value`= list, mis sisaldab nõutud andmeid
            - Pärast iga linna andmete edukat kogumist salvesta andmed `.json` faili:
                - Kutsu välja funktsioon `save_forecast_weather_data(forecast_data)`
                - See salvestab **kõik seni kogutud linnade andmed** JSON faili
                - Eesmärk: Kui programm katkeb keskel, on vähemalt osa andmeid juba salvestatud

5. Funktsioon `save_forecast_weather_data(forecast_data, forecast_data_filename = "weather_forecast_data.json")`:
    - **Parameetrid:**
        - `forecast_data` (dict): Ilmaprognooside andmed
        - `forecast_data_filename` (str): JSON faili nimi, vaikimisi `weather_forecast_data.json`
    - **Tagastab:**
        - Puudub
    - **Kirjeldus:**
        - Kontrolli, kas linna andmed on olemas:
            - Vea korral kuva enda valitud veateade
        - Vigade käsitlemine:
            - Kasuta üldist `try-except` blokki muu vea
            - Vea tekkimisel kuva veateade
        - Salvesta kõigi linnade prognoosiandmed korraga ühte JSON faili:
            - Ava fail kirjutamiseks
            - Kasuta sobivat `encoding`-ut
            - Formaat peab olema loetav
            - Eesti tähed peavad olema korrektsed
        - JSON struktuur peab olema järgmine:
            ```json
            {
                "Linna_nimi": [
                    {
                        "date": "kuupäev",
                        "temperature": temperatuur,
                        "max_wind_speed": tuule_kiirus,
                        "humidity": niiskus,
                        "uv_index": uv_indeks
                    },
                    {
                        "date": "kuupäev",
                        ...
                    },
                    {
                        "date": "kuupäev",
                        ...
                    }
                ],
                "Teine_linn": [...]
            }
            ```
        - Kui kõik andmed on salvestatud kuva tekst, mis kinnitab edukat salvestamist

6. Funktsioon `main()`:
    - Seadista API ühendus
        - Kontrolli, kas API võti on olemas
        - Kui võtit ei ole, siis välju funktsioonist
    - Kogu ja salvesta tänased ilmaandmed
        - Prindi välja linnade kogus,
    - Hangi ja salvesta ilmaprognoos
    - Kuva tulemused

7. Programmi käivitamine:
    ```python
    if __name__ == "__main__":
        main()
    ```

### `todays_weather_data.txt` faili sisu:
```text
Linn: Tallinn
Kohalik aeg: 2025-10-29 13:47
Temperatuur: 8.0°C
Tuule kiirus: 14.0 km/h
Õhuniiskus: 93%
UV indeks: 0.5


Linn: Riga
Kohalik aeg: 2025-10-29 14:04
Temperatuur: 11.3°C
Tuule kiirus: 13.3 km/h
Õhuniiskus: 66%
UV indeks: 0.6


Linn: Vilnius
Kohalik aeg: 2025-10-29 13:47
Temperatuur: 8.0°C
....
....
```

### `weather_forecast_data.json` faili sisu:
```json
{
    "Tallinn": [
        {
            "date": "2025-10-30",
            "temperature": 6.7,
            "max_wind_speed": 31.0,
            "humidity": 90,
            "uv_index": 0.1
        },
        {
            "date": "2025-10-31",
            "temperature": 8.0,
            "max_wind_speed": 27.4,
            "humidity": 89,
            "uv_index": 0.0
        },
        {
            "date": "2025-11-01",
            "temperature": 6.9,
            "max_wind_speed": 19.1,
            "humidity": 89,
            "uv_index": 0.1
        }
    ],
    "Riga": [
        {
            "date": "2025-10-30",
            "temperature": 8.1,
            "max_wind_speed": 26.6,
            "humidity": 90,
            "uv_index": 0.1
        },
        {
            ......
            ......
        }
```

### Väljundi näide:
```
Laadin API võtit
API võti laetud: 31 tähemärki

=== Hangin praeguseid ilmaandmeid 10 linna kohta ===

=== Salvestan praeguseid andmeid ===

=== Hangin ilma prognoosi ===

=== Salvestan prognoosi andmeid

```

### Näpunäited
1. **API võtme lugemiseks:** Kasuta `with open()` ja kontrolli, et võti pole tühi
2. **Tekstifaili salvestamiseks:** Vorminda andmed loetavalt (nt "Tallinn: 15.2°C, tuul 8km/h")
3. **JSON salvestamiseks:** Kasuta `json.dump()` funktsiooni koos soovitatud parameetritega
4. **Vigade käsitlemiseks:** Kontrolli HTTP response koode ja kasuta `try-except`

---

