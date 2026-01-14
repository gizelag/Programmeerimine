class Maja:
    def __init__(self, aadress: str, korterite_arv: int, ehitusaasta: int):
        # Konstruktor: loob Maja objekti ja paneb paika algse oleku
        self.aadress = aadress
        self.korterite_arv = korterite_arv
        self.ehitusaasta = ehitusaasta
        self.elanike_arv = 0          # Alguses eeldame, et elanikke pole
        self.renoveeritud = False     # Algolekus maja ei ole renoveeritud

    def lisa_elanik(self):
        # Suurendab elanike arvu – simuleerib uue elaniku sissekolimist
        self.elanike_arv += 1
        print(f"Majja {self.aadress} lisandus uus elanik. Elanikke kokku: {self.elanike_arv}")

    def eemalda_elanik(self):
        # Eemaldab elaniku ainult siis, kui neid on olemas
        if self.elanike_arv > 0:
            self.elanike_arv -= 1
            print(f"Majast {self.aadress} lahkus elanik. Elanikke kokku: {self.elanike_arv}")
        else:
            # Kaitse olukorra vastu, kus elanikke pole
            print(f"Majast {self.aadress} ei saa elanikku eemaldada, sest majas pole ühtegi elanikku!")

    def renoveeri(self):
        # Muudab maja olekut – märgib, et renoveerimine on tehtud
        self.renoveeritud = True
        print(f"Maja {self.aadress} on nüüd renoveeritud!")

    def __str__(self):
        # Tagastab Maja objekti inimesele loetaval kujul
        return (f"Maja - {self.aadress}\n"
                f"Ehitusaasta - {self.ehitusaasta}\n"
                f"Korterite arv - {self.korterite_arv}\n"
                f"Elanike arv - {self.elanike_arv}\n"
                f"Renoveeritud - {self.renoveeritud}\n")


def main():
    # Loome mõned Maja objektid erinevate andmetega
    vana_maja = Maja("Riia 14", 12, 1985)
    uus_maja = Maja("Tartu mnt 5", 24, 2018)
    kohvik_mandel = Maja("Veski 5", 3, 2000)
    taltech_tartu = Maja("Puiestee 78", 0, 1878)

    # Katsetame meetodeid ja vaatame, kuidas objektide olek muutub
    print(vana_maja)
    vana_maja.lisa_elanik()
    vana_maja.lisa_elanik()
    vana_maja.renoveeri()
    print(vana_maja)

    print(uus_maja)
    uus_maja.lisa_elanik()
    uus_maja.eemalda_elanik()
    uus_maja.eemalda_elanik()  # Siin tekib olukord, kus elanikke enam pole
    uus_maja.lisa_elanik()
    uus_maja.lisa_elanik()
    print(uus_maja)


if __name__ == "__main__":
    main()
