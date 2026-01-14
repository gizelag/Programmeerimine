from datetime import datetime
# Impordime datetime klassi, et saaksime töötada kuupäevadega (nt vanuse arvutamine)


class Kasutaja:
    # Klass, mis esindab ühte kasutajat süsteemis

    _kasutajate_arv = 0
    # Klassimuutuja – hoiab arvestust, mitu Kasutaja objekti on loodud


    def __init__(self, kasutajanimi: str, eesnimi: str, perenimi: str, synnikuupaev: datetime):
        # Konstruktor – määrab uue kasutaja algandmed

        self.kasutajanimi = kasutajanimi
        # Avalik atribuut, mida saab otse kasutada

        self._eesnimi = eesnimi
        self._perenimi = perenimi
        self._synnikuupaev = synnikuupaev
        # Privaatseks mõeldud atribuudid (konventsioon _),
        # neid kasutatakse klassi sees

        Kasutaja._kasutajate_arv += 1
        # Suurendame klassimuutujat iga uue kasutaja loomisel


    @property
    def taisnimi(self):
        # Property – võimaldab saada kasutaja täisnime
        # Kasutatakse nagu atribuut: kasutaja.taisnimi
        return self._eesnimi + " " + self._perenimi


    @property
    def vanus(self):
        # Arvutab kasutaja vanuse jooksva aasta ja sünniaasta põhjal
        return datetime.now().year - self._synnikuupaev.year


    @classmethod
    def loo_csv_reast(cls, csv_string):
        # Klassimeetod – loob Kasutaja objekti CSV-formaadis tekstireast
        # Näide: "kasutajanimi,eesnimi,perenimi,YYYY-MM-DD"

        osad = csv_string.split(",")
        # Jagame CSV-stringi osadeks

        synnikuupaev = osad[3]
        synnikuupaev_obj = datetime.strptime(synnikuupaev, '%Y-%m-%d')
        # Teisendame kuupäeva stringist datetime objektiks

        return Kasutaja(osad[0], osad[1], osad[2], synnikuupaev_obj)
        # Tagastame uue Kasutaja objekti


    @classmethod
    def loo_json_objektist(cls, registreeritud_kasutajad_dict):
        # Klassimeetod – loob Kasutaja objekti sõnastikust (nt JSON-ist)

        # Eeldame, et sõnastikul on kindlad võtmed
        kasutajanimi = registreeritud_kasutajad_dict['kasutajanimi']
        eesnimi = registreeritud_kasutajad_dict['eesnimi']
        perenimi = registreeritud_kasutajad_dict['perenimi']
        synnikuupaev = datetime.fromisoformat(registreeritud_kasutajad_dict['synnikuupaev'])
        # ISO-kuupäeva string teisendatakse datetime objektiks

        return Kasutaja(kasutajanimi, eesnimi, perenimi, synnikuupaev)


    @classmethod
    def kasutajate_statistika(cls):
        # Tagastab tekstilise info kasutajate koguarvu kohta
        return f"Süsteemis on {Kasutaja._kasutajate_arv} kasutajat"


    @staticmethod
    def valideeri_kasutajanimi(kasutajanimi):
        # Staatiline meetod – kontrollib kasutajanime reegleid
        # Ei kasuta klassi ega objekti andmeid

        if len(kasutajanimi) < 3:
            return (False, f"Kasutajanimi ({kasutajanimi}) peab olema vähemalt 3 tähemärki")

        if kasutajanimi.isalnum() is False:
            return (False, f"Kasutajanimi ({kasutajanimi}) võib sisaldada ainult tähti ja numbreid")

        return (True, "OK")


if __name__ == "__main__":
    # See osa käivitub ainult siis, kui faili otse käivitada

    kasutaja = Kasutaja("Julpa", "Märten", "Pall", "2004-01-15")
    # Loome kasutaja käsitsi (NB! siin on sünnikuupäev stringina)

    kasutaja1 = kasutaja.loo_csv_reast("Julpa,Märten1, Pall,2004-01-16")
    # Loome kasutaja CSV-reast klassimeetodi abil

    print(kasutaja1.taisnimi)
    # Kuvame kasutaja täisnime läbi property

    registreeritud_kasutajad_dict = {
        "kasutajanimi": "lottebiceps",
        "eesnimi": "Lotte",
        "perenimi": "Muskel",
        "synnikuupaev": "2000-01-15",
        "parool": "LotteStrong1"
    }
    # Näidis kasutaja andmed sõnastikuna (nt JSON-ist)

    print(kasutaja.kasutajate_statistika())
    # Kuvame kasutajate koguarvu

    pool, tekst = Kasutaja.valideeri_kasutajanimi("Märten")
    # Kontrollime kasutajanime sobivust

    print(tekst)
    print(Kasutaja.kasutajate_statistika())
