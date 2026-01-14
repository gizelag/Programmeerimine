from datetime import datetime


class Maja:
    """
    Klass Maja kirjeldab ühte konkreetset maja.
    Iga Maja objekt hoiab infot aadressi, ehitusaasta,
    korterite arvu ja elanike kohta.
    """

    def __init__(self, aadress: str, korterite_arv: int, ehitusaasta: int):
        # Konstruktor – käivitub automaatselt objekti loomisel
        # Paneb paika objekti algse oleku

        self._elanike_arv = 0            # privaatsed atribuudid (kokkuleppeliselt _)
        self._renoveeritud = False
        self._on_uus = False

        # Tüübikontroll – vale tüüpi andmeid ei lubata
        if not isinstance(aadress, str):
            raise TypeError("aadress peab olema string")
        if not isinstance(korterite_arv, int):
            raise TypeError("korterite arv peab olema int")
        if not isinstance(ehitusaasta, int):
            raise TypeError("ehitusaasta peab olema int")

        # Väärtuste sisuline kontroll
        if not aadress.strip():
            raise ValueError("aadress ei tohi olla tühi")
        if korterite_arv < 0:
            raise ValueError("korterite arv ei tohi olla negatiivne")
        if not Maja.on_kehtiv_aasta(ehitusaasta):
            raise ValueError("ehitusaasta ei ole lubatud vahemikus")

        # Andmete salvestamine objekti
        self._aadress = aadress
        self._korterite_arv = korterite_arv
        self._ehitusaasta = ehitusaasta

    @property
    def maja_vanus(self):
        # Property – arvutatud omadus
        # Kasutatakse nagu atribuuti: maja.maja_vanus
        return datetime.now().year - self._ehitusaasta #kutsun valja nagu muutujat aga kaivitub funktsioon

    @property
    def aadress(self):
        #  – tagastab aadressi
        return self._aadress

    @property
    def korterite_arv(self):
        return self._korterite_arv

    @property
    def ehitusaasta(self):
        return self._ehitusaasta

    @property
    def on_uus_maja(self):
        # Loogiline property – arvutab ise väärtuse
        self._on_uus = self._ehitusaasta > 2005
        return self._on_uus

    @property
    def elanike_tihedus(self):
        # Kui kortereid pole, väldime nulliga jagamist
        if self._korterite_arv == 0:
            return 0
        return round(self._elanike_arv / self._korterite_arv, 2)

    @property
    def renoveeritud(self):
        # Getter
        return self._renoveeritud

    @renoveeritud.setter
    def renoveeritud(self, uus_väärtus):
        # Setter – lubab väärtust muuta kontrollitult
        if not isinstance(uus_väärtus, bool):
            raise TypeError("renoveeritud peab olema boolean")
        self._renoveeritud = uus_väärtus

    @property
    def elanike_arv(self):
        return self._elanike_arv

    @elanike_arv.setter
    def elanike_arv(self, uus_arv):
        # Kaitseme objekti vale oleku eest
        if not isinstance(uus_arv, int):
            raise TypeError("elanike arv peab olema int")
        if uus_arv < 0:
            raise ValueError("elanike arv ei tohi olla negatiivne")
        self._elanike_arv = uus_arv

    @staticmethod
    def on_kehtiv_aasta(ehitusaasta):
        # Staticmethod – ei kasuta self ega cls
        # Lihtne abifunktsioon klassi loogika jaoks
        return 1800 <= ehitusaasta <= 2025

    def lisa_elanik(self):
        # Muudab objekti olekut
        self.elanike_arv += 1
        print(f"Majja {self._aadress} lisandus elanik. Kokku: {self._elanike_arv}")

    def eemalda_elanik(self):
        if self._elanike_arv > 0:
            self.elanike_arv -= 1
            print(f"Majast {self._aadress} lahkus elanik. Kokku: {self._elanike_arv}")
        else:
            print("Elanikke pole, ei saa eemaldada")

    def __str__(self):
        # Määrab, kuidas objekt print() käsuga kuvatakse
        reno = "Jah" if self._renoveeritud else "Ei"
        tyyp = "Uus maja" if self.on_uus_maja else "Vana maja"

        return (
            f"Maja: {self._aadress}\n"
            f"Ehitusaasta: {self._ehitusaasta}\n"
            f"Vanus: {self.maja_vanus} aastat\n"
            f"Korterite arv: {self._korterite_arv}\n"
            f"Elanike arv: {self._elanike_arv}\n"
            f"Elanike tihedus: {self.elanike_tihedus}\n"
            f"Renoveeritud: {reno}\n"
            f"Tüüp: {tyyp}\n"
        )


def main():
    # Programmi käivituspunkt
    maja1 = Maja("Tombi 10", 10, 2010)
    maja2 = Maja("Tombi 11", 5, 1999)

    maja1.lisa_elanik()
    maja1.renoveeritud = True

    print(maja1)
    print(maja2)


if __name__ == "__main__":
    main()
