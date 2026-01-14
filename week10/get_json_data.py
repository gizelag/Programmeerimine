import requests

def get_all_users(base_api_url):
    # Kontrollime, et URL oleks string
    if not isinstance(base_api_url, str):
        print("Viga: URL ei ole string")
        return {}

    try:
        # Teeme päringu API-le
        response = requests.get(base_api_url, timeout=10)

        # Kui server vastab veaga (nt 404, 500), viskab vea
        response.raise_for_status()

        # Kontrollime, kas vastus on edukas
        if response.status_code != 200:
            print("Viga: server ei tagastanud korrektset vastust")
            return {}

        # Teisendame vastuse JSON-iks (list sõnastikest)
        vastus = response.json()

        # Siia kogume nimed ja emailid
        sonastik = {}

        # Käime kõik kasutajad läbi
        for user in vastus:
            nimi = user["name"]
            email = user["email"]
            sonastik[nimi] = email

        return sonastik

    except requests.exceptions.RequestException as e:
        # Kui internetiühendus või päring läheb valesti
        print("Võrguviga:", e)
        return {}
    except Exception as e:
        # Kõik muud ootamatud vead
        print("Üldine viga:", e)
        return {}


def get_user_count(users_data):
    # Kontrollime, et andmed oleksid sõnastik
    if not isinstance(users_data, dict):
        print("Viga: andmed ei ole dict")
        return None

    # Kui sõnastik on tühi
    if not users_data:
        print("Tühi dict")
        return None

    # Loendame kasutajad
    summa = 0
    for nimi, email in users_data.items():
        summa += 1

    return summa


def main():
    # API aadress, kust kasutajaid küsime
    base_api_url = "https://jsonplaceholder.typicode.com/users"

    # Toome kasutajad
    tulemus = get_all_users(base_api_url)

    # Loendame kasutajad
    summa = get_user_count(tulemus)

    # Kui midagi läks valesti
    if tulemus == {} and summa is None:
        print("Viga: ei suutnud andmeid hankida")
        return

    # Prindime kasutajad koos emailidega
    for index, (nimi, email) in enumerate(tulemus.items()):
        print(f"{index + 1}. {nimi} ({email})")

    print("\nKASUTAJATE KOGU ARV:")
    print(f"Kasutajaid kokku on: {summa}")


if __name__ == "__main__":
    main()
