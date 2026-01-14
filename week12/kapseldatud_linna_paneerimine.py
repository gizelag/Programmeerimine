class Maja:

    def __init__(self, aadress: str, korterite_arv: int, ehitusaasta: int): #loome konstruktori et anda algvaartused
        self._elanike_arv = 0
        self._renoveeritud = False
        self._on_uus = False

        if not isinstance(aadress, str):
            raise TypeError("aadress must be a string")
        if not isinstance(korterite_arv, int):
            raise TypeError("korterite arv must be a int")
        if not isinstance(ehitusaasta, int):
            raise TypeError("ehitusaasta must be a int")

        if not aadress.strip():
            raise ValueError("aadress ei tohi olla tühi")
        if korterite_arv < 0:
            raise ValueError("korterite arv must be positive")
        if Maja.on_kehtiv_aasta(ehitusaasta) is False:
            raise ValueError("ehitusaasta ei ole sobiv")

        self._ehitusaasta = ehitusaasta
        self._aadress = aadress
        self._korterite_arv = korterite_arv

    @property
    def maja_vanus(self):
        from datetime import datetime
        return datetime.now().year - self._ehitusaasta

    @property
    def aadress(self):
        return f"Maja aadress: {self._aadress}"

    @property
    def korterite_arv(self):
        return self._korterite_arv

    @property
    def ehitusaasta(self):
        return self._ehitusaasta

    @property
    def on_uus_maja(self):
        if self._ehitusaasta <= 2005:
            self._on_uus = False
            return False
        else:
            self._on_uus = True
            return True

    @property
    def elanike_tihedus(self):
        if self._korterite_arv == 0:
            return 0
        return round(self._elanike_arv / self._korterite_arv, 2)

    @property
    def renoveeritud(self):
        return self._renoveeritud

    @renoveeritud.setter
    def renoveeritud(self, uus_väärtus):
        if not isinstance(uus_väärtus, bool):
            raise TypeError(f"uus_väärtus peab olema bool, praegu on {type(uus_väärtus)}")
        self._renoveeritud = uus_väärtus
        print(f"Maja {self._aadress} on nüüd renoveeritud!")

    @property
    def elanike_arv(self):
        return self._elanike_arv

    @elanike_arv.setter
    def elanike_arv(self, uus_elanike_arv):
        if not isinstance(uus_elanike_arv, int):
            raise TypeError(f"Uus väärtus peab olema int, praegu on {type(uus_elanike_arv)}")
        if uus_elanike_arv < 0:
            raise ValueError("Uus väärtus peab olema positiivne")
        self._elanike_arv = uus_elanike_arv

    @staticmethod
    def on_kehtiv_aasta(ehitusaasta):
        if 1800 <= ehitusaasta <= 2025:
            return True
        return False

    def lisa_elanik(self):
        try:
            self.elanike_arv = self._elanike_arv + 1
            print(f"Majja {self._aadress} lisandus uus elanik. Elanikke kokku: {self._elanike_arv}")
        except ValueError as e:
            print(f"Viga elaniku lisamisel ({e})")

    def eemalda_elanik(self):
        if self._elanike_arv > 0:
            try:
                self.elanike_arv = self._elanike_arv - 1
                print(f"Majjast {self._aadress} eemaldati elanik. Elanikke kokku: {self._elanike_arv}")
            except ValueError as e:
                print(f"Viga elaniku eemaldamisel ({e})")
        else:
            print("Majas ei ole elanikke, ei saa eemaldada.")

    def __str__(self):
        tekst_renoveeritud = "Jah" if self._renoveeritud else "Ei"
        tekst_maja = "Uus maja" if self.on_uus_maja else "Vana maja"

        return (
            f"Maja – {self._aadress}\n"
            f"Ehitusaasta – {self._ehitusaasta}\n"
            f"Vanus – {self.maja_vanus} aastat\n"
            f"Korterite arv: {self._korterite_arv}\n"
            f"Elanike arv: {self._elanike_arv}\n"
            f"Elanike tihedus: {self.elanike_tihedus} elanikku per korter\n"
            f"Renoveeritud: '{tekst_renoveeritud}'\n"
            f"Maja tüüp: '{tekst_maja}'\n"
        )


def main():
    maja1 = Maja("Tombi 10", 10, 2010)
    maja2 = Maja("Tombi 11", 5, 1999)
    maja3 = Maja("Tombi 12", 2, 2020)
    maja4 = Maja("Tombi 13", 20, 2025)

    maja1.lisa_elanik()
    maja1.renoveeritud = True

    print(maja1)
    print(maja4)


if __name__ == "__main__":
    main()
