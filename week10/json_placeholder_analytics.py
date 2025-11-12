
import requests


def analyze_email_domains(base_api_url):
    if not isinstance(base_api_url, str):
        print("Link pole str")
        return {}

    try:
        response = requests.get(f"{base_api_url}/users", timeout= 10)
        response.raise_for_status()

        if response.status_code != 200:
            print("Viga andmete saamisel")
            return {}

        vastus = response.json()
        sonastik_emailid = {}
        for email in vastus:
            mail = email["email"]
            lopp = mail.split(".")
            lopp = lopp[-1]
            if "." not in lopp:
                lopp = f".{lopp}"
            sonastik_emailid[lopp] = sonastik_emailid.get(lopp, 0) + 1
        return sonastik_emailid

    except Exception as e:
        print(e)
        return {}
    except requests.exceptions.RequestException as e:
        print(e)
        return {}


def get_user_info(base_api_url, user_id):
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return {}
    if not isinstance(user_id, int):
        print("Viga, used_id pole int")
        return {}

    try:
        response = requests.get(f"{base_api_url}/users/{user_id}", timeout= 10)
        response.raise_for_status()
        if response.status_code != 200:
            print("Viga andmete saamisel")
            return {}
        vastus = response.json()
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
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return []
    if not isinstance(user_id, int):
        print("Viga, used_id pole int")
        return []

    try:
        response = requests.get(f"{base_api_url}/users/{user_id}/posts", timeout=10)
        response.raise_for_status()
        if response.status_code != 200:
            print("Viga andmete saamisel")
            return []
        vastus = response.json()
        if not vastus:
            return []
        post_list = []
        for post in vastus:
            post_list.append(post)

        return post_list

    except Exception as e:
        print(e)
        return []
    except requests.exceptions.RequestException as e:
        print(e)
        return []


def count_user_comments(base_api_url, user_id):
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return 0
    if not isinstance(user_id, int):
        print("Viga, used_id pole int")
        return 0

    try:
        kommentaarid = get_user_posts(base_api_url, user_id)
        if not kommentaarid:
            kommentaarid = []

        post_ids = []
        for key in kommentaarid:
            post_ids.append(key["id"])

        kommentaar = requests.get(f"{base_api_url}/users/{user_id}/comments", timeout=10)
        kommentaar.raise_for_status()
        if kommentaar.status_code != 200:
            print("Viga andmete saamisel")
            return 0

        vastus = kommentaar.json()
        kommentaaride_arv = 0
        for id in vastus:
            if id["postId"] in post_ids:
                kommentaaride_arv += 1

        return kommentaaride_arv

    except Exception as e:
        print(e)
        return 0
    except requests.exceptions.RequestException as e:
        print(e)
        return 0


def generate_users_report(base_api_url, filename = "users_raport.txt"):
    if not isinstance(base_api_url, str):
        print("Viga, url pole str")
        return
    if not isinstance(filename, str):
        print("Viga, used_id pole int")
        return
    response = requests.get(f"{base_api_url}/users", timeout=10)
    response.raise_for_status()

    if response.status_code != 200:
        print("Viga andmete saamisel")
        return {}

    vastus = response.json()
    try:
        for ids in vastus:
            user_id = ids["id"]
            if "id" not in ids:
                continue

            info = get_user_info(base_api_url, user_id)
            if not info:
                continue

            posts =  get_user_posts(base_api_url, user_id)
            if not posts:
                continue

            kokku = count_user_comments(base_api_url, user_id)
            arv = 10
            try:
                with open(filename, "a", encoding="utf-8") as f:

                    f.write(
                        f"\n\n\nKASUTAJA {user_id} RAPORT\n"
                        f"Nimi: {info['name']}\n"
                        f"Email: {info['email']}\n"
                        f"Telefon: {info['phone']}\n"
                        f"Veebileht: {info['website']}\n\n"
                        f"Aadress: {info['address']['street']}, {info['address']['city']} {info['address']['zipcode']}\n"
                        f"Ettevõte: {info['company']['name']}\n\n"
                    )
                    f.write(f"Postitused ({arv} tk):\n")
                    for index in range(arv):
                        f.write(f"{index+1}. {posts[index]['title']}\n")
                    f.write(f"Kokku kommentaare kasutaja postitustel: {kokku}")
            except Exception as e:
                print(e)
                continue

    except Exception as e:
        print(e)
        return
    except requests.exceptions.RequestException as e:
        print(e)
        return


def main():
    base_api_url = "https://jsonplaceholder.typicode.com"
    tulemus = analyze_email_domains(base_api_url)
    if tulemus != {}:
        for domeen, kogus in tulemus.items():
            print(f"{domeen}: {kogus} kasutajat")
    else:
        print("Viga: domeene ei suudetud analüüsida")

    generate_users_report(base_api_url, "users_raport.txt")

if __name__ == '__main__':
    main()
