import json
import requests
import time

def read_api_key(api_key_filename):
    # Kontrollime kas fail on kaasa antud
    if api_key_filename is None:
        print("Faili nimi on vajalik!")
        return None
    try:
        with open(f"../API_KEY/{api_key_filename}", 'r') as f:
            api_key = f.read().strip()
            if len(api_key) == 31:
                return api_key
            else:
                print(f"API key invalid! (31 tähemärki)")
                return None
    except FileNotFoundError:
        print("API võtme fail puudub!")
        return None
    except Exception as e:
        print(e)
        return None

def get_weather_data_multiple_cities(api_base_url, api_key, cities, todays_data_filename="todays_weather_data.txt"):
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

    city_loendur = 0

    try:
        for query in cities:
            city_data = {}
            params = {
                'key': api_key,
                'q': query,
            }
            try:
                for attempt in range(2):
                    data = requests.get(f"{api_base_url}/current.json", params=params, timeout=10)
                    data.raise_for_status()
                    if data.status_code != 200:
                        print("Viga andmete saamises")
                        continue
                    vastus = data.json()

                    city_data.update({"location" : vastus["location"]["name"],
                                      "local_time" : vastus["location"]["localtime"],
                                      "temperature" : vastus["current"]["temp_c"],
                                      "wind_speed" : vastus["current"]["wind_kph"],
                                      "humidity" : vastus["current"]["humidity"],
                                      "uv_index" : vastus["current"]["uv"]
                                      })

                    kas_onnestus = save_todays_weather_data(city_data, todays_data_filename)
                    if kas_onnestus:
                        city_loendur += 1
                    break
            except requests.exceptions.RequestException as e:
                print("viga")
                if attempt == 1:
                    raise
                time.sleep(0.3)
                continue

        if city_loendur == 0:
            print("Viga andmetes")
            return None
        return city_loendur

    except Exception as e:
        print(e)
        return None

def save_todays_weather_data(city_data, todays_data_filename):
    if not city_data:
        print("Vigased linna andmed")
        return False
    try:
        with open(todays_data_filename, 'a', encoding="utf-8") as f:
            f.write(f"Linn: {city_data['location']}\n"
                    f"Kohalik aeg: {city_data['local_time']}\n"
                    f"Temperatuur:{city_data['temperature']} °C\n"
                    f"Tuule kiirus: {city_data['wind_speed']} km/h\n"
                    f"Õhuniiskus: {city_data['humidity']}\n"
                    f"UV indeks: {city_data['uv_index']}\n\n\n"
                    )

            return True
    except Exception as e:
        print(e)
        return False


def get_weather_forecast_multiple_cities(api_base_url, api_key, cities):
    forecast_all = {}
    city_forecast_data = {}

    try:
        for query in cities:
            three_days = []
            params = {
                'key': api_key,
                'q': query,
                'days' : 3
            }
            try:
                for attempt in range(2):
                    try:
                        data = requests.get(f"{api_base_url}/forecast.json", params=params, timeout=10)
                        data.raise_for_status()
                        if data.status_code != 200:
                            print("Viga andmete saamises")
                            continue
                        vastus = data.json()

                        day0 = vastus["forecast"]["forecastday"][0]
                        day_info = day0["day"]

                        forecast_all[query] = {
                            "date": day0["date"],
                            "location": vastus["location"]["name"],
                            "temperature_avg_c": day_info["avgtemp_c"],
                            "wind_kph": day_info["maxwind_kph"],
                            "humidity": day_info["avghumidity"],
                            "uv_index": day_info["uv"],
                        }

                        #Kolme päev forecast listi
                        for day in vastus["forecast"]["forecastday"]:
                            three_days.append({
                                "date": day["date"],
                                "temperature": day["day"]["avgtemp_c"],
                                "max_wind_speed": day["day"]["maxwind_kph"],
                                "humidity": day["day"]["avghumidity"],
                                "uv_index": day["day"]["uv"],
                            })

                        city_forecast_data[query] = three_days
                    except KeyError as e:
                        print(e)
                        continue

                    break

            except requests.exceptions.RequestException:
                if attempt == 1:
                    raise
                time.sleep(0.3)

        #Salvestame kõik andmed korraga jsoni
        onnestus = save_forecast_weather_data(forecast_data=city_forecast_data)
        return onnestus

    except Exception as e:
        print(e)
        return False

def save_forecast_weather_data(forecast_data, forecast_data_filename = "weather_forecast_data.json"):
    if not forecast_data:
        print("Viga andmetes")
        return None

    try:
        with open(forecast_data_filename, 'w', encoding="utf-8") as f:
            json.dump(forecast_data, f, indent=4, ensure_ascii=False)
            print("Success")
        return True

    except Exception as e:
        print(e)
        return None


def main():
    api_base_url = "http://api.weatherapi.com/v1"
    cities = [
        "Tallinn", "Riga", "Vilnius", "Helsinki",
        "Stockholm", "Warsaw", "Copenhagen",
        "Amsterdam", "Madrid", "London"
    ]

    api_key = read_api_key("weather_api_key.py")
    data = get_weather_data_multiple_cities(api_base_url, api_key, cities)
    forecast = get_weather_forecast_multiple_cities(api_base_url, api_key, cities)
    if forecast:
        print(f"Laadin API võtit\n"
              f"API võti laetud: {len(api_key)} tähemärki\n"
              f"=== Hangin praeguseid ilmaandmeid {data} linna kohta ===\n"
              f"=== Salvestan praeguseid andmeid ===\n"
              f"=== Hangin ilma prognoosi ===\n"
              f"=== Salvestan prognoosi andmeid ===\n"
              f"Andmed salvestatud Jsoni")
    else:
        print("Viga andmete salvestamises.")




if __name__ == "__main__":
    main()
