from raamat import Raamat #impordime raamatu

class Raamatukogu():  #loome klassi
    def __init__(self):
        self.raamatud = []
        self.laenutatud_raamatud = []


    def lisa_raamat(self, raamat):  #loome meetodi
        self.raamatud.append(raamat)

    def __str__(self):  #meetod
        if len(self.raamatud) == 0:
            return "Raamatukogu on tühi"
        else:
            raamatud_str = ""
            for raamat in self.raamatud:
                raamatud_str += f"{raamat}\n"  # kasuta Raamat.__str__ automaatselt

            return raamatud_str

    def kuva_raamatud(self):
        for index, i in enumerate(self.raamatud):
            print(f"{index+1}: {i}")

    def kuva_laenutatud_raamatud(self):
        if len(self.laenutatud_raamatud) == 0:
            print("Sa pole veel ühtegi raamatut laenutanud")
        else:
            print(f"Oled laenutanud kokku {len(self.laenutatud_raamatud)} raamatut.")
            for index, raamat in enumerate(self.laenutatud_raamatud):
                print(f"{index+1}: {raamat}")

    def on_juba_laenutatud(self, pealkiri):
        for i in self.laenutatud_raamatud:
            if i.pealkiri.lower() == pealkiri.lower():
                return True
        return False

    def laenuta_raamat(self, pealkiri):
        if self.on_juba_laenutatud(pealkiri) == True:
            return "juba_laenutatud"
        else:
            for index, i in enumerate(self.raamatud):
                if i.pealkiri.lower() == pealkiri.lower():
                    self.raamatud.remove(i)
                    self.laenutatud_raamatud.append(i)
                    print(i)
                    return i
            return None
