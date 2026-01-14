# Impordime hashlib mooduli
import hashlib

# Impordime json mooduli, et salvestada andmeid JSON-faili
import json


class ParooliHaldur:
    # KLASSIMUUTUJA – ühine kõigile ParooliHaldur objektidele
    # Siia salvestatakse kasutajanimed ja nende paroolide hashid
    _paroolid = {}

    def __init__(self, kasutajanimi):
        # Igal objektil on oma kasutajanimi
        self._kasutajanimi = kasutajanimi

        # Parooli hash alguses puudub
        self._parool_hash = None

    # Getter – võimaldab parooli hashi luged...meetod, millega loetakse objekti andmeid.
    @property
    def parool_hash(self):
        if self._parool_hash is None:
            return None
        return self._parool_hash

    # Setter – käivitatakse, kui määrame parool_hash = "parool"...meetod, millega muudetakse objekti andmeid kontrollitult.
    @parool_hash.setter
    def parool_hash(self, parool):
        # Kontrollime, kas parool vastab nõuetele
        vastus_bool, vastus_str = ParooliHaldur.valideeri_parool(parool)

        # Kui parool ei ole sobiv, väljastame vea
        if vastus_bool == False:
            return print(f"Viga kasutajal {self._kasutajanimi} : {vastus_str}")

        # Krüpteerime parooli ja salvestame selle
        self._parool_hash = ParooliHaldur.krüpteeri_parool(parool)

        # Lisame kasutaja ja tema parooli hashi klassimuutujasse
        ParooliHaldur._paroolid[self._kasutajanimi] = self._parool_hash

    # Staatiline meetod – ei kasuta ei self ega cls
    @staticmethod
    def valideeri_parool(parool):
        # Kontrollime parooli pikkust
        if len(parool) < 8:
            return (False, "Parool peab olema vähemalt 8 tähemärki")

        # Kontrollime, kas paroolis on suurtäht
        if not any(c.isupper() for c in parool):
            return (False, "Parool peab sisaldama suurtähte")

        # Kontrollime, kas paroolis on number
        if not any(c.isdigit() for c in parool):
            return (False, "Parool peab sisaldama numbrit")

        # Kui kõik tingimused on täidetud
        return (True, "Parool on tugev")

    # Staatiline meetod parooli krüpteerimiseks
    @staticmethod
    def krüpteeri_parool(parool):
        # SHA-256 räsi, parooli ei salvestata kunagi tekstina
        return hashlib.sha256(parool.encode()).hexdigest()

    # Klassimeetod – töötab klassimuutujaga _paroolid
    @classmethod
    def salvesta_paroolid_faili(cls, failinimi="paroolid.json"):
        try:
            with open(failinimi, "w", encoding="utf-8") as file:
                json.dump(
                    cls._paroolid,  # salvestame kõik paroolid
                    file,
                    ensure_ascii=False,
                    indent=4
                )
        except Exception as e:
            print(e)

        print(f"Paroolid salvestatud faili: {failinimi}")

    # Klassimeetod, mis tagastab salvestatud paroolide arvu
    @classmethod
    def paroolide_arv(cls):
        return len(cls._paroolid)


# Käivitatakse ainult siis, kui fail käivitatakse otse
if __name__ == "__main__":
    # Loome esimese kasutaja
    kasutaja = ParooliHaldur("Märten")
    kasutaja.parool_hash = "Jaowkdo212"
    print(ParooliHaldur._paroolid)

    # Loome teise kasutaja
    kasutaja1 = ParooliHaldur("Märtdawden")
    kasutaja1.parool_hash = "Jaowawdadkdo212"
    print(ParooliHaldur._paroolid)

    # Salvestame paroolid faili
    kasutaja1.salvesta_paroolid_faili()
