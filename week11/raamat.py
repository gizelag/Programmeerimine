class Raamat():   #loome klassi nimega raamat
    def __init__(self, pealkiri:str, autor:str, lehekuljed:int, liik:str):
        self.pealkiri = pealkiri    #lisame atribuudid
        self.autor = autor
        self.lehekuljed = lehekuljed
        self.liik = liik

    def __str__(self):
        return f"{self.pealkiri}, {self.autor}, {self.lehekuljed}, {self.liik}"