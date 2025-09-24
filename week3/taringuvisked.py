import random

def taringuvise():

    while True:
        print("Kirjuta 'veereta', et visata täringut.")
        print("Kirjuta 'lõpp', et programm lõpetada.")
        kasutaja_sisend = input("Sisend: ").lower().strip()
        print(f"kasutaja sisend: {kasutaja_sisend}")
        if kasutaja_sisend == "veereta":
            taringu_tulemus = random.randint(1, 6)
            print(f"Täring: {taringu_tulemus}")
            if taringu_tulemus == 6:
                print("Said kuue! Lõpp. ")
                break
        elif kasutaja_sisend == "lõpp":
            print("Programm lõpetatud.")
            break
        else:
            print("Veereta")
if __name__ == "__main__":
    main()

