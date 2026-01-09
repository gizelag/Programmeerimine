from datetime import datetime

class Kasutaja:
    _kasutajate_arv = 0

    def __init__(self, kasutajanimi:str, eesnimi:str, perenimi:str, synnikuupaev:datetime):
        self.kasutajanimi = kasutajanimi
        self._eesnimi = eesnimi
        self._perenimi = perenimi
        self._synnikuupaev = synnikuupaev
        Kasutaja._kasutajate_arv += 1

    @property
    def taisnimi(self):
        return self._eesnimi + " " + self._perenimi

    @property
    def vanus(self):
        return datetime.now().year - self._synnikuupaev.year

    @classmethod
    def loo_csv_reast(cls,csv_string):
        #csv_string - "kasutajanimi,eesnimi,perenimi,YYYY-MM-DD"
        osad = csv_string.split(",")
        synnikuupaev = osad[3]
        synnikuupaev_obj = datetime.strptime(synnikuupaev, '%Y-%m-%d')
        return Kasutaja(osad[0], osad[1],osad[2], synnikuupaev_obj)

    @classmethod
    def loo_json_objektist(cls, registreeritud_kasutajad_dict):

        #Sõnastik võtmetega 'kasutajanimi', 'eesnimi', 'perenimi', 'synnikuupaev'
        kasutajanimi = registreeritud_kasutajad_dict['kasutajanimi']
        eesnimi = registreeritud_kasutajad_dict['eesnimi']
        perenimi = registreeritud_kasutajad_dict['perenimi']
        synnikuupaev = datetime.fromisoformat(registreeritud_kasutajad_dict['synnikuupaev'])

        return Kasutaja(kasutajanimi, eesnimi,perenimi, synnikuupaev)

    @classmethod
    def kasutajate_statistika(cls):
        return f"Süsteemis on {Kasutaja._kasutajate_arv} kasutajat"

    @staticmethod
    def valideeri_kasutajanimi(kasutajanimi):
        if len(kasutajanimi) < 3:
            return (False, f"Kasutajanimi ({kasutajanimi}) peab olema vähemalt 3 tähemärki")
        if kasutajanimi.isalnum() is False:
            return (False, f"Kasutajanimi ({kasutajanimi}) võib sisaldada ainult tähti ja numbreid")

        return (True, "OK")

if __name__ == "__main__":
    kasutaja = Kasutaja("Julpa","Märten", "Pall", "2004-01-15")
    kasutaja1= kasutaja.loo_csv_reast("Julpa,Märten1, Pall,2004-01-16")

    print(kasutaja1.taisnimi)

    registreeritud_kasutajad_dict = {"kasutajanimi": "lottebiceps",
                                     "eesnimi": "Lotte",
                                     "perenimi": "Muskel",
                                     "synnikuupaev": "2000-01-15",
                                     "parool": "LotteStrong1"}

    print(kasutaja.kasutajate_statistika())
    pool, tekst = Kasutaja.valideeri_kasutajanimi("Märten")
    print(tekst)
    print(Kasutaja.kasutajate_statistika())