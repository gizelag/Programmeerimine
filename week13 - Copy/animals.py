class Zoo():
    def __init__(self, zoo_name = "Tallinna Loomaaed"):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.zoo_name}: Loom {animal.name} lisatud!")


    def feed_and_listen_all_the_animals(self):
        for a in self.animals:
            a.eat()
            a.make_sound()

    def show_all_animals(self):
        index = 0
        for a in self.animals:
            index += 1
            print(f"Animal nr. {index}"
                  f"{a.__repr__()}")

