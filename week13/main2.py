import csv        # CSV (comma-separated values) failide lugemiseks
import json       # JSON andmete lugemiseks ja salvestamiseks
import hashlib    # Paroolide räsimiseks (turvaline ühesuunaline krüpteerimine)


class FailiLugeja:
    """
    Utiliitklass failide lugemiseks.

    See klass ei esinda ühtegi konkreetset objekti,
    vaid pakub funktsionaalsust.
    Seetõttu on kõik meetodid staatilised.
    """

    @staticmethod
    def loe_csv_failist(failinimi):
        # List, kuhu kogutakse CSV failist loetud kasutajad
        andmed = []

        try:
            # Avame faili lugemiseks
            with open(failinimi, encoding="utf-8") as f:
                read = f.readlines()

                # Kui fail on tühi, pole midagi töödelda
                if not read:
                    return andmed

                # Esimene rida on päis (veerunimed)
                header = read[0].strip().split(",")

                # Läbime andmeread
                for rida in read[1:]:
                    rida = rida.strip()

                    # Tühjad read jäetakse vahele
                    if not rida:
                        continue

                    values = rida.split(",")

                    # Kui veergude arv ei klapi, on rida vigane
                    if len(values) != len(header):
                        continue

                    # Teisendame rea sõnastikuks
                    andmed.append(dict(zip(header, values)))

        except Exception as e:
            # Kui fail puudub või on vigane
            print(e)

        return andmed

    @staticmethod
    def loe_json_failist(failinimi):
        """
        Loeb JSON faili ja teisendab selle Python andmestruktuuriks.
        """
        try:
            with open(failinimi, encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(e)
            return []


class ParooliHaldur:
    """
    Vastutab paroolidega seotud loogika eest.

    Paroolid valideeritakse, räsitakse ja
    salvestatakse turvalisel kujul.
    """

    # Klassimuutuja – kõigi kasutajate parooliräsid hoitakse siin
    _paroolid = {}

    def __init__(self, kasutajanimi):
        # Iga ParooliHaldur objekt on seotud ühe kasutajaga
        self._kasutajanimi = kasutajanimi
        self._parool_hash = None

    @property
    def parool_hash(self):
        """
        Getter – võimaldab parooli räsi lugemist,
        kuid ei luba seda otse muuta.
        """
        return self._parool_hash

    @parool_hash.setter
    def parool_hash(self, parool):
        """
        Setter – käivitub parooli määramisel.

        Siin tehakse kõik vajalikud kontrollid
        enne, kui parool salvestatakse.
        """

        ok, msg = ParooliHaldur.valideeri_parool(parool)
        if not ok:
            print(f"Viga kasutajal {self._kasutajanimi}: {msg}")
            return

        # Räsime parooli
        self._parool_hash = ParooliHaldur.krüpteeri_parool(parool)

        # Salvestame tulemuse klassimuutujasse
        ParooliHaldur._paroolid[self._kasutajanimi] = self._parool_hash

    @staticmethod
    def valideeri_parool(parool):
        """
        Kontrollib, kas parool vastab miinimumnõuetele.
        """
        if len(parool) < 8:
            return False, "Parool liiga lühike"
        if not any(c.isupper() for c in parool):
            return False, "Parool peab sisaldama suurtähte"
        if not any(c.isdigit() for c in parool):
            return False, "Parool peab sisaldama numbrit"
        return True, "OK"

    @staticmethod
    def krüpteeri_parool(parool):
        """
        Räsib parooli SHA-256 algoritmiga.
        See tähendab, et algset parooli ei saa tagasi.
        """
        return hashlib.sha256(parool.encode()).hexdigest()

    @classmethod
    def salvesta_paroolid_faili(cls, fail="paroolid.json"):
        """
        Salvestab kõik parooliräsid JSON faili.
        """
        with open(fail, "w", encoding="utf-8") as f:
            json.dump(cls._paroolid, f, indent=4, ensure_ascii=False)

    @classmethod
    def paroolide_arv(cls):
        # Tagastab salvestatud paroolide arvu
        return len(cls._paroolid)


class Kasutaja:
    """
    Klass, mis esindab ühte kasutajat süsteemis.
    """

    # Klassimuutuja – kõik loodud kasutajad
    kasutajad = []

    def __init__(self, kasutajanimi, eesnimi, perenimi, vanus):
        self.kasutajanimi = kasutajanimi
        self.taisnimi = f"{eesnimi} {perenimi}"
        self.vanus = int(vanus)

        # Lisame kasutaja üldisesse nimekirja
        Kasutaja.kasutajad.append(self)

    @staticmethod
    def loo_csv_reast(rida):
        """
        Loob Kasutaja objekti CSV rea põhjal.
        """
        osad = rida.split(",")
        return Kasutaja(osad[0], osad[1], osad[2], osad[3])

    @staticmethod
    def loo_json_objektist(obj):
        """
        Loob Kasutaja objekti JSON objektist.
        """
        return Kasutaja(
            obj["kasutajanimi"],
            obj["eesnimi"],
            obj["perenimi"],
            obj["vanus"]
        )

    def valideeri_kasutajanimi(self, nimi):
        """
        Kontrollib kasutajanime lihtsat reeglit.
        """
        if len(nimi) < 3:
            return False, "Kasutajanimi liiga lühike"
        return True, "OK"

    @classmethod
    def kasutajate_statistika(cls):
        """
        Tagastab info, kui palju kasutajaid on loodud.
        """
        return f"Kasutajaid kokku: {len(cls.kasutajad)}"


def main():
    """
    Programmi põhiloogika.
    """

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

    ParooliHaldur.salvesta_paroolid_faili()

    print(Kasutaja.kasutajate_statistika())
    print("Paroole:", ParooliHaldur.paroolide_arv())


if __name__ == "__main__":
    main()
