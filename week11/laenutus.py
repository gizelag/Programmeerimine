from liikumisvahend import Liikumisvahend


class Laenutus:
    def __init__(self, liikumisvahendid: list):
        # Laenutuses olevate liikumisvahendite nimekiri
        # Iga element peaks olema Liikumisvahend tüüpi objekt
        self.liikumisvahendid = liikumisvahendid

    def kuva_valik(self, pikkus: float):
        # Kuvab kõik liikumisvahendid koos hinnaga
        # antud sõidupikkuse jaoks
        rattad_ja_hinnad = []

        try:
            # Käime kõik liikumisvahendid läbi
            for i in self.liikumisvahendid:
                # Arvutame, kui palju maksab selle vahendiga sõit
                hind = i.soidu_hind(pikkus)

                # Salvestame firma nime ja hinna tuple’ina
                # et saaksime hiljem hinna järgi sorteerida
                rattad_ja_hinnad.append((i.firma, hind))

            # Sorteerime liikumisvahendid hinna järgi (odavaim ees)
            rattad_ja_hinnad.sort(key=lambda x: x[1])

            # Kuvame nummerdatud nimekirja
            for index, (firma, hind) in enumerate(rattad_ja_hinnad):
                print(f"{index + 1}. {firma} - {hind} eurot")

        except FileNotFoundError:
            print("Viga faili saamisel")
            return None
        except Exception as e:
            print(e)
            return None

    def laenuta(self, firma, pikkus):
        # Proovib laenutada valitud firma liikumisvahendi
        # kontrollib, kas aku lubab soovitud pikkusega sõitu
        try:
            for i in self.liikumisvahendid:
                # Kontrollime, kas firma nimi sobib
                if i.firma in firma:
                    # Kui sõidukaugus on liiga väike
                    if i.soidukaugus < pikkus:
                        print("Liikumisvahendi aku on liiga tühi selle sõidu jaoks.")
                    else:
                        # Arvutame hinna ja sooritame sõidu
                        hind = i.soidu_hind(pikkus)
                        print(f"Laenutan {firma}, sõidupikkus {pikkus}")
                        print(f"Sõidu hind oli {hind} eurot\n")

                        # Vähendame aku taset
                        i.soida(pikkus)
                else:
                    continue

        except Exception as e:
            print(e)

    def lae_liikumisvahendit(self, firma, kilomeetrid):
        # Laeb valitud firma liikumisvahendit
        # lisades sellele sõidukaugust
        try:
            for i in self.liikumisvahendid:
                if i.firma in firma:
                    i.lae(kilomeetrid)
                else:
                    continue

        except Exception as e:
            print(e)
