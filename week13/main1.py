from zoo import *
from animals import *

def main():
    # Loo loomaaed
    zoo = Zoo()

    # Loon koera objekti
    # Koerad
    rex = Dog(name="Rex", age=5, gender="Male", weight=25.5, hair_color="Brown", breed="Labrador")
    bella = Dog(name = "Bella", age=3, gender="Female", weight=18.2, hair_color="Black", breed="Border Collie")

    # Kassid
    shadow = Cat(name="Shadow", age=3, gender="Female", weight=4.5, hair_color="Gray", indoor_cat=False)
    nafta = Cat("Nafta", 1, "Male", 3.7, "Black", True)

    # Linnud
    kotkas_toomas = Eagle(name="Toomas", age=8, gender="Male", weight=4.4, wingspan=180.6, can_fly=True)
    pingu_joosep = Penguin("Joosep", 4, "Male", 15.0, 30.0, can_fly=False)

    # Haikala
    hai_taavi = Shark(name="Taavi", age=12, gender="Male", weight=200.0, max_depth=500, water_type="Salty", danger_level=9)

    # Lisame loomaaeda
    loomad = [rex, shadow, bella, nafta, kotkas_toomas, pingu_joosep, hai_taavi]
    for a in loomad:
        zoo.add_animal(a)

    # Kuvame kõik loomad
    zoo.show_all_animals()

    # Polümorfism - söötmine ja kuulamine. eri klasside objektid võivad kasutada sama meetodit, kuid iga objekt teeb seda omal viisil.
    zoo.feed_and_listen_all_the_animals()

if __name__ == "__main__":
    main()
