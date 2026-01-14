# Impordime abstraktse baasklassi ja abstraktse meetodi toe
from abc import ABC, abstractmethod


# Abstraktne baasklass Animal
# Sellest klassist ei saa otseselt objekte luua
class Animal(ABC):

    # Looma tüüp (nt dog, cat, bird jne)
    # Seda kasutatakse vanuse arvutamisel
    animal_type = None

    def __init__(self, name, age: int, gender, weight):
        # Kontrollime, kas vanus on korrektne
        if not Animal.is_valid_age(age):
            raise ValueError(f"Looma {name} vanus peab olema 0-100 vahel! Saadud: {age}")

        # Objekti omadused
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    # Staatiline meetod – ei kasuta self ega cls
    # Kontrollib, kas vanus on korrektne
    @staticmethod
    def is_valid_age(age):
        if not isinstance(age, int):
            return False
        if age < 0 or age > 100:
            return False
        return True

    # Klassimeetod – kasutab cls
    # Arvutab looma vanuse inim-aastates
    @classmethod
    def calc_age_in_human_years(cls, age):
        looma_age_dict = {
            "dog": 7,
            "cat": 6,
            "bird": 4,
            "fish": 2
        }

        if cls.animal_type in looma_age_dict:
            return age * looma_age_dict[cls.animal_type]

    # Tavaline meetod – kõik loomad söövad
    def eat(self):
        print(f"{self.name} sööb maitsvat toitu")

    # Tavaline meetod – kõik loomad magavad
    def sleep(self):
        print(f"{self.name} magab magusalt")

    # Tagastab vanuse inim-aastates
    def get_human_years(self):
        return self.__class__.calc_age_in_human_years(self.age)

    # Abstraktne meetod
    # Iga alamklass PEAB selle ise defineerima
    @abstractmethod
    def make_sound(self):
        pass

    # Objekti tekstiline esitus
    def __repr__(self):
        return (
            f"\nAnimal name: {self.name}\n"
            f"Age: {self.age} years ({self.get_human_years()} in human years)\n"
            f"Gender: {self.gender}\n"
            f"Weight: {self.weight}kg\n"
        )


# Mammal klass pärib Animal klassist
class Mammal(Animal):
    def __init__(self, name, age, gender, weight, hair_color):
        super().__init__(name, age, gender, weight)
        self.hair_color = hair_color

    def __repr__(self):
        return super().__repr__() + f"Hair color: {self.hair_color}\n"


# Bird klass
class Bird(Animal):
    animal_type = "bird"

    def __init__(self, name, age, gender, weight, wingspan, can_fly):
        super().__init__(name, age, gender, weight)
        self.wingspan = wingspan
        self.flying_ability = can_fly

    def __repr__(self):
        tekst = "Yes" if self.flying_ability else "No"
        return super().__repr__() + f"Wingspan: {self.wingspan}cm. Can fly: {tekst}\n"


# Fish klass
class Fish(Animal):
    animal_type = "fish"

    def __init__(self, name, age, gender, weight, max_depth, water_type):
        super().__init__(name, age, gender, weight)
        self.max_depth = max_depth
        self.water_type = water_type

    def __repr__(self):
        return super().__repr__() + f"Max depth: {self.max_depth}m Water type: {self.water_type}\n"


# Dog klass – imetaja
class Dog(Mammal):
    animal_type = "dog"

    def __init__(self, name, age, gender, weight, hair_color, breed):
        super().__init__(name, age, gender, weight, hair_color)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} haugub: Auh Auh!")

    def __repr__(self):
        return super().__repr__() + f"Dog breed: {self.breed}\n"


# Cat klass – imetaja
class Cat(Mammal):
    animal_type = "cat"

    def __init__(self, name, age, gender, weight, hair_color, indoor_cat):
        super().__init__(name, age, gender, weight, hair_color)
        self.indoor_cat = indoor_cat

    def make_sound(self):
        print(f"{self.name} näugub: Mjäu Mjäu!")

    def __repr__(self):
        tekst = "Yes" if self.indoor_cat else "No"
        return super().__repr__() + f"Indoor cat: {tekst}\n"


# Eagle klass – lind
class Eagle(Bird):
    def make_sound(self):
        print(f"{self.name} karjub: Kiih Kiih")


# Penguin klass – lind
class Penguin(Bird):
    def make_sound(self):
        print(f"{self.name} kvääksub: Kvääk Kvääk")


# Shark klass – kala
class Shark(Fish):
    def __init__(self, name, age, gender, weight, max_depth, water_type, danger_level):
        super().__init__(name, age, gender, weight, max_depth, water_type)

        # Kontrollime ohu taset
        if danger_level <= 0 or danger_level > 10:
            raise ValueError("Danger level must be between 1–10")

        self.danger_level = danger_level

    def make_sound(self):
        print(f"{self.name} teeb: Mull Mull")

    def __repr__(self):
        return super().__repr__() + f"Danger level: {self.danger_level}/10\n"
