import random  # Moodul juhuslike arvude genereerimiseks


def taringuvise():
    # Lõputu tsükkel, mis töötab kuni kasutaja lõpetab programmi
    while True:
        # Kasutajale kuvatavad juhised
        print("Kirjuta 'veereta', et visata täringut.")
        print("Kirjuta 'lõpp', et programm lõpetada.")

        # Kasutaja sisendi lugemine ja normaliseerimine (väiketähed, tühikute eemaldus)
        kasutaja_sisend = input("Sisend: ").lower().strip()
        print(f"kasutaja sisend: {kasutaja_sisend}")

        # Kui kasutaja soovib täringut veeretada
        if kasutaja_sisend == "veereta":
            # Genereeritakse juhuslik arv vahemikus 1 kuni 6 (täringu vise)
            taringu_tulemus = random.randint(1, 6)
            print(f"Täring: {taringu_tulemus}")

            # Kontroll: kui visatakse 6, lõpetatakse tsükkel
            if taringu_tulemus == 6:
                print("Said kuue! Lõpp. ")
                break

        # Kui kasutaja soovib programmi lõpetada
        elif kasutaja_sisend == "lõpp":
            print("Programm lõpetatud.")
            break


    # Peafunktsioon, mis käivitab täringuviske loogika
    def main():
        taringuvise()

    # Kontroll, et programm käivituks ainult otse käivitamisel
    if __name__ == "__main__":
        main()
