# Impordid, mida programm vajab
# json – JSON failide lugemiseks ja kirjutamiseks
# csv – CSV failide lugemiseks
# hashlib – paroolide krüpteerimiseks (räsi arvutamiseks)

import json
import csv
import hashlib


class FailiLugeja:
    """
    Abiklass failidest andmete lugemiseks.

    Tegemist on utiliitklassiga – ta ei hoia oma olekut
    (ei ole vaja luua objekti), vaid pakub ainult
    staatilisi meetodeid failide lugemiseks.
    """

    @staticmethod
    def loe_csv_failist(failinimi):
        # Siia kogume CSV failist loetud andmed
        andmed = []

        try:
            # Avame faili lugemiseks UTF-8 kodeeringus
            with open(failinimi, encoding="utf-8") as f:
                read = f.readlines()

                # Kui fail on tühi, tagastame tühja listi
                if not read:
                    return andmed

                # Esimene rida on veerunimed (header)
                header = read[0].strip().split(",")

                # Ülejäänud read on andmeread
                for rida in read[1:]:
                    rida = rida.strip()

                    # Tühjad read jäetakse vahele
                    if not rida:
                        continue

                    väärtused = rida.split(",")

                    # Kui veergude arv ei klapi, jätame rea vahele
                    if len(väärtused) != len(header):
                        continue

                    # Teeme ühest reast sõnastiku
                    # võti = veeru nimi, väärtus = rea väärtus
                    andmed.append(dict(zip(header, väärtused)))

        except Exception as e:
            print(e)

        # Tagastame loetud andmed listina
        return andmed

    @staticmethod
    def loe_json_failist(failinimi):
        try:
            with open(failinimi, encoding="utf-8") as f:
                # json.load teisendab JSON faili Python objektiks
                return json.load(f)
        except Exception as e:
            print(e)
            return []


class ParooliHaldur:
    """
    Klass, mis tegeleb paroolide haldamisega.

    Vastutab:
    - parooli valideerimise eest
    - parooli krüpteerimise eest
    - paroolide salvestamise eest
    """

    # Klassimuutuja – ühine kõigi ParooliHaldur objektide vahel
    _paroolid = {}

    def __init__(self, kasutajanimi):
        # Iga objekt on seotud konkreetse kasutajaga
        self._kasutajanimi = kasutajanimi
        self._parool_hash = None

    @property
    def parool_hash(self):
        # Getter – võimaldab parooli räsi lugeda
        return self._parool_hash

    @parool_hash.setter
    def parool_hash(self, parool):
        # Setter – määrab parooli kontrollitult

        # Kontrollime, kas parool vastab nõuetele
        ok, msg = ParooliHaldur.valideeri_parool(parool)
        if not ok:
            print(f"Viga kasutajal {self._kasutajanimi}: {msg}")
            return

        # Krüpteerime parooli (räsi)
        self._parool_hash = ParooliHaldur.krüpteeri_parool(parool)

        # Salvestame räsi klassimuutujasse
        ParooliHaldur._paroolid[self._kasutajanimi] = self._parool_hash

    @staticmethod
    def valideeri_parool(parool):
        # Kontrollime parooli tugevust
        if len(parool) < 8:
            return False, "Parool peab olema vähemalt 8 märki"
        if not any(c.isupper() for c in parool):
            return False, "Parool peab sisaldama suurtähte"
        if not any(c.isdigit() for c in parool):
            return False, "Parool peab sisaldama numbrit"
        return True, "OK"

    @staticmethod
    def krüpteeri_parool(parool):
        # Kasutame SHA-256 algoritmi
        # Tegemist on ühesuunalise krüpteerimisega
        return hashlib.sha256(parool.encode()).hexdigest()

    @classmethod
    def salvesta_paroolid_faili(cls, fail="paroolid.json"):
        # Klassimeetod, sest kasutab klassimuutujat _paroolid
        with open(fail, "w", encoding="utf-8") as f:
            json.dump(cls._paroolid, f, indent=4, ensure_ascii=False)

    @classmethod
    def paroolide_arv(cls):
        # Tagastab salvestatud paroolide arvu
        return len(cls._paroolid)


class Kasutaja:
    """
    Klass, mis esindab kasutajat süsteemis.
    """

    # Klassimuutuja – hoiab kõiki loodud kasutajaid
    kasutajad = []

    def __init__(self, kasutajanimi, eesnimi, perenimi, vanus):
        self.kasutajanimi = kasutajanimi
        self.taisnimi = f"{eesnimi} {perenimi}"
        self.vanus = int(vanus)

        # Lisame kasutaja üldisesse nimekirja
        Kasutaja.kasutajad.append(self)

    @staticmethod
    def loo_csv_reast(rida):
        # Loob kasutaja CSV rea põhjal
        osad = rida.split(",")
        return Kasutaja(osad[0], osad[1], osad[2], osad[3])

    @staticmethod
    def loo_json_objektist(obj):
        # Loob kasutaja JSON objektist
        return Kasutaja(
            obj["kasutajanimi"],
            obj["eesnimi"],
            obj["perenimi"],
            obj["vanus"]
        )

    def valideeri_kasutajanimi(self, nimi):
        # Kontrollime kasutajanime pikkust
        if len(nimi) < 3:
            return False, "Kasutajanimi liiga lühike"
        return True, "OK"

    @classmethod
    def kasutajate_statistika(cls):
        # Tagastab info, mitu kasutajat on loodud
        return f"Kasutajaid kokku: {len(cls.kasutajad)}"


def main():
    # Loeme kasutajad CSV failist
    csv_andmed = FailiLugeja.loe_csv_failist("kasutajad.csv")

    for rida in csv_andmed:
        kasutaja = Kasutaja.loo_csv_reast(",".join(rida.values()))

        ok, msg = kasutaja.valideeri_kasutajanimi(rida["kasutajanimi"])
        if not ok:
            print(msg)
            continue

        parool = ParooliHaldur(rida["kasutajanimi"])
        parool.parool_hash = rida["parool"]

        print(kasutaja.taisnimi, kasutaja.vanus)

    # Loeme kasutajad JSON failist
    json_andmed = FailiLugeja.loe_json_failist("kasutajad.json")

    for obj in json_andmed:
        kasutaja = Kasutaja.loo_json_objektist(obj)
        parool = ParooliHaldur(obj["kasutajanimi"])
        parool.parool_hash = obj["parool"]

    # Salvestame kõik paroolid faili
    ParooliHaldur.salvesta_paroolid_faili()

    # Kuvame statistika
    print(Kasutaja.kasutajate_statistika())
    print(f"Registreeritud paroole: {ParooliHaldur.paroolide_arv()}")


if __name__ == "__main__":
    main()
