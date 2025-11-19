class Liikumisvahend():
    def __init__(self, firma:str, alustustasu: float, saja_meetri_hind : float, soidukaugus : float):
        self.firma = firma      #loome atribuudid
        self.alustustasu = alustustasu
        self.saja_meetri_hind = saja_meetri_hind
        self.soidukaugus = soidukaugus
        self.hind = None

    def soidu_hind(self, pikkus):#loon meetodi
        if self.soidukaugus < pikkus:
            return 1000
        else:
            return self.alustustasu + (pikkus * 10 * self.saja_meetri_hind)

    def soida(self, pikkus):  #loon meetodi
        self.soidukaugus -= pikkus
        if self.soidukaugus < 0:
            self.soidukaugus = 0
            return 0

    def lae(self, kilomeetrid):
        self.soidukaugus += kilomeetrid

    def __str__(self):
        return (f"Firma: {self.firma}, Alustustasu: {self.alustustasu}, 100m hind: {self.saja_meetri_hind}, SÃµidukaugus: {self.soidukaugus}")
