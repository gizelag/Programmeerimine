class Maja:
    def __init__(self, aadress: str, korterite_arv: int, ehitusaasta: int):
        self.aadress = aadress
        self.korterite_arv = korterite_arv
        self.ehitusaasta = ehitusaasta
        self.elanike_arv = 0
        self.renoveeritud = False


    def lisa_elanik(self):
        self.elanike_arv += 1
        print(f"Majja {self.aadress} lisandus uus elanik. Elanikke kokku: {self.elanike_arv}")

    def eemalda_elanik(self):
        if self.elanike_arv > 0:
            self.elanike_arv -= 1
            print(f"Majast {self.aadress} lahkus elanik. Elanikke kokku: {self.elanike_arv}")
        else:
            print(f"Majast {self.aadress} ei saa elanikku eemaldada, sest majas pole ühtegi elanikku!")

    def renoveeri(self):
        self.renoveeritud = True
        print(f"Maja {self.aadress} on nüüd renoveeritud!")

    def __str__(self):

        if self.renoveeritud == True:
            tekst = "Jah"
        else:
            tekst = "Ei"

        return (f"Maja - {self.aadress}\n"
                f"Ehitusaasta - {self.ehitusaasta}\n"
                f"Korterite arv - {self.korterite_arv}\n"
                f"Elanike arv - {self.elanike_arv}\n"
                f"renoveeritud - {self.renoveeritud}\n")

def main():

    # Loome neli erinevat maja
    vana_maja = Maja("Riia 14", 12, 1985)
    uus_maja = Maja("Tartu mnt 5", 24, 2018)
    kohvik_mandel = Maja("Veski 5", 3, 2000)
    taltech_tartu = Maja("Puiestee 78", 0, 1878)

    # Demonstreerime meetodite kasutamist
    print(vana_maja)
    vana_maja.lisa_elanik()
    vana_maja.lisa_elanik()
    vana_maja.renoveeri()
    print(vana_maja)

    print(uus_maja)
    uus_maja.lisa_elanik()
    uus_maja.eemalda_elanik()
    uus_maja.eemalda_elanik()
    uus_maja.lisa_elanik()
    uus_maja.lisa_elanik()
    print(uus_maja)

if __name__ == "__main__":
    main()

