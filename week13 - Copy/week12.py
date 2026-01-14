# =========================
# KUUPÄEVA JA AJA TÖÖTLUS
# =========================
from datetime import datetime


# =========================
# KLASS: Kasutaja
# =========================
class Kasutaja:
    # KLASSIMUUTUJA
    # Kuulub klassile, mitte konkreetsele objektile
    # Loendab, mitu kasutajat on loodud
    _kasutajate_arv = 0

    def __init__(self, kasutajanimi: str, eesnimi: str, perenimi: str, synnikuupaev: datetime):
        # Avalik atribuut – ligipääsetav otse
        self.kasutajanimi = kasutajanimi

        # "Kaitstud" atribuudid (_)
        # Tähendab: kasuta läbi property, mitte otse
        self._eesnimi = eesnimi
        self._perenimi = perenimi
        self._synnikuupaev = synnikuupaev

        # Iga uue kasutaja loomisel suurendame loendurit
        Kasutaja._kasutajate_arv += 1

    # =========================
    # PROPERTY – GETTER
    # =========================
    # Võimaldab kutsuda nagu omadust:
    # kasutaja.taisnimi (mitte kasutaja.taisnimi())
    @property
    def taisnimi(self):
        # Koostame täisnime ees- ja perenimest
        return self._eesnimi + " " + self._perenimi

    # =========================
    # PROPERTY – VANUSE ARVUTUS
    # =========================
    @property
    def vanus(self):
        # Praegune aasta miinus sünniaasta
        # (lihtsustatud arvutus)
        return datetime.now().year - self._synnikuupaev.year

    # =========================
    # CLASSMETHOD – OBJEKT CSV REAST
    # =========================
    @classmethod
    def loo_csv_reast(cls, csv_string):
        # csv_string näide:
        # "kasutajanimi,eesnimi,perenimi,YYYY-MM-DD"

        # Jagame stringi osadeks
        osad = csv_string.split(",")

        # Sünnikuupäev on neljas element
        synnikuupaev = osad[3]

        # Teeme stringist datetime objekti
        synnikuupaev_obj = datetime.strptime(synnikuupaev, '%Y-%m-%d')

        # Loome ja tagastame Kasutaja objekti
        return Kasutaja(osad[0], osad[1], osad[2], synnikuupaev_obj)

    # =========================
    # CLASSMETHOD – OBJEKT JSON SÕNASTIKUST
    # =========================
    @classmethod
    def loo_json_objektist(cls, registreeritud_kasutajad_dict):
        # Sõnastik peab sisaldama võtmeid:
        # 'kasutajanimi', 'eesnimi', 'perenimi', 'synnikuupaev'

        kasutajanimi = registreeritud_kasutajad_dict['kasutajanimi']
        eesnimi = registreeritud_kasutajad_dict['eesnimi']
        perenimi = registreeritud_kasutajad_dict['perenimi']

        # ISO-kuupäev string → datetime objekt
        synnikuupaev = datetime.fromisoformat(
            registreeritud_kasutajad_dict['synnikuupaev']
        )

        # Tagastame uue Kasutaja objekti
        return Kasutaja(kasutajanimi, eesnimi, perenimi, synnikuupaev)

    # =========================
    # CLASSMETHOD – STATISTIKA
    # =========================
    @classmethod
    def kasutajate_statistika(cls):
        # Kasutab klassimuutujat
        return f"Süsteemis on {Kasutaja._kasutajate_arv} kasutajat"

    # =========================
    # STATICMETHOD – KASUTAJANIME KONTROLL
    # =========================
    @staticmethod
    def valideeri_kasutajanimi(kasutajanimi):
        # Kasutajanimi peab olema vähemalt 3 tähemärki
        if len(kasutajanimi) < 3:
            return (
                False,
                f"Kasutajanimi ({kasutajanimi}) peab olema vähemalt 3 tähemärki"
            )

        # Lubatud on ainult tähed ja numbrid
        if kasutajanimi.isalnum() is False:
            return (
                False,
                f"Kasutajanimi ({kasutajanimi}) võib sisaldada ainult tähti ja numbreid"
            )

        # Kui kõik korras
        return (True, "OK")


# =========================
# TESTIMINE – KÄIVITUB AINULT OTSE FAILI KÄIVITADES
# =========================
if __name__ == "__main__":

    # Loome kasutaja käsitsi
    kasutaja = Kasutaja(
        "Julpa",
        "Märten",
        "Pall",
        datetime.strptime("2004-01-15", "%Y-%m-%d")
    )

    # Loome kasutaja CSV reast
    kasutaja1 = Kasutaja.loo_csv_reast(
        "Julpa,Märten1,Pall,2004-01-16"
    )

    # Kasutame property't
    print(kasutaja1.taisnimi)

    # JSON-sarnane sõnastik
    registreeritud_kasutajad_dict = {
        "kasutajanimi": "lottebiceps",
        "eesnimi": "Lotte",
        "perenimi": "Muskel",
        "synnikuupaev": "2000-01-15",
        "parool": "LotteStrong1"
    }

    # Kuvame kasutajate arvu
    print(Kasutaja.kasutajate_statistika())

    # Kontrollime kasutajanime
    pool, tekst = Kasutaja.valideeri_kasutajanimi("Märten")
    print(tekst)

    # Kuvame uuesti statistika
    print(Kasutaja.kasutajate_statistika())
