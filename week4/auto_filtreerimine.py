# Loeb autode andmed tekstifailist
# Tagastab failist loetud read listina
def loe_autode_andmed(failinimi):
    try:
        # Avame faili lugemiseks UTF-8 kodeeringuga
        with open(failinimi, "r", encoding="utf-8") as file:
            return file.readlines()

    # Kui faili ei leita, anname kasutajale veateate
    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None


# Kontrollib, kas üks auto rida vastab etteantud tingimustele
def kontrolli_auto_andmeid(auto_rida):
    # Kui rida puudub, ei ole see sobiv
    if auto_rida is None:
        return False

    # Kontrollime, et eraldajaks oleks semikoolon
    if not ";" in auto_rida:
        return False

    try:
        # Jagame rea andmeväljadeks
        rea_osad = auto_rida.split(";")

        # Kontrollime, et andmeid oleks täpselt 6
        if len(rea_osad) != 6:
            return False

        # Käigukasti kontroll (peab olema manuaal)
        kast = rea_osad[4].strip()
        kast = kast.lower()
        if kast != "manuaal":
            return False

        # Võtame auto aasta ja teisendame täisarvuks
        auto_vanus = int(rea_osad[5].strip())

        # Kontroll, et aasta oleks olemas
        if auto_vanus is None:
            return False

        # Lubame ainult autod, mis on uuemad kui 2010
        if auto_vanus <= 2010:
            return False

        # Kui kõik kontrollid läbitud, on auto sobiv
        return True

    except ValueError:
        # Tekib siis, kui aastat ei saa arvuks teisendada
        return


# Filtreerib sobivad autod ja salvestab need faili
def filtreeri_ja_salvesta(autod_list):
    # Kui autode list puudub, lõpetame funktsiooni
    if autod_list is None:
        return

    # String, kuhu kogume sobivad autod
    sobivad_autod = ""

    try:
        # Läbime kõik autode read
        for auto_rida in autod_list:
            auto_rida = auto_rida.strip()

            # Jätame tühjad read vahele
            if not auto_rida:
                continue

            # Kontrollime, kas auto vastab tingimustele
            kontrolli = kontrolli_auto_andmeid(auto_rida)

            if kontrolli is True:
                sobivad_autod += f"{auto_rida}\n"

        # Kirjutame sobivad autod faili
        kirjuta_filteeritud_autod(sobivad_autod)

    except Exception as e:
        print(e)


# Salvestab filtreeritud autod eraldi tekstifaili
def kirjuta_filteeritud_autod(sobivad_autod):
    try:
        fail_kuhu_kirjan = "filtreeritud_autod.txt"

        # Avame faili kirjutamiseks
        with open(fail_kuhu_kirjan, "w", encoding="utf-8") as file:
            file.write(sobivad_autod)
            print(f"Sobivad autod salvestatud faili '{fail_kuhu_kirjan}'")

    except Exception as e:
        print(f"Viga faili kirjutamisel: {e}")


# Programmi käivituspunkt
def main():
    # Loeme autode andmed failist
    autod_list = loe_autode_andmed(failinimi="autode_andmed.txt")

    # Filtreerime ja salvestame sobivad autod
    filtreeri_ja_salvesta(autod_list)


# Tagab, et programm käivitub ainult otse faili käivitamisel
if __name__ == "__main__":
    main()
