import requests


def analyze_email_domains(base_api_url):
    # Kontrollime, et URL oleks string
    if not isinstance(base_api_url, str):
        print("Link pole str")
        return {}

    try:
        # Küsimme serverist kasutajad
        response = requests.get(f"{base_api_url}/users", timeout=10)
        response.raise_for_status()

        # Kui server ei vastanud korrektselt
        if response.status_code != 200:
            print("Viga andmete saamisel")
            return {}

        vastus = response.json()

        # Sõnastik emaili lõppude loendamiseks
        sonastik_emailid = {}

        # Käime kõik kasutajad läbi
        for email in vastus:
            mail = email["email"]

            # Võtame emaili lõpud (nt .com, .org)
            lopp = mail.split(".")
            lopp = lopp[-1]

            # Lisame punkti, kui seda pole
            if "." not in lopp:
                lopp = f".{lopp}"

            # Suurendame vastava lõpu loendurit
            sonastik_emailid[lopp] = sonastik_emailid.get(lopp, 0) + 1

        return sonastik_emailid

    except Exception as e:
        print(e)
        return {}
    except requests.exceptions.RequestException as e:
        print(e)
        return {}


def get_user_info(base_api_url, user_id):
    # Kontrollid
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return {}
    if not isinstance(user_id, int):
        print("Viga, user_id pole int")
        return {}

    try:
        # Küsimme konkreetse kasutaja info
        response = requests.get(f"{base_api_url}/users/{user_id}", timeout=10)
        response.raise_for_status()

        if response.status_code != 200:
            print("Viga andmete saamisel")
            return {}

        vastus = response.json()

        # Kui vastus on tühi
        if not vastus:
            return {}

        return vastus

    except Exception as e:
        print(e)
        return {}
    except requests.exceptions.RequestException as e:
        print(e)
        return {}


def get_user_posts(base_api_url, user_id):
    # Kontrollid
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return []
    if not isinstance(user_id, int):
        print("Viga, user_id pole int")
        return []

    try:
        # Küsimme kasutaja postitused
        response = requests.get(f"{base_api_url}/users/{user_id}/posts", timeout=10)
        response.raise_for_status()

        if response.status_code != 200:
            print("Viga andmete saamisel")
            return []

        vastus = response.json()

        if not vastus:
            return []

        # Tagastame postitused listina
        return vastus

    except Exception as e:
        print(e)
        return []
    except requests.exceptions.RequestException as e:
        print(e)
        return []


def count_user_comments(base_api_url, user_id):
    # Kontrollid
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return 0
    if not isinstance(user_id, int):
        print("Viga, user_id pole int")
        return 0

    try:
        # Saame kasutaja postitused
        postitused = get_user_posts(base_api_url, user_id)

        # Kogume postituste ID-d
        post_ids = []
        for post in postitused:
            post_ids.append(post["id"])

        # Küsimme kasutaja kommentaarid
        kommentaar = requests.get(
            f"{base_api_url}/users/{user_id}/comments", timeout=10
        )
        kommentaar.raise_for_status()

        if kommentaar.status_code != 200:
            print("Viga andmete saamisel")
            return 0

        vastus = kommentaar.json()

        # Loendame kommentaarid, mis kuuluvad kasutaja postitustele
        kommentaaride_arv = 0
        for k in vastus:
            if k["postId"] in post_ids:
                kommentaaride_arv += 1

        return kommentaaride_arv

    except Exception as e:
        print(e)
        return 0
    except requests.exceptions.RequestException as e:
        print(e)
        return 0


def generate_users_report(base_api_url, filename="users_raport.txt"):
    # Kontrollid
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return
    if not isinstance(filename, str):
        print("Viga, failinimi pole str")
        return

    # Küsimme kõik kasutajad
    response = requests.get(f"{base_api_url}/users", timeout=10)
    response.raise_for_status()

    if response.status_code != 200:
        print("Viga andmete saamisel")
        return

    vastus = response.json()

    # Käime kõik kasutajad läbi
    for user in vastus:
        if "id" not in user:
            continue

        user_id = user["id"]

        info = get_user_info(base_api_url, user_id)
        posts = get_user_posts(base_api_url, user_id)
        kokku = count_user_comments(base_api_url, user_id)

        if not info or not posts:
            continue

        # Kirjutame raporti faili
        with open(filename, "a", encoding="utf-8") as f:
            f.write(
                f"\n\nKASUTAJA {user_id} RAPORT\n"
                f"Nimi: {info['name']}\n"
                f"Email: {info['email']}\n"
                f"Telefon: {info['phone']}\n"
                f"Veebileht: {info['website']}\n"
                f"Aadress: {info['address']['street']}, "
                f"{info['address']['city']} {info['address']['zipcode']}\n"
                f"Ettevõte: {info['company']['name']}\n\n"
            )

            f.write("Postitused:\n")
            for i, post in enumerate(posts[:10]):
                f.write(f"{i + 1}. {post['title']}\n")

            f.write(f"Kokku kommentaare: {kokku}\n")


def main():
    base_api_url = "https://jsonplaceholder.typicode.com"

    # Analüüsime emailide lõppe
    tulemus = analyze_email_domains(base_api_url)
    for domeen, kogus in tulemus.items():
        print(f"{domeen}: {kogus} kasutajat")

    # Loome raporti faili
    generate_users_report(base_api_url, "users_raport.txt")


if __name__ == "__main__":
    main()
