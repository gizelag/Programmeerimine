import json
import requests
import time


def read_api_key(api_key_filename):
    # Kontrollime, kas faili nimi anti üldse ette
    if api_key_filename is None:
        print("Faili nimi on vajalik!")
        return None

    try:
        # Avame API võtme faili
        with open(f"../API_KEY/{api_key_filename}", 'r') as f:
            api_key = f.read().strip()

            # Kontrollime, kas API võtme pikkus on õige
            if len(api_key) == 31:
                return api_key
            else:
                print("API key invalid! (31 tähemärki)")
                return None

    except FileNotFoundError:
        print("API võtme fail puudub!")
        return None
    except Exception as e:
        print(e)
        return None


def get_weather_data_multiple_cities(api_base_url, api_key, cities,
                                     todays_data_filename="todays_weather_data.txt"):
    # Andmete tüübi kontroll
    if not isinstance(api_base_url, str):
        print("Viga andmetes")
        return None
    if not isinstance(cities, list):
        print("Viga andmetes")
        return None
    if not isinstance(todays_data_filename, str):
        print("Viga andmetes")
        return None
    if not api_key:
        print("Viga andmetes")
        return None

    # Loendame, mitme linna andmed edukalt saadi
    city_loendur = 0

    try:
        # Käime kõik linnad läbi
        for query in cities:
            city_data = {}

            # API päringu parameetrid
            params = {
                'key': api_key,
                'q': query,
            }

            try:
                # Proovime päringut kuni 2 korda
                for attempt in range(2):
                    data = requests.get(
                        f"{api_base_url}/current.json",
                        params=params,
                        timeout=10
                    )
                    data.raise_for_status()

                    if data.status_code != 200:
                        print("Viga andmete saamises")
                        continue

                    vastus = data.json()

                    # Võtame vajalikud ilmaandmed välja
                    city_data.update({
                        "location": vastus["location"]["name"],
                        "local_time": vastus["location"]["localtime"],
                        "temperature": vastus["current"]["temp_c"],
                        "wind_speed": vastus["current"]["wind_kph"],
                        "humidity": vastus["current"]["humidity"],
                        "uv_index": vastus["current"]["uv"]
                    })

                    # Salvestame andmed faili
                    kas_onnestus = save_todays_weather_data(
                        city_data, todays_data_filename
                    )

                    if kas_onnestus:
                        city_loendur += 1
                    break

            except requests.exceptions.RequestException:
                print("Viga päringus")
                if attempt == 1:
                    raise
                time.sleep(0.3)

        if city_loendur == 0:
            print("Viga andmetes")
            return None

        return city_loendur

    except Exception as e:
        print(e)
        return None


def save_todays_weather_data(city_data, todays_data_filename):
    # Kontrollime, kas linna andmed on olemas
    if not city_data:
        print("Vigased linna andmed")
        return False

    try:
        # Lisame ilmaandmed faili
        with open(todays_data_filename, 'a', encoding="utf-8") as f:
            f.write(
                f"Linn: {city_data['location']}\n"
                f"Kohalik aeg: {city_data['local_time']}\n"
                f"Temperatuur: {city_data['temperature']} °C\n"
                f"Tuule kiirus: {city_data['wind_speed']} km/h\n"
                f"Õhuniiskus: {city_data['humidity']}\n"
                f"UV indeks: {city_data['uv_index']}\n\n\n"
            )
        return True

    except Exception as e:
        print(e)
        return False


def get_weather_forecast_multiple_cities(api_base_url, api_key, cities):
    # Sõnastik kõikide linnade prognooside jaoks
    city_forecast_data = {}

    try:
        # Käime kõik linnad läbi
        for query in cities:
            three_days = []

            params = {
                'key': api_key,
                'q': query,
                'days': 3
            }

            try:
                for attempt in range(2):
                    data = requests.get(
                        f"{api_base_url}/forecast.json",
                        params=params,
                        timeout=10
                    )
                    data.raise_for_status()

                    if data.status_code != 200:
                        print("Viga andmete saamises")
                        continue

                    vastus = data.json()

                    # Kolme päeva prognoos
                    for day in vastus["forecast"]["forecastday"]:
                        three_days.append({
                            "date": day["date"],
                            "temperature": day["day"]["avgtemp_c"],
                            "max_wind_speed": day["day"]["maxwind_kph"],
                            "humidity": day["day"]["avghumidity"],
                            "uv_index": day["day"]["uv"],
                        })

                    city_forecast_data[query] = three_days
                    break

            except requests.exceptions.RequestException:
                if attempt == 1:
                    raise
                time.sleep(0.3)

        # Salvestame prognoosi JSON faili
        return save_forecast_weather_data(city_forecast_data)

    except Exception as e:
        print(e)
        return False


def save_forecast_weather_data(forecast_data,
                               forecast_data_filename="weather_forecast_data.json"):
    # Kontrollime, kas on mida salvestada
    if not forecast_data:
        print("Viga andmetes")
        return None

    try:
        # Salvestame prognoosi JSON faili
        with open(forecast_data_filename, 'w', encoding="utf-8") as f:
            json.dump(forecast_data, f, indent=4, ensure_ascii=False)
            print("Success")
        return True

    except Exception as e:
        print(e)
        return None


def main():
    api_base_url = "http://api.weatherapi.com/v1"

    # Linnad, mille ilma tahame
    cities = [
        "Tallinn", "Riga", "Vilnius", "Helsinki",
        "Stockholm", "Warsaw", "Copenhagen",
        "Amsterdam", "Madrid", "London"
    ]

    # Loeme API võtme failist
    api_key = read_api_key("weather_api_key.py")

    # Hangime tänased ilmaandmed
    data = get_weather_data_multiple_cities(
        api_base_url, api_key, cities
    )

    # Hangime ilmaennustuse
    forecast = get_weather_forecast_multiple_cities(
        api_base_url, api_key, cities
    )

    if forecast:
        print(
            f"API võti laetud ({len(api_key)} tähemärki)\n"
            f"Andmed hangitud {data} linna kohta\n"
            f"Andmed salvestatud faili ja JSON-i"
        )
    else:
        print("Viga andmete salvestamises.")


if __name__ == "__main__":
    main()
