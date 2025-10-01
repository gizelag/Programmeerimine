def loe_autode_andmed(failinimi):
    try:
        with open(failinimi, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError as e:
        print(f"Viga: Faili '{failinimi}' ei leitud, error: {e}")
        return None


def kontrolli_auto_andmeid(auto_rida):
    if auto_rida is None:
        return False
    if not ";" in auto_rida:
        return False
    try:
        rea_osad = auto_rida.split(";")
        if len(rea_osad) != 6:
            return False
        kast = rea_osad[4].strip()
        kast = kast.lower()
        if kast != "manuaal":
            return False
        auto_vanus = int(rea_osad[5].strip())
        if auto_vanus is None:
            return False
        if auto_vanus <= 2010:
            return False
        return True
    except ValueError:
        return


def filtreeri_ja_salvesta(autod_list):
    if autod_list is None:
        return
    sobivad_autod = ""
    try:
        for auto_rida in autod_list:
            auto_rida = auto_rida.strip()
            if not auto_rida:
                continue
            kontrolli = kontrolli_auto_andmeid(auto_rida)
            if kontrolli is True:
                sobivad_autod += f"{auto_rida}\n"
        kirjuta_filteeritud_autod(sobivad_autod)

    except Exception as e:
        print(e)

def  kirjuta_filteeritud_autod(sobivad_autod):
    try:
        fail_kuhu_kirjan = "filtreeritud_autod.txt"
        with open(fail_kuhu_kirjan, "w", encoding="utf-8") as file:
            file.write(sobivad_autod)
            print(f"Sobivad autod salvestatud faili '{fail_kuhu_kirjan}'")
    except Exception as e:
        print(f"Viga faili kirjutamisel: {e}")

def main():
    autod_list=loe_autode_andmed(failinimi="autode_andmed.txt")
    filtreeri_ja_salvesta(autod_list)

if __name__ == "__main__":
    main()