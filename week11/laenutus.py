from liikumisvahend import Liikumisvahend

class Laenutus():
    def __init__(self, liikumisvahendid : list):
        self.liikumisvahendid = liikumisvahendid

    def kuva_valik(self, pikkus: float):
        rattad_ja_hinnad = []
        try:
            for i in self.liikumisvahendid:
                hind = i.soidu_hind(pikkus)

                #List selleks, et saaksime nad järjekorda panna ja kuvada
                rattad_ja_hinnad.append((i.firma, hind))

            # sorteeri hinna järgi
            rattad_ja_hinnad.sort(key=lambda x: x[1])
            for index, (firma,hind) in enumerate(rattad_ja_hinnad):
                print(f"{index+1}. {firma} - {hind} eurot")

        except FileNotFoundError:
            print("Viga file saamisel")
            return None
        except Exception as e:
            print(e)
            return None

    def laenuta(self, firma, pikkus):
        try:
            for i in self.liikumisvahendid:
                if i.firma in firma:
                    if i.soidukaugus < pikkus:
                        print("Liikumisvahendi aku on liiga tühi selle sõidu jaoks.")
                    else:
                        hind = i.soidu_hind(pikkus)
                        print(f"Laenutan {firma}, sõidupikkus {pikkus}")
                        print(f"Sõidu hind oli {hind} eurot\n")
                        i.soida(pikkus)
                else:
                    continue
        except Exception as e:
            print(e)

    def lae_liikumisvahendit(self, firma, kilomeetrid):
        try:
            for i in self.liikumisvahendid:
                if i.firma in firma:
                    i.lae(kilomeetrid)
                else:
                    continue
        except Exception as e:
            print(e)

