from raamat import Raamat  # impordime Raamat-klassi teisest failist

class Raamatukogu:
    def __init__(self):
        # Konstruktor – käivitatakse iga kord, kui luuakse uus Raamatukogu objekt

        # List raamatutest, mis on hetkel raamatukogus saadaval
        self.raamatud = []

        # List raamatutest, mis on kasutaja poolt laenutatud
        self.laenutatud_raamatud = []

    def lisa_raamat(self, raamat):
        # Meetod uue raamatu lisamiseks raamatukokku
        # Eeldame, et parameeter 'raamat' on Raamat-objekt
        self.raamatud.append(raamat)

    def __str__(self):
        # __str__ erimeetod määrab, kuidas Raamatukogu objekt tekstina välja näeb

        # Kui raamatukogus pole ühtegi raamatut
        if len(self.raamatud) == 0:
            return "Raamatukogu on tühi"
        else:
            # Koostame stringi kõikidest raamatutest
            raamatud_str = ""

            # Läbime kõik raamatud ja kasutame iga Raamat-objekti __str__ meetodit
            for raamat in self.raamatud:
                raamatud_str += f"{raamat}\n"

            return raamatud_str

    def kuva_raamatud(self):
        # Kuvab kõik saadaval olevad raamatud nummerdatud nimekirjana
        for index, i in enumerate(self.raamatud):
            print(f"{index+1}: {i}")

    def kuva_laenutatud_raamatud(self):
        # Kuvab kõik hetkel laenutatud raamatud

        if len(self.laenutatud_raamatud) == 0:
            print("Sa pole veel ühtegi raamatut laenutanud")
        else:
            print(f"Oled laenutanud kokku {len(self.laenutatud_raamatud)} raamatut.")

            for index, raamat in enumerate(self.laenutatud_raamatud):
                print(f"{index+1}: {raamat}")

    def on_juba_laenutatud(self, pealkiri):
        # Kontrollib, kas antud pealkirjaga raamat on juba laenutatud
        # Tagastab True või False

        for i in self.laenutatud_raamatud:
            if i.pealkiri.lower() == pealkiri.lower():
                return True

        return False

    def laenuta_raamat(self, pealkiri):
        # Proovib raamatut laenutada pealkirja alusel

        # Kui raamat on juba laenutatud, siis katkestame
        if self.on_juba_laenutatud(pealkiri) == True:
            return "juba_laenutatud"
        else:
            # Otsime raamatut saadaval olevate raamatute seast
            for index, i in enumerate(self.raamatud):
                if i.pealkiri.lower() == pealkiri.lower():
                    # Eemaldame raamatu saadaval olevatest
                    self.raamatud.remove(i)

                    # Lisame selle laenutatud raamatute hulka
                    self.laenutatud_raamatud.append(i)

                    # Kuvame laenutatud raamatu info
                    print(i)

                    return i

            # Kui sobivat raamatut ei leitud
            return None
