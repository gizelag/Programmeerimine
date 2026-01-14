# Impordime json mooduli JSON-failide lugemiseks
import json


class FailiLugeja:
    # Staatiline meetod CSV faili lugemiseks
    @staticmethod
    def loe_csv_failist(failinimi):

        # Siia kogume CSV-st loetud andmed
        andme_list_csv = []

        try:
            # Avame faili lugemiseks UTF-8 kodeeringuga
            with open(failinimi, encoding="utf-8") as f:

                # Loeme kõik read faili mällu
                read = f.readlines()

                # Kui fail on tühi, tagastame tühja listi
                if not read:
                    return andme_list_csv

                # Esimene rida on päis (veeru nimed)
                header = read[0].strip().split(",")

                # Käime läbi kõik andmeread (alates teisest reast)
                for rida in read[1:]:

                    # Eemaldame reavahetused ja tühikud
                    rida = rida.strip()

                    # Kui rida on tühi, jätame vahele
                    if not rida:
                        continue

                    # Jagame rea väärtusteks
                    väärtused = rida.split(",")

                    # Kui veergude arv ei klapi päisega, jätame rea vahele
                    if len(väärtused) != len(header):
                        continue

                    # Seome päised ja väärtused sõnastikuks
                    andme_list_csv.append(dict(zip(header, väärtused)))

        # Kui tekib viga (nt fail puudub), prindime veateate
        except Exception as e:
            print(e)

        # Tagastame loetud CSV andmed listina
        return andme_list_csv

    # Staatiline meetod JSON faili lugemiseks
    @staticmethod
    def loe_json_failist(failinimi):
        try:
            # Avame JSON faili
            with open(failinimi, encoding="utf-8") as f:

                # json.load() teisendab JSON sisu Python andmeteks
                return json.load(f)

        # Kui fail puudub või on vigane, tagastame tühja listi
        except Exception as e:
            print(e)
            return []
