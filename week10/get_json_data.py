import requests

def get_user_count():import json
import requests

def get_all_users(base_api_url):
    if not isinstance(base_api_url, str):
        print("File pole")
        return {}

    try:
        response = requests.get(base_api_url, timeout = 10)
        response.raise_for_status()
        if response.status_code != 200:
            print("Viga, faili ei saanud lugeda serverist")
            return {}
        vastus = response.json()

        sonastik = {}

        for user in vastus:
            nimi = user["name"]
            email = user["email"]
            sonastik[nimi] = email
        return sonastik
    except Exception as e:
        print(e)
        return {}
    except requests.exceptions.RequestException as e:
        print(e)
        return {}

def get_user_count(users_data):
    if not isinstance(users_data, dict):
        print("Viga")
        return None

    if not users_data:
        print("TÃ¼hi dict")
        return None

    summa = 0
    for nimi, email in users_data.items():
        summa += 1

    return summa

def main():
    base_api_url = "https://jsonplaceholder.typicode.com/users"
    tulemus = get_all_users(base_api_url)
    summa = get_user_count(tulemus)

    if tulemus == {} and summa is None:
        print("Viga: ei suutnud andmeid hankida")

    for index, (nimi, email) in enumerate(tulemus.items()):
        print(f"{index+1}. {nimi} ({email})")

    print("KASUTAJATE KOGU ARV:")
    print(f"Kasutajaid kokku on: {summa}")

if __name__ == '__main__':
    main()