# =========================
# ABSTRACT KLASSIDE TUGI
# =========================
from abc import ABC, abstractmethod
# ABC = Abstract Base Class
# abstractmethod = meetod, mis PEAB olema alamklassides olemas


# =========================
# VANEM KLASS: Animal (ABSTRACT)
# =========================
class Animal(ABC):
    # KLASSIMUUTUJA
    # Ühine kõigile alamklassidele
    animal_type = None

    def __init__(self, name, age: int, gender, weight):

        # Kontrollime vanuse sobivust staatilise meetodiga
        if not Animal.is_valid_age(age):
            # Kui vanus on vale → error
            raise ValueError(
                f"Looma {name} vanus peab olema 0-100 vahel! Saadud: {age}"
            )

        # Isendi (objekti) muutujad
        self.name = name          # looma nimi
        self.age = age            # looma vanus
        self.gender = gender      # sugu
        self.weight = weight      # kaal

    # =========================
    # STATICMETHOD
    # =========================
    # Ei kasuta self ega cls
    # Lihtne abifunktsioon
    @staticmethod
    def is_valid_age(age):
        # Kontrollime, kas on täisarv
        if not isinstance(age, int):
            return False

        # Kontrollime vahemikku
        if 100 < age or age < 0:
            return False

        return True

    # =========================
    # CLASSMETHOD
    # =========================
    # Kasutab KLASSI (cls), mitte objekti
    # Sobib, kui loogika sõltub klassist
    @classmethod
    def calc_age_in_human_years(cls, age):
        # Sõnastik looma → inimese aastate suhe
        looma_age_dict = {
            "dog": 7,
            "cat": 6,
            "bird": 4,
            "fish": 2
        }

        # Kontrollime, kas klassil on animal_type määratud
        if cls.animal_type in looma_age_dict:
            return age * looma_age_dict[cls.animal_type]

    # =========================
    # TAVALINE MEETOD
    # =========================
    def eat(self):
        print(f"{self.name} sööb maitsvat toitu")

    def sleep(self):
        print(f"{self.name} magab magusalt")

    # =========================
    # MEETOD, MIS KUTSUB CLASSMETHODI
    # =========================
    def get_human_years(self):
        # self.__class__ → objekti tegelik klass (Dog, Cat jne)
        return self.__class__.calc_age_in_human_years(self.age)

    # =========================
    # ABSTRACTMETHOD
    # =========================
    # PEAB OLEMA IGAS ALAMKLASSIS
    @abstractmethod
    def make_sound(self):
        pass

    # =========================
    # OBJEKTI TEKSTILINE ESITUS
    # =========================
    def __repr__(self):
        return (
            f"\nAnimal name: {self.name}\n"
            f"Age: {self.age} years ({self.get_human_years()} in human years)\n"
            f"Gender: {self.gender}\n"
            f"Weight: {self.weight}kg\n"
        )


# =========================
# MAMMAL – NOOREM KLASS
# =========================
class Mammal(Animal):
    def __init__(self, name, age, gender, weight, hair_color):
        # super() → kutsub Animal __init__
        super().__init__(name, age, gender, weight)

        # Spetsiifiline omadus imetajatele
        self.hair_color = hair_color

    def __repr__(self):
        return super().__repr__() + f"Hair color: {self.hair_color}\n"


# =========================
# BIRD – NOOREM KLASS
# =========================
class Bird(Animal):
    animal_type = "bird"  # määrab classmethodi loogika

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight)

        self.wingspan = wingspan        # tiibade siruulatus
        self.flying_ability = can_fly  # kas suudab lennata

    def __repr__(self):
        tekst = "Yes" if self.flying_ability else "No"
        return (
            super().__repr__() +
            f"Wingspan: {self.wingspan}cm. Can fly: {tekst}\n"
        )


# =========================
# FISH – NOOREM KLASS
# =========================
class Fish(Animal):
    animal_type = "fish"

    def __init__(self, name, age, gender, weight, max_depth, water_type):
        super().__init__(name, age, gender, weight)

        self.max_depth = max_depth      # max sügavus
        self.water_type = water_type    # soolane / mage

    def __repr__(self):
        return (
            super().__repr__() +
            f"Max depth: {self.max_depth}m Water type: {self.water_type}\n"
        )


# =========================
# DOG – KONKREETNE LOOM
# =========================
class Dog(Mammal):
    animal_type = "dog"

    def __init__(self, name, age, gender, weight, hair_color, breed):
        super().__init__(name, age, gender, weight, hair_color)

        self.breed = breed  # tõug

    # ABSTRACTMETHODI REALISEERIMINE
    def make_sound(self):
        print(f"\n{self.name} haugub: Auh, Auh!\n")

    def __repr__(self):
        return super().__repr__() + f"Dog breed: {self.breed}\n"


# =========================
# CAT
# =========================
class Cat(Mammal):
    animal_type = "cat"

    def __init__(self, name, age, gender, weight, hair_color, indoor_cat):
        super().__init__(name, age, gender, weight, hair_color)

        self.indoor_cat = indoor_cat  # kas toakass

    def make_sound(self):
        print(f"{self.name} näugub: Mjäu Mjäu!")

    def __repr__(self):
        tekst = "Yes" if self.indoor_cat else "No"
        return super().__repr__() + f"Indoor cat: {tekst}\n"


# =========================
# EAGLE
# =========================
class Eagle(Bird):
    def make_sound(self):
        print(f"{self.name} karjub: Kiih Kiih")


# =========================
# PENGUIN
# =========================
class Penguin(Bird):
    def make_sound(self):
        print(f"\n{self.name} kvääksub: Kvääk Kvääk\n")


# =========================
# SHARK
# =========================
class Shark(Fish):
    def __init__(self, name, age, gender, weight, max_depth, water_type, danger_level):
        super().__init__(name, age, gender, weight, max_depth, water_type)

        # Kontrollime ohu taset
        if danger_level <= 0 or danger_level > 10:
            raise ValueError("Danger level must be 1–10!")

        self.danger_level = danger_level

    def make_sound(self):
        print(f"{self.name} teeb: Mull Mull")

    def __repr__(self):
        return super().__repr__() + f"Danger level: {self.danger_level}/10\n"
