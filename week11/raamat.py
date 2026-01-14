class Raamat():   #loome klassi nimega raamat
    def __init__(self, pealkiri:str, autor:str, lehekuljed:int, liik:str):
        self.pealkiri = pealkiri    #lisame atribuudid
        self.autor = autor
        self.lehekuljed = lehekuljed
        self.liik = liik

    def __str__(self):
        return f"{self.pealkiri}, {self.autor}, {self.lehekuljed}, {self.liik}"
    # __str__ on erimeetod, mis määrab,
    # kuidas objekt stringina (tekstina) välja näeb

    # Tagastame stringi, mis koosneb objekti atribuutidest:
    # pealkiri, autor, lehekülgede arv ja liik